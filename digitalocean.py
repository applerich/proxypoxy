import urllib3
import json
import certifi
import sys

class Cloud:
    http    = None
    username = None
    __token__ = None
    def __init__(self, token=None, username=None):
        if token == None:
            return None
        self.set_token(token)
        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        self.username = username

    def set_token(self, token):
        if token == '':
            print "Hey! token is empty"
        else:
            self.__token__ = token

    def get_token(self):
        return self.__token__
    
    def getPublicAddress(self):
        """
        Returns the public ip address from the first instance found
        """
        instances = self.list_instances()
        instance = instances["droplets"][0]
        
        ip_address = None
        for network_4 in instance["networks"]["v4"]:
            if network_4["type"] == "public":
                ip_address = network_4["ip_address"]
                break
        return ip_address
        
        return ip_address

    def list_instances(self):
        """
        Returns the list of instances currently available
        """
        auth = "Bearer " + self.get_token()
        url = "https://api.digitalocean.com/v2/droplets"
        headers = { "Content-Type":"application/json", "Authorization": auth}
        http = self.http

        req = http.request('GET', url, headers=headers)
        self.debug(req)

        response= req.read(decode_content=True)
        data = json.loads( response )
        return data
    
    def debug(self,req):
        print >> sys.stderr, "status", req.status 
        print >> sys.stderr, "ratelimit-remaining:", req.getheader("ratelimit-remaining")
        print >> sys.stderr, "ratelimit-limit:", req.getheader("ratelimit-limit")
        print >> sys.stderr, "ratelimit-reset:", req.getheader("ratelimit-reset")
