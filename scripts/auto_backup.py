from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import time
import datetime
import schedule

def job():

    TNOW = datetime.datetime.now().replace(microsecond=0)
    IP_LIST = open('myswitches.txt')
    for IP in IP_LIST:
        print ('\n  '+ IP.strip() + '  \n' )
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

        print ('Initiating cofig backup at ' + str(TNOW))
        output = net_connect.send_command('show run')

        SAVE_FILE = open('auto', 'w')
        SAVE_FILE.write(output)
        SAVE_FILE.close()
        print ('Finished config backup')
schedule.every().minute.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)