import paramiko
import time
import getpass

username = input('Enter your username: ')
password = getpass.getpass()

f = open('myswitches.txt')

for line in f:

	ip_address = line.strip()
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname = ip_address, username = username, password = password)

	print('Successful connection', ip_address)

	remote_connection = ssh_client.invoke_shell()

	remote_connection.send('enable\n')
	remote_connection.send('cisco\n')
	remote_connection.send('terminal length 0\n')
	remote_connection.send('show run\n')
	remote_connection.send('exit\n')

	time.sleep(20)
	readoutput = remote_connection.recv(655350)
	saveoutput = open('backup_switch_' + ip_address,'w')
	saveoutput.write(readoutput.decode('ascii'))
	saveoutput.write('\n')
	print('done')
	saveoutput.close()