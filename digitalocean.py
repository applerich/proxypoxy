import urllib3
import json
import certifi
import sys

class Cloud:
    http    = None
    __token__ = None
    def __init__(self, token=None):
        if token == None:
            return None
        self.set_token(token)
        self.http =urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

    def set_token(self, token):
        if token == '':
            print "Hey! token is empty"
        else:
            self.__token__ = token

    def get_token(self):
        return self.__token__

    def list_instances(self):
        auth = "Bearer " + self.get_token()
        url = "https://api.digitalocean.com/v2/droplets"
        headers = { "Content-Type":"application/json", "Authorization": auth}
        http = self.http

        req = http.request('GET', url, headers=headers)
        self.debug(req)

        response= req.read(decode_content=True)
        print response
        data = json.loads( response )
        return data
    
    def debug(self,req):
        print >> sys.stderr, "status", req.status 
        print >> sys.stderr, "ratelimit-remaining:", req.getheader("ratelimit-remaining")
        print >> sys.stderr, "ratelimit-limit:", req.getheader("ratelimit-limit")
        print >> sys.stderr, "ratelimit-reset:", req.getheader("ratelimit-reset")
