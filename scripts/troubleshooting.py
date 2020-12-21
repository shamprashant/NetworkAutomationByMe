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

	print('collecting Troubleshooting log file of ', ip_address)

	remote_connection.send('enable\n')
	remote_connection.send('cisco\n')
	remote_connection.send('terminal length 0\n')
	remote_connection.send('show ip int brief\n')
	remote_connection.send('show ip bgp summ\n')
	remote_connection.send('show ip route ospf\n')
	remote_connection.send('show ip route\n')
	remote_connection.send('show log\n')
	remote_connection.send('exit\n')

	time.sleep(20)
	readoutput = remote_connection.recv(655350)
	saveoutput = open('log_file_of_' + ip_address,'w')

	print('saving log file in log file of ' + ip_address + '\n')

	saveoutput.write(readoutput.decode('ascii'))
	saveoutput.write('\n')
	print('done')

	saveoutput.close()
	ssh_client.close()
