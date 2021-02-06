from wakeonlan import send_magic_packet
from getmac import get_mac_address
import time
ipp="192.168.1.100"
ip_mac = get_mac_address(ip=ipp)
def slp(s):
    time.sleep(s)
print("Trying to wake up...")
slp(1)
try:
    send_magic_packet("4c:cc:6a:00:77:37", ip_address="192.168.1.100", port=9)
except TypeError:
    print("Not founded object by ip "+ipp)
else:
    print("Successful!")
