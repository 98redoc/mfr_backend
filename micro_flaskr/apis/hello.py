""" Hello API Namespace Module. """
from flask_restplus import Resource, Namespace
from flask import request


api = Namespace(name='hello')


@api.route('')
class Hello(Resource):
	def get(self):
		return {"hello": "world"}
