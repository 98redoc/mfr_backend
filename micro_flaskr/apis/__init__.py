from flask_restplus import Api
from .hello import api as ns_hello


api = Api(prefix='/api', doc='/api/docs')
api.add_namespace(ns_hello)
