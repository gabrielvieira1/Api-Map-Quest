import tabulate
import ncclient
from netmiko import ConnectHandler
import pyang
import xmltodict
import requests

sshCli = ConnectHandler(
        device_type='cisco_ios',
        host='192.168.56.101',
        port=22,
        username='cisco',
        password='cisco123!'
        )

config_commands = [
     'int loopback 1',
     'ip address 2.2.2.2 255.255.255.0',
     'description WHATEVER'
 ]

output = sshCli.send_config_set(config_commands)
print("show config commands:\n{}\n".format(output))


output = sshCli.send_command("show ip int brief")
print("show ip int brief:\n{}\n".format(output))

##api_url "https://192.168.56.101/restconf/date/ietf-interfaces:interfaces"