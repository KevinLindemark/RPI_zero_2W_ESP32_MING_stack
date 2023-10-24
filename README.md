# RPI_zero_2W_ESP32_MING_stack


Lav fleet på balenaCloud (create new fleet) og vælg raspberry pi Zero w2 og hak wifi og ethernet af under network connection og indtast SSID og PASSWORD og tryk Flash knappen og så download balena etcher for at flashe Balena OS til Raspberry Pi (Zero W 2)

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/3485a493-8db2-45b1-b8e8-17de7c2082d5)

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/172a2e06-838b-41d8-8e98-49ca4259c8f5)


Gå til github linket og tryk deploy with balena knap og vælg eksisterende fleet på balenaCloud dashboard:
https://github.com/mpous/ming 
 

 ![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/4f46079d-a3da-429b-b470-0d8beba01630)

 ![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/0ae39376-01d7-4ff4-951f-1b53176e427e)


Derefter opdateres rpi zero til at anvende ming stacken


when using influxdb on a docker container:
If your node-red and influxdb containers are in the same machine, you can't reference it using localhost (because the host of the container is not running an influxdb itself). You need to reference it using the name of the container.
Example: influxdb:8086 instead of localhost:8086.
