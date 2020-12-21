from netmiko import ConnectHandler
from datetime import datetime
from threading import Thread
startTime = datetime.now()

threads = []
def checkparallel(ip):
	device = ConnectHandler(device_type='cisco_ios', ip=ip, username='prashant', password='cisco')
	output = device.send_command("show run | in hostname")
	output=output.split(" ")
	hostname=output[1]
	print ("\nHostname for IP %s is %s" % (ip,hostname))

for n in range(11, 14):
	ip="10.10.10.{0}".format(n)
	t = Thread(target=checkparallel, args= (ip,))
	t.start()
	threads.append(t)

#wait for all threads to completed
for t in threads:
	t.join()

print ("\nTotal execution time:")
print(datetime.now() - startTime)
