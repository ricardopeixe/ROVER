#classe servo
from machine import Pin, PWM
class Servo:
    def __init__(self, pin_pwm, freq):
        self.freq=freq
        self.pwm=PWM(Pin(pin_pwm, Pin.OUT),freq)
    
    def converter_valor(self,angulo):
        valor_convertido=0.000006*(angulo)**2+0.5722*(angulo)+25 #os ângulos lidos no slider são em graus (0-180) uma vez que apenas são recebidos valores entre 25-130, é necessário fazer essa conversão
        print('metodo')
        self.pwm.duty(int(valor_convertido))