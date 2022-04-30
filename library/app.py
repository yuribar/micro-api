#!/usr/bin/env python

from tokenize import String
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Qwert78940*@mysql/microservice'

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

    # Selecionar Tudo
@app.route("/usuarios", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]

    return jsonify(200, "usuarios", usuarios_json)

# Selecionar Individual
@app.route("/usuario/<id>", methods=["GET"])
def seleciona_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    usuario_json = usuario_objeto.to_json()

    return jsonify(200, "usuario", usuario_json)

   
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    