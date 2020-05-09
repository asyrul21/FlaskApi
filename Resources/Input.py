from flask_restful import Resource, reqparse
# for data formatting
from flask_restful import fields, marshal_with
from markupsafe import escape

# import method classes
from inputProcessors.ResponseRetriever import ResponseRetriever
from inputProcessors.Classifiers import classifyInput

# define arguments parser
# reqparse is Resource specific
# i.e. args defined in here does not work in other Resources
parser = reqparse.RequestParser()
parser.add_argument('message', type=str,
                    help='The input string sent by the user')

# define data format
# may be optional
resource_fields = {
    'source': fields.String,
    'input': fields.String,
    'response': fields.String,
}


class Input(Resource):
    @marshal_with(resource_fields)
    def get(self):
        # get input
        message = parser.parse_args()['message']

        # escape input message
        escapedMessage = escape(message)

        # classify input
        messageClass = classifyInput(message)

        # get reponse
        rr = ResponseRetriever()
        res = rr.getResponse(messageClass)

        # return response as json
        return {
            "source": 'bot',
            "input": escapedMessage,
            "response": res,
        }
