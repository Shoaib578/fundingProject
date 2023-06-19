from application import db
from datetime import datetime

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    working_package_id = db.Column(db.ForeignKey('working_package.package_id'))
    task_name = db.Column(db.String(200))
    task_description = db.Column(db.Text)
    created_date = db.Column(db.DateTime, default=datetime.utcnow,nullable=False)
    due_date = db.Column(db.String(30), nullable=True)
