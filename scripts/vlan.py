import getpass
import sys
import telnetlib

HOST = input("Enter Device IP: ")
user = input("Enter your telnet username:")
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
tn.write(b'vlan 2 name Python_VLAN_5\n')
tn.write(b'vlan 3 name Python_VLAN_6\n')
tn.write(b'vlan 4 name Python_VLAN_7\n')
tn.write(b"exit\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))