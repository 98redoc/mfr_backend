""" Auth DTO Module. """
from flask_restplus import Namespace, fields
from flask_restplus import reqparse

class AuthDto:

	def __init__(self, name='auth', description=None, **kwagrs):
		""" Initializer. """
		api = Namespace(name=name, description=description)
		# define models
		# register_post_fields = api.model('RegisterPostModel', {
		# 	'username': fields.String(description='Username', required=True),
		# 	'password': fields.String(description='Password', required=True)
		# })
		# define request parsers
		register_post_parser = reqparse.RequestParser()
		register_post_parser.add_argument('username', required=True, location='form', help='Username')
		register_post_parser.add_argument('password', required=True, location='form', help='Password')
		self.api = api
		# assign to the class object
		self.api = api
		self.register_post_parser = register_post_parser
		for key, val in kwagrs.items(): # add key word args to class attributes
			setattr(self, key, val)
