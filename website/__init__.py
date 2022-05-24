from flask import Flask
from flask_pymongo import PyMongo
from bson import ObjectId
from flask_login import LoginManager, AnonymousUserMixin
from werkzeug.security import generate_password_hash
import json
import urllib.request

client = PyMongo()
DB_NAME = 'event-app'
db = client.db


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CSCI2720ProjectRemake'
    app.config['MONGO_URI'] = f'mongodb://localhost:27017/{DB_NAME}'
    client.init_app(app=app)
    global db
    db = client.db
    create_database(db)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(_id):
        from .models import User
        user = db.user.find_one({'_id': ObjectId(_id)})
        if user:
            return User(*user.values())
        return AnonymousUserMixin()

    return app


def create_database(db):
    from .models import user_schema, event_schema
    if db.user is None:
        db.create_collection('user', validator=user_schema, validateLevel='strict')
        db.user.insert_one({'user_name': 'KwokCK', 'password': generate_password_hash('123456')})
    if db.event is None:
        db.create_collection('event')
        with urllib.request.urlopen('https://www.lcsd.gov.hk/datagovhk/event/leisure_prog.json') as url:
            events = json.loads(url.read().decode())
            docs = db.event.insert_many(events)
