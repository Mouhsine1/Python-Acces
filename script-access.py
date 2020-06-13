from netmiko import ConnectHandler

acc1 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.131', 'username': 'mouhsine', 'password':'axians'}
acc2 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.132', 'username': 'mouhsine', 'password':'axians'}
acc3 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.133', 'username': 'mouhsine', 'password':'axians'}
acc4 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.134', 'username': 'mouhsine', 'password':'axians'}
acc5 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.135', 'username': 'mouhsine', 'password':'axians'}
acc6 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.136', 'username': 'mouhsine', 'password':'axians'}
acc7 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.137', 'username': 'mouhsine', 'password':'axians'}
acc8 = { 'device_type': 'cisco_ios', 'ip':'192.168.1.138', 'username': 'mouhsine', 'password':'axians'}

with open('access1') as s1:
	lines = s1.read().splitlines()
print(lines)
net_connect= ConnectHandler(**acc1)
output = net_connect.send_config_set(lines)
print(output)
with open('access2') as s2:
	lines = s2.read().splitlines()
print(lines)
net_connect= ConnectHandler(**acc2)
output = net_connect.send_config_set(lines)
print(output)
with open('access3') as s3:
	lines = s3.read().splitlines()
print(lines)
net_connect= ConnectHandler(**acc3)
output = net_connect.send_config_set(lines)
print(output)
with open('access4') as s4:
	lines = s4.read().splitlines()
print(lines)
net_connect= ConnectHandler(**acc4)
output = net_connect.send_config_set(lines)
print(output)
with open('access5') as s5:
	lines = s5.read().splitlines()
print(lines)
net_connect= ConnectHandler(**acc5 )
output = net_connect.send_config_set(lines)
print(output)
with open('access6') as s6:
	lines = s6.read().splitlines()
print(lines)
net_connect= ConnectHandler(**acc6 )
output = net_connect.send_config_set(lines)
print(output)
with open('access7') as s7:
	lines = s7.read().splitlines()
print(lines)
net_connect= ConnectHandler(**acc7)
output = net_connect.send_config_set(lines)
print(output)
with open('access8') as s8:
	lines = s5.read().splitlines()
print(lines)
net_connect= ConnectHandler(**acc8)
output = net_connect.send_config_set(lines)
print(output)