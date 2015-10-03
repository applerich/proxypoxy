#!/usr/bin/python

import json
import sys
from pprint import pprint
import digitalocean  
import ssh

def load_config(configfile):
    # Loads the given cloud config provided and will return an object for the configured cloud
    if configfile =="":
        print "Error: Configuration file not provided"
        sys.exit(1)
    
    __cloud = None
    with open(configfile) as data_file:    
        data = json.load(data_file)
    
    return data

data = load_config(sys.argv[1])

if data["digitalocean"]["token"] != "":
    cloud = digitalocean.Cloud(data["digitalocean"]["token"])

proxy = ssh.Proxy(data["socks"]["key"]["private"], data["socks"]["port"])


if cloud == None:
    print "Error Initializing Cloud"
    sys.exit(1)


instances = cloud.list_instances()
instance = instances["droplets"][0]

ip_address = None
for network_4 in instance["networks"]["v4"]:
    if network_4["type"] == "public":
        ip_address = network_4["ip_address"]
        print >> sys.stderr, network_4["ip_address"]

proxy.connect(data["socks"]["username"], ip_address, data["socks"]["port"]) 
proxy.just_wait()

#  
#  for instance in instances["droplets"]:
#      print >> sys.stderr, instance["name"]
#      for network_4 in instance["networks"]["v4"]:
#          if network_4["type"] == "public":
#              print >> sys.stderr, network_4["ip_address"]
#      for network_6 in instance["networks"]["v6"]:
#          if network_6["type"] == "public":
#              print >> sys.stderr, network_6["ip_address"]
#  
