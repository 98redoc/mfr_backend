""" Authentication Namespace Module. """
import functools
from flask import request
from flask import current_app as app
from flask_restplus import Namespace, Resource
from werkzeug.security import check_password_hash, generate_password_hash
from ..services.auth_service import register_new_user, login
from ..utils.auth_dto import AuthDto


auth_dto = AuthDto(name='auth', description='Authentication API Namespace.')
api = auth_dto.api
#register_post_fields = auth_dto.register_post_fields


@api.route('/register')
class Register(Resource):

	@api.expect(auth_dto.register_post_parser)
	def post(self):
		args = auth_dto.register_post_parser.parse_args()
		return register_new_user(username=args['username'], password=args['password'])


@api.route('/login')
class Login(Resource):
	@api.expect(auth_dto.register_post_parser)
	def post(self):
		args = auth_dto.register_post_parser.parse_args()
		return login(username==args['username'], password=args['password'])