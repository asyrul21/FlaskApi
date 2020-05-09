# $ export FLASK_ENV=development
# $ flask run

# This does the following things:

# it activates the debugger
# it activates the automatic reloader
# it enables the debug mode on the Flask application.

# import Flask
from flask import Flask, render_template, request
from markupsafe import escape
# Flask restful
# from flask_restful import Resource, Api

# import method classes
from inputProcessors.ResponseRetriever import ResponseRetriever
from inputProcessors.Classifiers import classifyInput

# create app instance
app = Flask(__name__)

#  add route
@app.route('/')
def hello_world():
    return render_template('index.html', title='Welcome to the flask API')


@app.route('/input/', methods=['GET', 'POST'])
def input():
    if(request.method == 'GET'):
        # get input
        message = request.args.get('message', '')

        # escape input message
        escapedMessage = escape(message)

        # classify input
        messageClass = classifyInput(message)

        # get reponse
        rr = ResponseRetriever()
        res = rr.getResponse(messageClass)

        # return response as json
        return {
            "source:": "bot",
            "input": message,
            "response": res
        }
    else:
        return 'You just made a POST request!'


# page 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


##########
# rr = ResponseRetriever()
# print(rr.getResponse('hello'))
