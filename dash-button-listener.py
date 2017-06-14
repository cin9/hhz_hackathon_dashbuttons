#Below is our python script. 
# It's a slightly modified version of this code found at: https://blog.thesen.eu/aktuellen-dash-button-oder-ariel-etc-von-amazon-jk29lp-mit-dem-raspberry-pi-nutzen-hacken/
# Many thanks to Stefan from the "Bastel & Reparatur Blog" for sharing his script!

import datetime
import logging
import urllib2
import sys
import os
 
# Constants
timespan_threshhold = 3
 
# Globals
lastpress = datetime.datetime(1970,1,1)
 
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
 
 
def button_pressed_dash1():
  global lastpress
  thistime = datetime.datetime.now()
  timespan = thistime - lastpress
  if timespan.total_seconds() > timespan_threshhold:
    current_time = datetime.datetime.strftime(thistime, '%Y-%m-%d %H:%M:%S')
    print 'Dash button gillette pressed at ' + current_time
    urllib2.urlopen('https://maker.ifttt.com/trigger/poster_gillette/with/key/dxpJRFJ8zacPkgcM0wpjxWfYI6_ENMhjgaUmXH39ZxM')
 
  lastpress = thistime


def button_pressed_dash2():
  global lastpress
  thistime = datetime.datetime.now()
  timespan = thistime - lastpress
  if timespan.total_seconds() > timespan_threshhold:
    current_time = datetime.datetime.strftime(thistime, '%Y-%m-%d %H:%M:%S')
    print 'Dash button brabantia pressed at ' + current_time
    urllib2.urlopen('https://maker.ifttt.com/trigger/poster_brabantia/with/key/dxpJRFJ8zacPkgcM0wpjxWfYI6_ENMhjgaUmXH39ZxM')
 
  lastpress = thistime


def button_pressed_dash3():
  global lastpress
  thistime = datetime.datetime.now()
  timespan = thistime - lastpress
  if timespan.total_seconds() > timespan_threshhold:
    current_time = datetime.datetime.strftime(thistime, '%Y-%m-%d %H:%M:%S')
    print 'Dash button nerf pressed at ' + current_time
    urllib2.urlopen('https://maker.ifttt.com/trigger/toilet_nerf/with/key/dxpJRFJ8zacPkgcM0wpjxWfYI6_ENMhjgaUmXH39ZxM')
 
  lastpress = thistime


def button_pressed_dash4():
  global lastpress
  thistime = datetime.datetime.now()
  timespan = thistime - lastpress
  if timespan.total_seconds() > timespan_threshhold:
    current_time = datetime.datetime.strftime(thistime, '%Y-%m-%d %H:%M:%S')
    print 'Dash button powerpoint pressed at ' + current_time
    print 'Execute shell script to switch picture'
    os.system('sudo sh ./mouseclick.sh')
 
  lastpress = thistime


def udp_filter(pkt):
  if pkt.haslayer(DHCP):
    options = pkt[DHCP].options
    for option in options:
      if isinstance(option, tuple):
        if 'requested_addr' in option:
          # we've found the IP address, which means its the second and final UDP request, so we can trigger our action
          mac_to_action[pkt.src]()
          break
  else: pass
 
mac_to_action = {'ac:63:be:60:28:9e' : button_pressed_dash1, #poster_gillette
                 '50:f5:da:52:cd:06' : button_pressed_dash2, #poster_brarbantia
                 '34:d2:70:d8:4d:37' : button_pressed_dash3, #toilet_nerf
                 '50:f5:da:1d:16:6d' : button_pressed_dash4} #screen_powerpoint
                 
mac_id_list = list(mac_to_action.keys())
 
print "Waiting for a button press..."
sniff(prn=udp_filter, store=0, filter="udp", lfilter=lambda d: d.src in mac_id_list)
 
if __name__ == "__main__":
  main()

# The mouseclick.sh script which is called by the button_pressed_dash4-method contains of only one line of code:
# "xdotool click 1"
# This is used to control an image viewer (we ran feh preview in fullscreen) and loops through images stored in a folder

