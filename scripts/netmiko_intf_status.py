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

		output = net_connect.send_command('sh ip int brief')
		
		name = output[1]['intf']
		status = output[1]['status']
		print('\n Interface ' + name + ' status is ' + status)

