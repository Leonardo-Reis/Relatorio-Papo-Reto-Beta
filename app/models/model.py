import re
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    
    def __repr__(self):
        return f"<User {self.nome}>"

