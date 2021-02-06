import wakeonlan
from getmac import get_mac_address
ip_mac = get_mac_address(ip="192.168.1.100")
print(ip_mac)
wakeonlan.create_magic_packet(ip_mac)
