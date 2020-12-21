import paramiko
import time

for RTR in [6,7]:
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname = '10.10.10.' + str(RTR), username = 'prashant', password = 'cisco')

	print('successfull connected to 10.10.10.' + str(RTR))

	remote_connection = ssh_client.invoke_shell()

	remote_connection.send('enable\n')
	remote_connection.send('cisco\n')
	remote_connection.send('conf t\n')

	for last in range(1,4):
		remote_connection.send('int loop ' + str(last) + '\n')
		remote_connection.send('ip address 1.1.1.' + str(last) + ' 255.255.255.255' + '\n')
	time.sleep(3)

	remote_connection.send('do term length 0\n')
	remote_connection.send('do sh ip int brief\n')

	remote_connection.send('exit\n')

	time.sleep(3)
	output = remote_connection.recv(65535)
	print(output.decode('ascii'))

	ssh_client.close()