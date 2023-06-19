from application import db
from datetime import datetime

class Module(db.Model):
    module_id = db.Column(db.Integer, primary_key=True)
    module_name = db.Column(db.String(200))
    fund_id = db.Column(db.ForeignKey('fund.fund_id'))
    company_id = db.Column(db.ForeignKey('company.company_id'),nullable=True)
    user_id = db.Column(db.ForeignKey('user.id'),nullable=True)

    created_date = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)

