from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form.get('userName')
        password = request.form.get('password')
        user = db.user.find_one({'user_name': user_name})
        if user_name == user['user_name'] and check_password_hash(user['password'], password):
            user = User(user['_id'], user['user_name'], user['password'])
            login_user(user)
            return redirect(url_for('views.home'))
        else:
            flash('Wrong login credentials', 'danger')
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
