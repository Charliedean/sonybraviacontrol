from wakeonlan import wol
import subprocess
import re
import time
import os

tv_send = """curl --silent -XPOST http://%s/sony/IRCC -d '<?xml version="1.0"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:X_SendIRCC xmlns:u="urn:schemas-sony-com:service:IRCC:1"><IRCCCode>%s</IRCCCode></u:X_SendIRCC></s:Body></s:Envelope>' -H 'Content-Type: text/xml; charset=UTF-8' -H 'SOAPACTION: "urn:schemas-sony-com:service:IRCC:1#X_SendIRCC"' -O /dev/null"""

#TV Codes - Might need to be changed if doesn't work
tv_input = "AAAAAQAAAAEAAAAlAw=="
tv_down = "AAAAAQAAAAEAAAB1Aw=="
tv_confirm = "AAAAAQAAAAEAAABlAw=="
# Change with your TV Mac address
tv_mac = '00:00:00:00:00:00'
# Change with desired HDMI number
# Zero doesn't change HDMI
desired_HDMI_num = 0

arpscan = subprocess.check_output(['arp', '-a'])

for arp in arpscan.split('\n'):
	if re.search(tv_mac.lower(),arp):
		tv_ip = arp.split()[1].strip('()')
		break
if tv_ip:
	print "TV IP address: " + tv_ip
else:
	print "TV not found, Make sure MAC address is correct and TV is connected and this device can see it"
	exit()

print "Turning on TV"
wol.send_magic_packet(tv_mac)
print "Sleeping while TV turns on..."
time.sleep(2)

print "Changing TV input to HDMI ", desired_HDMI_num

os.system(tv_send%(tv_ip,tv_input))
time.sleep(0.3)

if desired_HDMI_num < 0:
	for num in xrange(desired_HDMI_num):
		os.system(tv_send%(tv_ip,tv_down))
		time.sleep(0.1)

os.system(tv_send%(tv_ip,tv_confirm))

