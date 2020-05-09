from flask_restful import Resource
# doesnt work because its Flask Restful is only for APIs
from flask import render_template


class HelloWorld(Resource):
    # restful automatically maps method name to request type
    def get(self):
        return {
            'message': 'Hello World!'
        }

    def post(self):
        return {
            'message': 'You have made a POST request!'
        }
