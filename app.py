# import Flask
from flask import Flask
# Flask restful
from flask_restful import Resource, Api, reqparse


# import resources
from Resources.HelloWorld import HelloWorld
from Resources.Input import Input

# create app instance
app = Flask(__name__)
# restful
api = Api(app)


# add resource to route
api.add_resource(HelloWorld, '/')
api.add_resource(Input, '/input/')


# enable ro disable debugging here
if __name__ == '__main__':
    app.run(debug=True)


##########
# run: python app_restful.py
