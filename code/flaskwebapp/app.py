###
### Adapted from tutorial:
### https://www.youtube.com/watch?v=8aTnmsDMldY&ab_channel=PrettyPrinted
####

###
### Pet Privacy
### https://petpace.com/privacy-policy/
###


from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, IntegerField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
# Authentication Encryption Module
from werkzeug.security import generate_password_hash, check_password_hash
# login active site Module
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import request

# aRest Library for arduino
# arest.io

app = Flask(__name__)
app.config["SECRET_KEY"] = 'Thisismysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/steph/Dropbox/Academic/Duke/_Fall-2017/projects/myflaskapp/database.db'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
	# About the user
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	ownerfirstname = db.Column(db.String(80))
	ownerlastname = db.Column(db.String(80))

	username = db.Column(db.String(15), unique=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))

	ownergender = db.Column(db.String(6))
	ownerage = db.Column(db.Integer)

	# -------------- #

	# About the dog
	dogname = db.Column(db.String(20))
	dogbreed = db.Column(db.String(30))
	dogweight = db.Column(db.Integer)
	doggender = db.Column(db.String(6))
	dogage = db.Column(db.Integer)

	ee1 = db.Column(db.String(40))
	ee1Count = db.Column(db.Integer)
	ee2 = db.Column(db.String(40))
	ee2Count = db.Column(db.Integer)
	ee3 = db.Column(db.String(40))
	ee3Count = db.Column(db.Integer)


# Event Table
class EventTable(db.Model):
	__tablename__ = 'event'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	toy = db.Column(db.Integer)
	treat = db.Column(db.Integer)
	praise = db.Column(db.Integer)

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

##################
### Login Form ###
##################
class LogInForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')


###################
### Signup Form ###
###################
class RegisterForm(FlaskForm):
	# About the user
	ownerfirstname = StringField('owner first name', validators=[InputRequired(), Length(max=80)])
	ownerlastname = StringField('owner last name', validators=[InputRequired(), Length(max=80)])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])	
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	ownergender = RadioField('owner gender', validators=[InputRequired(), Length(max=6)], choices = [('M','Male'),('F','Female')])
	ownerage = IntegerField('owner age', validators=[InputRequired()])

	# About the dog
	dogname = StringField('dog name', validators=[InputRequired(), Length(max=20)])
	dogbreed = StringField('dog breed', validators=[InputRequired(), Length(max=30)])
	dogweight = IntegerField('dog weight (lbs)', validators=[InputRequired()])
	doggender = RadioField('owner gender', validators=[InputRequired(), Length(max=6)], choices = [('M','Male'),('F','Female')])	
	dogage = IntegerField('dog age', validators=[InputRequired()])

	# exitable event #1
	ee1 = StringField('exitable event 1', validators=[InputRequired(), Length(max=40)])
	# ee1Count
	ee2 = StringField('exitable event 2', validators=[InputRequired(), Length(max=40)])
	# ee2Count
	ee3 = StringField('exitable event 3', validators=[InputRequired(), Length(max=40)])
	# ee3Count


class EEForm(FlaskForm):
	exitableEvent = RadioField('Excitable Events', validators=[InputRequired(), Length(max=6)], choices = [('treat','treat'),('toy','toy'), ('praise', 'praise')])	

###############
### Routing ###
###############
@app.route('/')
def index():
	return render_template('index.html')

# login
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LogInForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password, form.password.data):
				login_user(user, remember=form.remember.data)
				return redirect(url_for('dashboard'))
		return '<h1> Invalid Username or Password </h1>'

	return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = RegisterForm()

	if form.validate_on_submit():
		# Password encryption
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		# new_user = User(username=form.username.data, email=form.email.data, password=hashed_password, ownername=form.ownername.data, ownergender=form.ownergender.data, dogname=form.dogname.data, doggender=form.doggender.data, dogbreed=form.dogbreed.data, ee1=form.ee1.data, ee2=form.ee2.data, ee3=form.ee3.data)
		new_user = User(ownerfirstname=form.ownerfirstname.data, ownerlastname=form.ownerlastname.data, username=form.username.data, email=form.email.data, password=hashed_password, ownergender=form.ownergender.data, ownerage=form.ownerage.data, dogname=form.dogname.data, dogbreed=form.dogbreed.data, dogweight=form.dogweight.data, doggender=form.doggender.data, dogage=form.dogage.data, ee1=form.ee1.data, ee1Count=0, ee2=form.ee2.data, ee2Count=0, ee3=form.ee3.data, ee3Count=0)
		db.session.add(new_user)
		db.session.commit()
		return '<h1> New user has been created </h1>'
		# return '<h1>' + form.username.data + ' ' + form.password.data + ' ' + form.email.data + '</h1>'

	return render_template('signup.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard.html', name=current_user.ownername, dogname=current_user.dogname, doggender=current_user.doggender, dogbreed=current_user.dogbreed, ee1=current_user.ee1, ee2=current_user.ee2, ee3=current_user.ee3)


# Post Route
@app.route('/postjson', methods = ['GET', 'POST'])
def postJsonHandler():
     content = request.get_json()
     print(content)

     if request.method == 'POST':
	     val = content['shakeValue']
	     other_val = content['id']

	     events = EventTable.query.all()

	     print(val)
	     print(other_val)
	     if val == 0:
	     	print("not shaking")
	     else:
	     	print("shaking")

	     new_event = EventTable(id=1, user_id=current_user, toy=0, treat=0, praise=int(val))
	     db.session.add(new_event)
	     db.session.commit()
	     return render_template('jsonpost.html',form=form, events=events, val=int(val))

     # EE Form
     form = EEForm()

     return render_template('jsonpost.html',  form=form)


if __name__ == '__main__':
	app.run(debug=True, host='10.194.129.63')
