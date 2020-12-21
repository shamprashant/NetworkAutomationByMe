from netmiko import ConnectHandler
import time

with open('myswitches.txt') as file:
	for line in file:
		IP = line.strip()

		device = {
			'device_type': 'cisco_ios',
			'ip': IP,
			'username': 'prashant',
			'password': 'cisco',
		}

		net_connect = ConnectHandler(**device)
		
		print('connected with ',IP)

		with open('config_switches.txt') as configurations:
			commands = [command.strip() for command in configurations]
			
			net_connect.send_config_set(commands)

		output = net_connect.send_command('sh ip int brief',use_textfsm = True)
		
		l = len(output)
		
		print ('\nList of interfaces which are UP \n')
		for i in range(0,l):
		    if output[i]['status'] == 'up':
		        print (output[i]['intf'] +' ' + output[i]['status'])

		print ('\nList of interfaces which are DOWN \n')
		for i in range(0,l):
		    if output[i]['status'] != 'up':
		        print (output[i]['intf'] +' ' + output[i]['status'])

