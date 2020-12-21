from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

IP_LIST = open('myswitches.txt')
for IP in IP_LIST:
    print ('\n'+ IP.strip() + '  \n' )
    RTR = {
    'ip':   IP,
    'username': 'prashant',
    'password': 'cisco',
    'device_type': 'cisco_ios',
    }

    try:
        net_connect = ConnectHandler(**RTR)
    except NetMikoTimeoutException:
        print ('Device not reachable.')
        continue
    except AuthenticationException:
        print ('Authentication Failure.')
        continue
    except SSHException:
        print ('Make sure SSH is enabled in device.')
        continue

    output = net_connect.send_config_from_file(config_file = 'config_switches.txt')
    print(output)

    output = net_connect.send_command('show ip int brief')
    print(output)