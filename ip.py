#!/usr/bin/python3
import optparse, os
try:
 import urllib.request as ul
 import ip_address, json
except ImportError:
 #print('Grant Us Root To Auto Install Required Modules!.')
 os.system('pip3 install ip_address')
 os.system(f'python3 {os.path.basename(__file__)}')
 exit(0)
parser = optparse.OptionParser()
parser.add_option('-t','--target',dest='ip',help='target ip')
(value, key) = parser.parse_args()
ipx = value.ip

class Tracer:
 def __init__(self, ip):
  self.ip = ip
		

 def trace(self):
  conv = ul.urlopen(f"http://ip-api.com/json/{self.ip}")
  read = conv.read()
  load = json.loads(read)
  print("")
  print(f"IP: {load['query']}")
  print(f"Country: {load['country']}")
  print(f"country code: {load['countryCode']}")
  print(f"region: {load['region']}")
  print(f"Region Name: {load['regionName']}")
  print(f"City: {load['city']}")
  print(f"zip code: {load['zip']}")
  print(f"time zone: {load['timezone']}")
  print(f"ISP: {load['isp']}")
  print(f"org: {load['org']}")
  print(f"as: {load['as']}")
  print(f"latitude: {load['lat']}")
  print(f"longitude: {load['lon']}")


 def banner(self):
  print(f"""
=========================
 __  _______             |
 \\ \\/ /_   _|            |
  >  <  | |              |
 /_/\\_\\ |_|              |
                         |
X-Tracer By: Anikin Luke |
-------------------------|
Your Ip: {ip_address.get()}   |
=========================
result:""")


 def check(self):
  if self.ip is None:
   self.ip = input("\nip to trace: ")
   ip_trace.banner()
   ip_trace.trace()
  else:
   ip_trace.banner()
   ip_trace.trace()


if __name__=='__main__':
 ip_trace = Tracer(ipx)
 ip_trace.check()
