from flask import render_template, url_for, flash, redirect
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, EntryForm
from app.models import User, Entry
from flask_login import login_user, current_user, logout_user, login_required
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('index.html')

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.tracker'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route("/tracker", methods=['GET', 'POST'])
@login_required
def tracker():
    form = EntryForm()
    if form.validate_on_submit():
        entry = Entry(amount=form.amount.data, author=current_user)
        db.session.add(entry)
        db.session.commit()
        flash('Entry added!', 'success')
        return redirect(url_for('main.tracker'))
    entries = Entry.query.filter_by(author=current_user).all()
    return render_template('tracker.html', title='Tracker', form=form, entries=entries)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))