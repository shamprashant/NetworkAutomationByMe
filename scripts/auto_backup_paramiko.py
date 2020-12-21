import paramiko
import time
import schedule

def backup():
    with open('myswitches.txt','r') as file:
        for line in file:
            try:
                IP = line.strip()
                ssh_client = paramiko.SSHClient()
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh_client.connect(hostname = IP, username = 'prashant', password = 'cisco')

                print('connected with ', IP)

                remote_connection = ssh_client.invoke_shell()

                remote_connection.send('enable\n')
                remote_connection.send('cisco\n')
                remote_connection.send('term length 0\n')
                remote_connection.send('show run\n')
                remote_connection.send('exit\n')
                time.sleep(3)

                output = remote_connection.recv(65535)
                print(output.decode('ascii'))

                output_file = open('auto','w')
                output_file.write(output.decode('ascii'))
            except Exception as e:
                print(e)
                print('----------' + IP + '-------------')


schedule.every().minute.at(":00").do(backup)
while(True):
    schedule.run_pending()
    time.sleep(1)