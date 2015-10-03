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
      "username": "",
      "port": 8080
    }
}
```

TODO:
-----
  * support `start` and `stop` tasks:
    * ``./poxy.py start``: should begin the normal procedure described above.
    * ``./poxy.py stop``: would be expected to destroy the instance.

USAGE:
------
  ```
./poxy.py /path/to/config.json 2> debug 
  ``` 
if it's correctly configured it will printout the Digital Ocean json structure and it will try to connect to the first instance available using the given `private_key`

This is an early version, not expect it to work and have a fire extinguisher close to you.
