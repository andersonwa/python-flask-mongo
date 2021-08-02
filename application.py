from flask import Flask, request
from pymongo import MongoClient
from bson.json_util import dumps
import datetime

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
databse = client['teste-python']
testCollection = databse.test_collection


@app.route('/find-one')
def findOne():
  item = testCollection.find_one()
  return dumps(item)

@app.route('/find-all')
def findAll():
  items = testCollection.find()
  return dumps(items)

@app.route('/')
def hello():
  musica = {
    "nome": "Nothing left to say",
    "banda": "Imagine Dragons",
    "categorias": ["indie", "rock"],
    "lancamento": datetime.datetime.now()
  }

  musica = testCollection.insert_one(musica)
  print(musica)
  return "oi"

app.run(debug=True)