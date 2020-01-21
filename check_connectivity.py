#!/usr/bin/python3

from netmiko import ConnectHandler
import json
from prettytable import PrettyTable 

with open("NSOT_OoB.json") as fo:
	oob = json.load(fo)

with open("NSOT_inband.json") as  fi:
	inband = json.load(fi)

rw = ["Devices"] 
net_stat = {}
for device in oob.keys():
        rw.append(device)
        ping_stat = [] 
        ping_stat.append(device)
        net_connect = ConnectHandler(**oob[device])
        print("Trying to SSH into the Device " + device)
        print("Initiating Ping Sequence for device " + device) 
        for i in inband.keys():
            pi = 1 
            for j in inband[i]: 
                dev  = inband[i][j]['ip']
                print("Trying to ping " + dev)
                res = net_connect.send_command("ping " + dev + " repeat 3")
                if('round-trip' in res):
                    res = 1 
                else: 
                     res = 0
                pi = int(pi and res)
                print(pi)
            ping_stat.append(pi)    
            
        net_stat.update({device : ping_stat})
        print(net_stat)
    
        print("Disconnecting from device " + device)
        net_connect.disconnect()

table = PrettyTable(rw)
for k in net_stat.keys():
      table.add_row(net_stat[k])

print("Connectivity Check Done")
print("Status Generated")
print(table)
