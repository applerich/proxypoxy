import urllib2

class Cloud:
    __token__ = None
    def set_token(self, token):
        if token == '':
            print "Hey! token is empty"
        else:
            print "token loaded"
        self.__token__ = token

    def get_token(self):
        return self.__token__

    def list_instances():
        urllib2.

