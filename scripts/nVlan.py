import getpass
import sys
import telnetlib

HOST = input('Enter your device IP: ')
n = int(input('Enter the number of vlan you want to create'))
user = input('Enter your telnet username: ')
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b'Username:')
tn.write(user.encode('ascii') + b"\n")
if password:
	tn.read_until(b"Password:")
	tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b'vlan database\n')

for i in range(i,n):
	tn.write(("vlan " + str(i+1) + " name Python_VLAN_" + str(i+1) + "\n").encode('ascii'))

tn.write(b"exit\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))