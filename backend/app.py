### IMPORTS ###
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


### SET UP ###
# Init app
app = Flask(__name__)
# Current directory
basedir = os.path.abspath(os.path.dirname(__file__))
# Database in correct directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "db.sqlite")
# Suppress complaints
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


### DEFINITIONS ###
# Product Class/Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

    # Constructor
    def __init__(self, id, public_id, name, password, admin):
        self.id = id
        self.public_id = public_id
        self.name = name
        self.password = password
        self.admin = admin

# User Schema
#class UserSchema(ma.Schema):
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        #fields = ('id', 'public_id', 'name', 'password', 'admin')
        load_instance = True
        model = User

# Init Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)


### ROUTES ###
# Health 
@app.route('/')
def hello_world():
    return "Flask Dockerized!"

# Test
@app.route('/test', methods=['GET'])
def get():
    return jsonify({ 'msg': 'returning Hello World' })

# User Creation
@app.route('/user', methods=['POST'])
def add_user():
    id = request.json['id']
    public_id = request.json['public_id']
    name = request.json['name']
    password = request.json['password']
    admin = request.json['admin']
    # Instantiate User
    new_user = User(id, public_id, name, password, admin)
    # Add user to db
    db.session.add(new_user)
    db.session.commit()
    # Respond with new user
    return user_schema.jsonify(new_user)

# Retrieve All Users
@app.route('/user', methods=['GET'])
def get_users():
    all_users = User.query.all()
    print(all_users)
    result = jsonify(users_schema.dump(all_users))
    return (result)
    

# Retrieve Single User
@app.route("/user/<id>", methods=['GET'])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.dump(user)


### SERVER ###
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)