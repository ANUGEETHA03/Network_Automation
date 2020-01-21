#This Code explains how Netmiko Tool can we used to Remotely configure and 
#Acess a Cisco Router 
#This code has high chance of Re-Use 



import netmiko
from netmiko import ConnectHandler

R1 = {
        'device_type' : 'cisco_ios',
        'host':'192.168.1.1',
        'username':'vava',
        'password':'vava@123'
     }

R2 = {
        'device_type' : 'cisco_ios',
        'host':'192.168.1.2',
        'username':'vava',
        'password':'vava@123'
     }

print("Trying to SSH into R1") 
net_connect = ConnectHandler(**R1)
print("Trying to SSH into R2") 
net_connect2 = ConnectHandler(**R2)

try:
  print("Yay SSH-ed into R1 and R2")
  print("Display the IP interface brief for the routers")
  print("R1 Status")
  R1_output = net_connect.send_command("show ip int brief")
  print(R1_output)
  print("R2 Status")
  R2_output = net_connect2.send_command("show ip int brief")
  print(R2_output)

  print("Change the hostname of R1 and R2")
  print("R1 Status")
  net_connect.send_config_set("hostname R1_Vava")
  print("R2 Status")
  net_connect2.send_config_set("hostname R2_Vava")
  print("hostnames have been changed")
except Exception as e: 
    print("Some Exception was thrown") 
    print(e)

print("Disconnecting from R1")
net_connect.disconnect()
print("Disconnecting from R2")
net_connect2.disconnect()
