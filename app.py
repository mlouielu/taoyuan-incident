# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_compress import Compress
from sqlalchemy import func


import main
import model
from model import Incident


DATA = []
ALL_FILTERS = {}

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
Compress(app)
CORS(app, resources={r'/*': {'origins': '*'}})


def load_incident_data():
    global DATA, ALL_FILTERS
    data = ['traffic106_c.csv', 'traffic107_c.csv']
    DATA = []
    for d in data:
        DATA.extend(main.read_csv(d))
    ALL_FILTERS = main.get_all_category_with_id(DATA)


@app.route('/filters')
def filters():
    return jsonify(ALL_FILTERS)


@app.route('/incidents')
def incidents():
    return jsonify({'data': DATA})


@app.route('/incidents/<float:lat1>/<float:lng1>/<float:lat2>/<float:lng2>',
           methods=['GET', 'POST'])
def incidents_by_bounds(lat1, lng1, lat2, lng2):
    q = Incident.query.filter(
        Incident.geo.intersects(func.ST_MakeEnvelope(lng1, lat1, lng2, lat2, 4326)))
    if request.method == 'POST':
        for k, v in request.get_json().items():
            if not v:
                continue
            q = q.filter(getattr(Incident, k).in_(v))
    q = q.all()
    return jsonify([i._asdict() for i in q])


if __name__ == '__main__':
    load_incident_data()
    model.connect_to_db(app)
    model.db.create_all()
    #Incident.add_incidents(DATA)
    app.run(debug=True)
