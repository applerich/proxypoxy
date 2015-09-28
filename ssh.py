## Library to open a ssh connection and make it available as a local socks proxy.

# import paramiko
import subprocess
import shlex
import sys

class Proxy:
    private_key = None
    public_key = None
    port = None
    def __init__(self, private_key, public_key, port=8080):
        self.private_key = private_key
        self.public_key = public_key
        self.port = port

    def connect(self, ip_address, port=8080):
        socks_enabled = " -D "
        hostname = " root@" + ip_address
        params = "ssh" + socks_enabled + str(port) + " -i " + self.private_key + hostname
        args = shlex.split(params)
        print >> sys.stderr, "ssh", params
        subprocess.Popen(args)
        # pk = paramiko.RSAKey.from_private_key_file(self.private_key)
        # client = paramiko.SSHClient()
        # client.load_system_host_keys()
        # client.connect(ip_address, username = "root", pkey = pk)
        # transport = client.get_transport()
        # result = transport.open_channel("direct-tcpip", dest_addr=('0.0.0.0', 0), src_addr=("localhost", port))
        
