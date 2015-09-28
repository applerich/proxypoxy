Proxy Poxy
==========

Creates the smallest instance possible and then opens a tunnel to be used as a proxy; opens port `8080` by default.

Only Digital Ocean is supported by now, Openstack and AWS are planned.

Requirements
------------
poxy uses the following libraries:
  * subprocesses (for SSH, paramiko implementation failed and is commented for now at ssh.py)
  * urllib3 (for the http calls to DO)
  * certifi (for https calls)
  * json just for fun.

Config file:
------------
The current config file syntax should contain the following fields
```
{
  "digitalocean": 
    {
      "token": ""
    },
  "socks":
    {
      "key": {
        "private": "/path/to/private_key",
        "public": "/path/to/public_key"
      },
      "port": 
    }
}
```

TODO:
-----
  * support `start` and `stop` tasks:
    * ``./poxy.py start``: should begin the normal procedure described above.
    * ``./poxy.py stop``: would be expected to destroy the instance.
