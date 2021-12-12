#from market import app
from flask import Flask, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm
from market import db
from flask_login import login_user
app = Flask(__name__)

@app.route('/')
def hello_world():
	return '<h1>Changed text!</h1>'

@app.route('/home')
def home_page():
	return render_template('home.html')

@app.route('/market')
def market_page():
#     items = [
#    	{'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
#    	{'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
#    	{'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
#     ]
	items = Item.query.all()
	return render_template('market.html', items=items)

@app.route('/register')
def register_page():
	form = RegisterForm()
	if form.validate_on_submit():
	     user_to_create = User(username=form.username.date,
		email_address=form.email_address.data,
		password=form.password1.data)
	     db.session.add(user_to_create)
	     db.session.commit()
	     return redirect(url_for('market_page'))
	if form.errors != {}: #If there are not errors from the validation
		for err_msg in form.errors.values():
			flash(f'There was an error with creating a user:{err_msg}')
	return render_template('register.html', form=form)

@app.route('/login', method=['GET', 'POST'])
def login_page():
	form = LoginForm()
	if form.validate_on_submit():
		attemted_user = User.query.filter_by(username=form.username.data).first()
		if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
			login_user(attempted_user)
			flash(f'Success! You are logged n as: {attempted_user.username}', category='success')
			return redirect(url_for('market_page'))
		else:
			flash('Username and password are not match! Please try again', category='danger')

	return render_template('login.html', form=form)