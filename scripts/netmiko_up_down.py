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

		name = output[1]['intf']
		status = output[1]['status']
		print ('\nInterface ' + name + ' status is ' + status )

		if status == 'up':
		    print ('Finishing the script')
		else :
		    print ('making backup interface UP')
		    config_commands = [ 'int fa0/1',
		                        'no shut' ]
		    output = net_connect.send_config_set(config_commands)
		    print (output)
		    print ('Finished configuration')