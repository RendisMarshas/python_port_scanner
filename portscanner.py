import socket #this library allow us to communicate to other machines using tcp and udp protocols 

#This function makes program to go from 1 to selected number of ports
def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)

#This function  tries to detect ports on given IP addresses
def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
        #conneting to our target
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass

#In this section we enter our targets, and nuber of port we want to scan 
targets = input(" Enter Targets To Scan(split them by ,): ")
ports = int(input(" Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print(" Scanning Multiple Targets")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
