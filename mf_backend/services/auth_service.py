""" Auth Service Module. """
from flask import abort, session
from flask import current_app as app
from werkzeug.local import LocalProxy
from werkzeug.security import check_password_hash, generate_password_hash
from ..models import User


def register_new_user(username, password):
	""" Register new user by storing username and hashed password to the db. """
	error = None
	if not username:
		error = 'Username is required.'
	elif not password:
		error = 'Password is required.'
	elif User.query.filter_by(username=username).first() is not None:
		error = f'User {username} is already registered.'

	if error is None:
		user = User(username=username, password=generate_password_hash(password))
		user.save()
		return {'username': username}, 201

	return {'error': error}, 400


def login(username, password):
	error = None
	user = User.query.filter_by(username=username).first()

	if user is None:
		error = 'Incorrect username.'
	elif not check_password_hash(user['password'], password):
		error = 'Incorrect password.'

	if error is None:
		session.clear()
		session['user_id'] = user['id']
		return '', 204

	return {'error': error}
