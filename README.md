# RPI_zero_2W_ESP32_MING_stack

lav en bruger her:
https://dashboard.balena-cloud.com

Lav fleet på balenaCloud (create new fleet) og vælg raspberry pi Zero w2 og hak wifi og ethernet af under network connection og indtast SSID og PASSWORD og tryk Flash knappen og så download balena etcher for at flashe Balena OS til Raspberry Pi (Zero W 2)

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/3485a493-8db2-45b1-b8e8-17de7c2082d5)

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/172a2e06-838b-41d8-8e98-49ca4259c8f5)


Gå til github linket og tryk deploy with balena knap og vælg eksisterende fleet på balenaCloud dashboard:
https://github.com/mpous/ming 
 

 ![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/4f46079d-a3da-429b-b470-0d8beba01630)

 ![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/0ae39376-01d7-4ff4-951f-1b53176e427e)


Derefter opdateres raspberry pi til at anvende ming stacken. på balenacloud kan man se de lokale IP adresser til de forskelige docker tjenester der køres og tilgå dem ved at angive adressen i en browsers URL felt.
både brugernavn og password til tjenesterne er **balena**

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/8529915f-0373-4f63-a520-8a7cc18b31af)

Mosquitto MQTT broker lytter på port 1883 for MQtt besked publicationer.

InfluxDB lytter på port 8086 og giver en time series database til sensor data opbevaring.

NodeRed lytter på port 80 og anvendes med en nem grafisk interface til at parse, analysere, opbevare og viderestille sensor data beskeder.

Grafana lytter på port 8080 og tilbyder et datavisualiseringsmiljø til sensor data.

WiFi Connect lytter på port 80 i tilfælde af at der ikke er WiFi connectivity tilgængelig.

Når der bruges influxdb i en docker container:
Hvis node-red og influxdb containers er på samme maskine kan man ikke tilgå dem genne localhost (fordi hosten af contianeren ikke kører influxdb selv). Man skal derimod tilgå den genmmen en reference til selve containerens navn.
Eksempel: **influxdb:8086** i stedet for **localhost:8086**
