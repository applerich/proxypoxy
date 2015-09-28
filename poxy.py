#!/usr/bin/python

import urllib2
import json
import sys
from pprint import pprint
import digitalocean  

def load_config(configfile):
    # Loads the given cloud config provided and will return an object for the configured cloud
    if configfile =="":
        print "Error: Configuration file not provided"
        sys.exit(1)
    
    with open(configfile) as data_file:    
        data = json.load(data_file)
    
    if data["digitalocean"]["token"] != "":
        print "using Digital Ocean"

    __cloud = digitalocean.Cloud()
    __cloud.set_token( data["digitalocean"]["token"])
    return __cloud

cloud = load_config(sys.argv[1])


