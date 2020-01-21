#A Network Source of Truth File Describes the configurations of every Network Device, (for example its IPs and Subnet Mask, and how they are connected to other Network Devices"
#Out Network Design Team as already defined and created a NSOT file and saved it as NSOT_inband.json 
#We can assign that json into a dictionary using json.load() function 

import re
import json 
from netmiko import ConnectHandler

#To Read the OoB json file  
with open("NSOT_OoB.json") as fo: 
    oob = json.load(fo)

#To Read the in_band json file  
with open("NSOT_inband.json") as fi: 
    inband = json.load(fi)

print("Inband Network") 
print(inband)


print("OoB Network") 
print(oob)

net = {} 
for device in oob.keys():
    ip = []
    print("Entered Loop, looking for Device") 
    print("Trying to SSH into: ")
    print(device)
    net_connect = ConnectHandler(**oob[device])
    for interface in inband[device]:
        inter = "interface " + interface
        des = "description " + device + " " + interface
        ip_add = "ip address " + inband[device][interface]['ip'] + " " + inband[device][interface]['mask']
        print(ip_add)
        net_connect.send_config_set([inter,des,ip_add,"no shutdown"])
        print("Interface " + interface + " of device " + device + " is configured with " + inband[device][interface]['ip'])
        ip_address_list = re.findall(r"\d+\.\d+\.\d+\.\d+",ip_add)
        ip.append(ip_address_list[0])
        print(ip)
    net.update({device : ip})
    print("Configure Hostname")
    host = "hostname " + device + "_Vava"
    print(host)
    net_connect.send_config_set(host)
    for i in net[device]:
             net_connect.send_config_set(["router ospf 100","network " + i + " 0.0.0.255 " + "area 0"])
             print("network " + i + " 0.0.0.255 " + "area 0")
    ip_status = net_connect.send_command("show ip interface brief")
    print(ip_status)
    print("The Network for Device >>")
    print(net)
    print("Exiting Out of the Device")
    net_connect.disconnect()
