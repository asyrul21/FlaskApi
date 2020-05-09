# to mock async request
# from threading import Timer


class ResponseRetriever:
    def __init__(self):
        pass

    def getResponse(self, message):
        return self.getResponseForClass(message)

    def getResponseForClass(self, messageClass):
        if messageClass == 'greeting':
            return 'Hi there!'
        elif messageClass == 'thank':
            return 'My pleasure!'
        # elif
        # elif
        # elif
        # elif
        # elif
        if messageClass == 'notfound':
            return 'I dont know what you are talking about!'
