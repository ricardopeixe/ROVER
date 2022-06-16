#classe motor
from machine import Pin, PWM 
class Motor:
    def __init__(self, enable, pino_in1, pino_in2):
        self.pin1 = Pin(pino_in1, Pin.OUT)
        self.pin2 = Pin(pino_in2, Pin.OUT)
        self.enb=Pin(enable, Pin.OUT)
        
    def mov_frente(self): 
        self.pin1.on()
        self.pin2.off()
        self.enb.on()

    def mov_tras(self):
        self.pin1.off()
        self.pin2.on()
        self.enb.on()

    def parar(self):
        self.pin1.off()
        self.pin2.off()
        self.enb.on()
        
