import paramiko
import time
import getpass

username = input('Enter the username: ')
password = getpass.getpass()

f = open('myswitches.txt')

for line in f:
	try:
		ip_address = line.strip()
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.connect(hostname = ip_address, username = username, password = password)

		remote_connection = ssh_client.invoke_shell()

		remote_connection.send('enable')
		remote_connection.send('cisco')
		remote_connection.send('exit\n')
	except:
		remote_connection = ('socket.error')

	result = remote_connection

	if result == 'socket.error':
		print(ip_address, 'Not Accessible')
	else:
		print(ip_address, 'Accessible')

print('connectivity check done')