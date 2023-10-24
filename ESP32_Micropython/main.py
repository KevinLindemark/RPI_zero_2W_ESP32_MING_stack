# Complete project details at https://RandomNerdTutorials.com

def sub_cb(topic, msg):
  print((topic, msg))
  if msg == b'on':
    led.value(1)
  elif msg == b'off':
    led.value(0)

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

last_sensor_reading = 0
readings_interval = 3

while True:
  try:
    client.check_msg()
    if (time.time() - last_sensor_reading) > readings_interval:
      msg = str(lmt84.celcius_temperature()) # needs string to send to MQTT broker
      print(f"Publishing temperature: {msg}")
      client.publish(topic_pub, msg)
      last_sensor_reading = time.time()
  except OSError as e:
    restart_and_reconnect()
