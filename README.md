Proxy Poxy
==========

Connects to an instance possible and then opens a tunnel to be used as a proxy; opens port `8080` by default.

Only Digital Ocean and AWS are supported by now, Openstack is planned.

Requirements
------------
poxy uses the following libraries:
  * subprocesses (for SSH, paramiko implementation failed and is commented for now at ssh.py)
  * urllib3 (for the http calls to DO) 
  * certifi (for https calls, for DO)
  * boto3 (for aws usage)
  * json just for fun.


Config file:
------------
The current config file syntax should contain the following fields
```
{
  "aws": 
    {
      "username": ""
    },
  "digitalocean": 
    {
      "username": "",
      "token": ""
    },
  "socks":
    {
      "key": {
        "private": "/path/to/private_key",
        "public": "/path/to/public_key"
      },
      "port": 8080
    }
}
```

TODO:
-----
  * support `start` and `stop` tasks:
    * ``./poxy.py start``: should begin the normal procedure described above and create an instance if required.
    * ``./poxy.py stop``: would be expected to destroy the instance if one was created.

USAGE:
------
  ```
./poxy.py /path/to/config.json
  ``` 
if it's correctly configured it will printout the Digital Ocean json structure and it will try to connect to the first instance available using the given `private_key`

This is an early version, not expect it to work and have a fire extinguisher close to you.
