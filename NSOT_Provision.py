#A Network Source of Truth File Describes the configurations of every Network Device, (for example its IPs and Subnet Mask, and how they are connected to other Network Devices"
#Out Network Design Team as already defined and created a NSOT file and saved it as NSOT_inband.json 
#We can assign that json into a dictionary using json.load() function 

import json 
from netmiko import ConnectHandler

with open("NSOT_OoB.json") as fo: 
    oob = json.load(fo)

with open("NSOT_inband.json") as fi: 
    inband = json.load(fi)

print("Inband Network") 
print(inband)


print("OoB Network") 
print(oob)

for device in oob.keys():
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
    
    print("Configure Hostname")
    host = "hostname " + device + "_Vava"
    print(host)
    net_connect.send_config_set(host)
    ip_status = net_connect.send_command("show ip interface brief")
    print(ip_status)
    print("Exiting Out of the Device")
    net_connect.disconnect()
