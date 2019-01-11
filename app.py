# -*- coding: utf-8 -*-
from collections import defaultdict

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

    total = q.count()
    q = q.order_by(func.random()).limit(1000).all()

    reasons = defaultdict(list)
    reasonsdd = defaultdict(lambda: defaultdict(int))
    for i in q:
        name = ALL_FILTERS['乘坐車輛的當事者區分_子類別代碼_車種'][
            i.乘坐車輛的當事者區分_子類別代碼_車種]
        reasonsdd['乘坐車輛的當事者區分_子類別名稱_車種'][name] += 1
        name = ALL_FILTERS['肇因研判子類別代碼_主要'][
            i.肇因研判子類別代碼_主要]
        reasonsdd['肇因研判子類別名稱_主要'][name] += 1
    for reason in reasonsdd:
        for k, v in reasonsdd[reason].items():
            reasons[reason].append([k, v])
        reasons[reason].sort(key=lambda x: x[1], reverse=True)

    return jsonify(
        {
            'data': [i._asdict() for i in q],
            'reasons': reasons,
            'total': total
        }
    )


def setup_app():
    load_incident_data()
    model.connect_to_db(app)
    model.db.create_all()


setup_app()


if __name__ == '__main__':
    load_incident_data()
    model.connect_to_db(app)
    model.db.create_all()
    #Incident.add_incidents(DATA)
    app.run(debug=True)
