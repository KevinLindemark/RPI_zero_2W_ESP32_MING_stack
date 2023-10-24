# Complete project details at https://RandomNerdTutorials.com

import time
from umqtt_simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
from lmt84_class import LMT84
esp.osdebug(None)
import gc
gc.collect()
# fill with own credentials
ssid = ''
password = ''
mqtt_server = ''
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'output'
topic_pub = b'temp'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())


lmt84 = LMT84()
led = machine.Pin(26, machine.Pin.OUT, value=0)