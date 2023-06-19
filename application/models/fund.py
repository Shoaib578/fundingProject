from application import db
from datetime import datetime

class Fund(db.Model):
    fund_id = db.Column(db.Integer, primary_key=True)
    fund_name = db.Column(db.String(200))
    fund_description = db.Column(db.String(800))
    created_date = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)
    company_id = db.Column(db.ForeignKey('company.company_id'), nullable=True)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=True)
