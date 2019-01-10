from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry


db = SQLAlchemy()


class Incident(db.Model):
    __tablename__ = 'incidents'

    incident_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    發生日期 = db.Column(db.Date)
    發生時間 = db.Column(db.String(10))
    發生年度 = db.Column(db.Integer)
    發生月份 = db.Column(db.Integer)
    發生星期 = db.Column(db.String(2))
    到場處理日期 = db.Column(db.String(10))
    到場處理時間 = db.Column(db.String(10))
    結束_事故排除_日期 = db.Column(db.String(10))
    結束_事故排除_時間 = db.Column(db.String(10))
    GPS經度 = db.Column(db.Float)
    GPS緯度 = db.Column(db.Float)
    geo = db.Column(Geometry("POINT"))
    事故類別名稱 = db.Column(db.String(10))
    地址類型名稱 = db.Column(db.String(10))
    發生縣市名稱 = db.Column(db.String(10))
    發生市區鄉鎮名稱 = db.Column(db.String(10))
    發生地址_村里代碼 = db.Column(db.String(20))
    發生地址_鄰 = db.Column(db.String(10))
    發生地址_路街代碼 = db.Column(db.String(20))
    發生地址_路街 = db.Column(db.String(10))
    發生地址_段 = db.Column(db.String(10))
    發生地址_巷 = db.Column(db.String(10))
    發生地址_弄 = db.Column(db.String(10))
    發生地址_號 = db.Column(db.String(10))
    發生地址_前幾公尺 = db.Column(db.String(10))
    發生地址_側名稱 = db.Column(db.String(10))
    發生交叉路口_村里名稱 = db.Column(db.String(10))
    發生交叉路口_路街口 = db.Column(db.String(10))
    發生交叉路口_段 = db.Column(db.String(10))
    發生交叉路口_巷 = db.Column(db.String(10))
    發生交叉路口_弄 = db.Column(db.String(10))
    發生地址_其他 = db.Column(db.String(70))
    死亡人數_24小時內 = db.Column(db.Integer)
    死亡人數_2_30日內 = db.Column(db.Integer)
    受傷人數 = db.Column(db.Integer)
    天候代碼 = db.Column(db.String(10))
    光線代碼 = db.Column(db.String(10))
    道路第1當事者_代碼 = db.Column(db.String(10))
    速限_第1當事者 = db.Column(db.String(10))
    道路型態大類別代碼 = db.Column(db.String(10))
    道路型態子類別代碼 = db.Column(db.String(10))
    事故位置大類別代碼 = db.Column(db.String(10))
    事故位置子類別代碼 = db.Column(db.String(10))
    路面狀況_路面鋪裝代碼 = db.Column(db.String(10))
    路面狀況_路面狀態代碼 = db.Column(db.String(10))
    路面狀況_路面缺陷代碼 = db.Column(db.String(10))
    道路障礙_障礙物代碼 = db.Column(db.String(10))
    道路障礙_視距品質代碼 = db.Column(db.String(10))
    道路障礙_視距代碼 = db.Column(db.String(10))
    號誌_號誌種類代碼 = db.Column(db.String(10))
    號誌_號誌動作代碼 = db.Column(db.String(10))
    車道劃分設施_分向設施大類別代碼 = db.Column(db.String(10))
    車道劃分設施_分向設施子類別代碼 = db.Column(db.String(10))
    車道劃分設施_快車道或一般車道間代碼 = db.Column(db.String(10))
    車道劃分設施_快慢車道間代碼 = db.Column(db.String(10))
    車道劃分設施_路面邊線代碼 = db.Column(db.String(10))
    事故類型及型態大類別代碼 = db.Column(db.String(10))
    事故類型及型態子類別代碼 = db.Column(db.String(10))
    肇因研判大類別代碼_主要 = db.Column(db.String(10))
    肇因研判子類別代碼_主要 = db.Column(db.String(10))
    國籍 = db.Column(db.String(10))
    牌照種類代碼 = db.Column(db.String(10))
    乘坐車輛的牌照種類代碼 = db.Column(db.String(10))
    乘坐車輛的當事者區分_大類別代碼_車種 = db.Column(db.String(10))
    乘坐車輛的當事者區分_子類別代碼_車種 = db.Column(db.String(10))
    受傷程度代碼 = db.Column(db.String(10))
    主要傷處代碼 = db.Column(db.String(10))
    保護裝備代碼 = db.Column(db.String(10))
    行動電話_電腦或其他相類功能裝置代碼 = db.Column(db.String(10))
    車輛用途代碼 = db.Column(db.String(10))
    當事者行動狀態大類別代碼 = db.Column(db.String(10))
    當事者行動狀態子類別代碼 = db.Column(db.String(10))
    駕駛資格情形代碼 = db.Column(db.String(10))
    駕駛執照種類大類別代碼 = db.Column(db.String(10))
    駕駛執照種類子類別代碼 = db.Column(db.String(10))
    飲酒情形代碼 = db.Column(db.String(10))
    車輛撞擊部位大類別代碼_最初 = db.Column(db.String(10))
    車輛撞擊部位子類別代碼_最初 = db.Column(db.String(10))
    車輛撞擊部位大類別代碼_其他 = db.Column(db.String(10))
    車輛撞擊部位子類別代碼_其他 = db.Column(db.String(10))
    肇因研判大類別代碼_個別 = db.Column(db.String(10))
    肇因研判子類別代碼_個別 = db.Column(db.String(10))
    肇事逃逸類別代碼_是否肇逃 = db.Column(db.String(10))
    職業代碼 = db.Column(db.String(10))
    旅次目的代碼 = db.Column(db.String(10))

    def _asdict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns
                if c.name != 'geo'}

    @classmethod
    def add_incident(cls, incident):
        keys = Incident.__table__.columns.keys()
        geo = 'POINT({} {})'.format(incident.GPS經度, incident.GPS緯度)
        incident = Incident(**{k:v for k, v in incident._asdict().items() if k in keys}, geo=geo)
        db.session.add(incident)
        db.session.commit()

    @classmethod
    def add_incidents(cls, incidents):
        keys = Incident.__table__.columns.keys()
        for i in incidents:
            geo = 'POINT({} {})'.format(i.GPS經度, i.GPS緯度)
            if i.發生日期 == 'NA':
                continue
            incident = Incident(**{k:v.replace('NA', '-1').replace(' ', '') for k, v in i._asdict().items() if k in keys}, geo=geo)
            db.session.add(incident)
        db.session.commit()


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///test'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
