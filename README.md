Proxy Poxy
==========

Creates the smallest instance possible and then opens a tunnel to be used as a proxy; opens port `8080` by default.

Only Digital Ocean is supported by now, Openstack and AWS are planned.

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
      "public_key": "",
      "port": 
    }
}
```

TODO:
-----
  * support `start` and `stop` tasks:
    * ``./poxy.py start``: should begin the normal procedure described above.
    * ``./poxy.py stop``: would be expected to destroy the instance.
