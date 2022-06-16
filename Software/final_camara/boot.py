from network import WLAN, STA_IF
from time import sleep_ms

#     SSID="HUAWEI-B315-FC04"
#     PASS="8TB448HF5A7"
# SSID="TP-Link_16F6"
# PASS="10142004"
#     SSID="MEO-B60A37"
#     PASS="A562D35D2C"
SSID="MSI_20"
PASS="9a;900J5"

interface=WLAN(STA_IF)
interface.active(True) #para ativar
interface.connect(SSID, PASS)

max_secs=40
print ("Connecting: ", end="")
while not interface.isconnected() and max_secs>0:
    print(".",end="")
    sleep_ms(1000)
    max_secs-=1
    
if max_secs==0:
    print("\nCouldn't connect to network!!!")
else:
    print("\Connection to the wireless network successful!")
    ip_addr, mask, gateway, dns_srv = interface.ifconfig()
    print("IP address: ", ip_addr)
    print("Network mask: ", mask)
    print("Gateway: ", gateway)
    print("DNS server: ", dns_srv)
