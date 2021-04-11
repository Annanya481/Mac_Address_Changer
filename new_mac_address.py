#!/usr/bin/env python

import subprocess
import optparse
import re

def get_args():
  parser = optparse.OptionParser()
  parser.add_option("-i", "--interface", dest="interface", help="interface to change it's MAC address")
  parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
  (options, arguments) = parser.parse_args()
  if not options.interface:
    parser.error("[-] Please enter an interface whose MAC address is to be changed; use --help for further options")
  elif not options.new_mac:
    parser.error("[-] Please enter a new MAC address; use --help for further options")
  else:
    return options
  
def change_mac(interface, new_mac):
  print("[+] Changing MAC address for " + interface + " to " + new_mac)
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
  subprocess.call(["ifconfig", interface, "up"])

def get_mac(interface):
  ifconfig_result = subprocess.check_output(["ifconfig", interface])
  search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
  if serach_result:
    return search_result.group(0)
  else:
    print("[-] MAC address not found")

options = get_args()
current_mac = get_mac(options.interface)
print("Current MAC:  " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_mac(optons.interface)
if current_mac == options.new_mac:
  print("[-] MAC address was successfully changed to " + current_mac)
else:
  print("[-] MAC address was not changed")
