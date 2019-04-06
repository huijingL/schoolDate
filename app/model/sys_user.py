from app import db

class sys_user(db.Document):
    username = db.StringField()
    password = db.StringField()

    def to_json(self):
        return {
            'username': self.username,
            'password': self.password,
        }