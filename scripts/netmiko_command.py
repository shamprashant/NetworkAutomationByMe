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

		output = net_connect.send_config_from_file(config_file = 'config_switches.txt')

		output = net_connect.send_command('sh ip int brief')
		print(output + '\n\n')

