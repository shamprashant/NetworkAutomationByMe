import paramiko
import time

ip_address = '10.10.10.6'
username = 'prashant'
password = 'cisco'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = ip_address, username = username, password = password)

print('Successful connection ',ip_address)

remote_connection = ssh_client.invoke_shell()

remote_connection.send('enable\n')
remote_connection.send('cisco\n')
remote_connection.send('configure terminal\n')
remote_connection.send('int loop 0\n')
remote_connection.send('ip address 1.1.1.1 255.255.255.255\n')
remote_connection.send('int loop 1\n')
remote_connection.send('ip address 2.2.2.2 255.255.255.255\n')
remote_connection.send('router ospf 1\n')
remote_connection.send('network 0.0.0.0 255.255.255.255 area 0\n')
remote_connection.send('end\n')

remote_connection.send('vlan database\n')

for n in range(2,12):
	print('creating vlan ' + str(n))
	remote_connection.send("vlan " + str(n) + " name Vlan_" + str(n) + "\n")
	time.sleep(0.5)

remote_connection.send('exit\n')
time.sleep(5)
output = remote_connection.recv(65535)
print(output.decode('ascii'))
ssh_client.close()