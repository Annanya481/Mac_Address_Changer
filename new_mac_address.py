#!/usr/bin/env python

import subprocess
import optparse

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
  
def change(interface, new_mac):
  print("[+] Changing MAC address for " + interface + " to " + new_mac)
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
  subprocess.call(["ifconfig", interface, "up"])
  
options = get_args()
change(options.interface, options.new_mac)
     
