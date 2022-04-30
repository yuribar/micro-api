#!/usr/bin/env python

from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json



app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Qwert78940*@localhost/microservice'

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
    
    def to_json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}

@app.route("/")
def hello():
    return "Bem - vindo a API !\n"

app.run()
    