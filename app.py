from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
app=Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))
#Database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
#init db
db=SQLAlchemy(app)
#init ma
ma=Marshmallow(app)
#Product Class/Model
class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    description=db.Column(db.String(200))
    price=db.Column(db.Float)
    qty=db.Column(db.Integer)
    def __init__(self,name,description,price,qty):
        self.name=name
        self.description=description
        self.price=price
        self.qty=qty
#product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields=('id','name','description','price','qty')
#init schema
product_schema=ProductSchema()
products_schema=ProductSchema(many=True)
#Run server
if __name__=='__main__' :
    app.run(debug=True,port="9000")
