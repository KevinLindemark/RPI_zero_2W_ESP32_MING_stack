## OBS DENNE TUTORIAL ER UNDER UDVIKLING OG BILLEDER SKAL OPDATERES SÅ DER ANVENDES SAMME RASPBERRY PI
TODO
* opdater billeder
* opdatér så mqtt sendes som JSON https://gist.github.com/Paraphraser/c9db25d131dd4c09848ffb353b69038f (eller test anden måde at få flere forskellige datapunkter sendt)
* ESP32 koden har ofte problemer med at forbinde til MQTT broker (dette skal fixes)

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

**Mosquitto MQTT broker** lytter på port **1883** for MQtt besked publicationer.

**InfluxDB** lytter på port **8086** og giver en time series database til sensor data opbevaring.

**NodeRed** lytter på port **80** og anvendes med en nem grafisk interface til at parse, analysere, opbevare og viderestille sensor data beskeder.

**Grafana** lytter på port **8080** og tilbyder et datavisualiseringsmiljø til sensor data.

WiFi Connect lytter på port 80 i tilfælde af at der ikke er WiFi connectivity tilgængelig.

For at kunne modtage data fra MQTT skal der oprettes og konfigureres en **MQTT IN** node til det. Her angives IP adresse og portnummeret tilsvarende den som blev vist i balena cloud.

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/1304f28f-8410-4127-929b-9cf2eccac2ff)


tilføj efterfølgende en **debug** node og forbind den til **MQTT IN** node. Og tryk derefter på deploy knappen:

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/50b70ab8-9772-4760-9641-f3a596f30fc6)

Upload fileksemple fra micropython mappen i dette repository til ESP32 (forudsætter at der er et Educaboard med LMT84 tilsluttet) og opdater **ssid** **password** og **mqtt_server** variablerne så den kan logge på samme accespoint som raspberry pi og indsæt raspberry pi's ip addresse som **mqtt_server**. hvis ESP32 forbindes korrekt til netværket og mqtt brokeren på raspberry pi, kan man vælge debug ikonet og der bør man se data fra ESP32 som blev send over MQTT.

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/f1702b1e-757a-4c59-a14f-1fb87b6fec64)

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/47fe4b9e-efc4-433b-979d-54a781db4159)

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/a8ad16a3-33ad-4479-b66e-d43383e2cb17)

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/59588633-0d8b-422c-9939-c3fcafdb471b)

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/b21698c4-1df0-48c5-816f-08f342188889)


![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/4a77975a-95b8-4c6a-ba91-c3f74ef73c9d)

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/05fb46ed-c78f-47d5-b9ab-cb6726946cac)

se dette link for mere info om influxdb opsætningen: https://gist.github.com/Paraphraser/c9db25d131dd4c09848ffb353b69038f 

![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/9716fd47-19e1-454f-88f1-0437be607f26)

For at forbinde og lægge data i influxdb skal der oprettes en node til dette. Når man bruger Docker skal containernavnet **influxdb** angives som host:
![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/50b21102-b67a-4e15-a40a-c3442ec30a98)
Husk at tryk deploy når denne node er oprettet. 

Efterfølgende kan man åbne en influxdb shell i Balena cloud:
![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/0af718ad-e36e-4ecc-9042-ccee8750e263)

først skal man oprette en database ved at skrive:
```
$ influx
> CREATE DATABASE koji
> USE koji
> select * from temp
```
hvor koji i dette tilfælde er databasen navn. Navnet kan man selv vælge, og det bør være meningsfyldt for hvad databasen bruges til.

Fra influxdb shell kan man verificere at der kommer data i databasen, som her er fra en temperatursensor på en ESP32 der sende data til MQTT brokeren:
![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/4f94079d-5675-4d3c-b85c-164e93a95cb1)

Åben grafana i browser på den lokale IP adresse som kan findes i balena cloud og på port 8080 i mit tilfælde er addressen **http://192.168.1.128:8080/** men din vil højest sansynligt være en anden. Første gang grafana anvendes skal man oprette bruger og password (jeg anvder **admin admin** til test men i produktion skal der angives et stærkt password!). for at konfigurere grafana til at vise data fra influxdb skal man i venstre menu vælge tandhjulet og **data sources**
![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/d08d7100-6225-4e92-8fb8-26c7d0012468)

For at få vist data i grafana skal man lave et dashboard. For at gøre dette vælges ikonet med 4 firkanter i menuen:
![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/13e2c72d-5849-436c-bdbe-f96d8015551f)

Man kan lave en query:
![image](https://github.com/KevinLindemark/RPI_zero_2W_ESP32_MING_stack/assets/58036568/2fd8261c-57f3-4caf-aff0-8567c308d730)


**En ekstra ting man bør være opmærksom på**:

Når der bruges influxdb i en docker container:
Hvis node-red og influxdb containers er på samme maskine kan man ikke tilgå dem genne localhost (fordi hosten af contianeren ikke kører influxdb selv). Man skal derimod tilgå den genmmen en reference til selve containerens navn.
Eksempel: **influxdb:8086** i stedet for **localhost:8086**
