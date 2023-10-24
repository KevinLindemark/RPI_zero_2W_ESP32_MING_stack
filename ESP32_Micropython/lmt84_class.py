from machine import Pin, ADC
from time import sleep, ticks_ms

class LMT84:
    """
    LMT84 class to return temperature, celcius, fahrenheit and kelvin
    """
    def __init__(self, pin_number=35, attenuation=2, alpha = -5.5, beta = 1035, average = 128):
        self.adc = ADC(Pin(pin_number))
        self.adc.atten(attenuation)
        self.alpha = alpha
        self.beta = beta
        self.average = average
        # first number is mV and callibrated to match DHT22 temp at 20 degrees celsius (ESP32 has bad ADC)
        self.ADC_mV = 2027.0 / 4095.0 
    
    def millivolts(self):
        return self.adc.read() * self.ADC_mV
    
    def celcius_temperature(self):
        ADC_value = 0
        if self.average > 1:
            for i in range(self.average):
                ADC_value += self.adc.read()
                sleep(1 / self.average)
            ADC_value = ADC_value / self.average
        else:
            ADC_value = self.adc.read()
            sleep(1)

        mV = self.ADC_mV * ADC_value
        temperature_celcius = (mV - self.beta) / self.alpha
        return temperature_celcius
    def fahrenheit_temperature(self):
        #°F = (°C x 1.8) + 32 or °F = °C x 9 5 {\displaystyle {\frac {9}{5}}} + 32 formula.
        celsius = self.celcius_temperature()
        temperature_fahrenheit = (celsius * 1.8) + 32
        return temperature_fahrenheit
    def kelvin_temperature(self):
        # K = °C + 273.15
        temperature_kelvin = self.celcius_temperature() + 273.15
        return temperature_kelvin
        
        
        