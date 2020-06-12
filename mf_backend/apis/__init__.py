from flask_restplus import Api
from .hello import api as ns_hello
from .auth import api as ns_auth


api = Api(prefix='/api', doc='/api/docs')
api.add_namespace(ns_hello)
api.add_namespace(ns_auth)
