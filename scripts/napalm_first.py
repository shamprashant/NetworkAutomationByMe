from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('10.10.10.6', 'prashant', 'cisco')
device.open()

device.load_merge_candidate(filename='29_cisco_route')
print (device.compare_config())