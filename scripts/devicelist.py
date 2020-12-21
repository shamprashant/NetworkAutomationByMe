import getpass
import sys
import telnetlib

user = input('enter your username: ')
password = getpass.getpass()

f = open('myswitches.txt')

for line in f:
	print('Getting running-config ' + line)
	HOST = line.strip()
	tn = telnetlib.Telnet(HOST)

	tn.read_until(b'Username:')
	tn.write(user.encode('ascii') + b"\n")
	if password:
		tn.read_until(b"Password:")
		tn.write(password.encode('ascii') + b"\n")

	tn.write(b'enable\n')
	tn.write(b'cisco\n')
	tn.write(b'terminal length 0\n')
	tn.write(b'show run\n')
	tn.write(b'exit\n')

	readoutput = tn.read_all().decode('ascii')
	saveoutput = open('switch' + HOST,'w')
	saveoutput.write(readoutput)
	saveoutput.write("\n")
	saveoutput.close()

	print(tn.read_all().decode('ascii'))