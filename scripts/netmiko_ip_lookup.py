from netmiko import ConnectHandler

ip = input('Enter the IP: ')
RTR_10 = {
    'ip':   '10.10.10.6',
    'username': 'prashant',
    'password': 'cisco',
    'device_type': 'cisco_ios',
}
print ('Connecting to the device..')
net_connect = ConnectHandler(**RTR_10)

output = net_connect.send_command('show ip int brie', use_textfsm=True)

print ('\nSearch result \n')



ipsearch =[i['intf'] for i in output if i['ipaddr'] == ip]
for ipoutput in ipsearch:
    print ('IP Address ' + ip + ' belongs to interface ' + ipoutput )
print ('IP Address ' + ip + ' belongs to interface ' + str(ipsearch) )