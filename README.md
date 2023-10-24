# RPI_zero_2W_ESP32_MING_stack

when using influxdb on a docker container:
If your node-red and influxdb containers are in the same machine, you can't reference it using localhost (because the host of the container is not running an influxdb itself). You need to reference it using the name of the container.
Example: influxdb:8086 instead of localhost:8086.
