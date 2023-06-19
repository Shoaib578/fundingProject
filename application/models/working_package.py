from application import db
from datetime import datetime

class WorkingPackage(db.Model):
    package_id = db.Column(db.Integer, primary_key=True)
    package_name = db.Column(db.String(200))
    module_id = db.Column(db.ForeignKey('module.module_id'))
    company_id = db.Column(db.ForeignKey('company.company_id'),nullable=True)
    package_parent = db.Column(db.String(400))
    
    created_date = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)

