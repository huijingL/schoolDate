from app import db

class sys_user(db.Document):
    username = db.StringField()
    password = db.StringField()