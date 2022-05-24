from flask import Blueprint, render_template, request, flash, jsonify
from .models import User
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from . import db
import json
from bson import ObjectId

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if db.event.count_documents({}) > 0:
        events = db.event.find({}, {'_id': 1, 'EN_PGM_NAME': 1, 'PGM_START_DATE': 1, 'EN_VENUE': 1, 'EN_ACT_TYPE_NAME': 1})
    else:
        events = {}

    if request.method == 'POST':
        pass
    return render_template('index.html', user=current_user, events=events)


@views.route('/event=<string:event_id>', methods=['GET', 'POST'])
@login_required
def view_event(event_id):
    _id = ObjectId(event_id)
    event = db.event.find_one({'_id': _id})
    if request.method == 'POST':
        user = db.user.find_one({'user_name': current_user.user_name})
        if event['_id'] not in user['event_id']:
            db.user.update_one({'user_name': current_user.user_name}, {'$addToSet': {'event_id': _id}})
        else:
            db.user.update_one({'user_name': current_user.user_name}, {'$pull': {'event_id': _id}})
    return render_template('event.html', user=current_user, event=event)


@views.route('/fav')
@login_required
def fav():
    user = db.user.find_one({'user_name': current_user.user_name})
    events = {}
    if 'event_id' in user.keys():
        events = db.event.find({'_id': {'$in': user['event_id']}})
    return render_template('fav.html', user=current_user, events=events)


@views.route('/about')
def about():
    return render_template('about.html', user=current_user)
