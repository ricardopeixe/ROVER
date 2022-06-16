from network import WLAN, STA_IF
from machine import Pin
from time import sleep_ms
from socket import socket, AF_INET, SOCK_STREAM
from motor_classe import *
from mensagens_pagina import mensagem_motor,pagina_controlo
from string_analises  import *
from servo_classe import *


s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80)) # listen to port 80 of localhost
s.listen(10) # start listening to a maximum of 3 simultaneous connections

motor_dc_A = Motor(14, 27, 26)#comandos para o motorA
motor_dc_B = Motor(32, 33, 25)#comandos para o motorB
servo1 = Servo(2,50)#pino servo rodas
servo3 = Servo(18,50)#pino servo rodas
servo2 = Servo(12,50)#pino servo camera
luzes1=Pin(21, Pin.OUT)
luzes2=Pin(19, Pin.OUT)
led_indic_aliment_esp=Pin(23, Pin.OUT)



while True:
    #led que indica a existência de alimentacao no esp
    led_indic_aliment_esp.on()
    
    conn, addr = s.accept() # waits for connection (i.e. blocks loop)
    msg = conn.recv(1024) # use new socket to get message from client
    new_msg=msg.decode().strip() 
    conn.send('HTTP/1.1 200 OK\n') # client expects this
    conn.send('Content-Type: text/html\n') # client expects this
    conn.send('Connection: close\n\n') # client expects this
    conn.sendall(pagina_controlo) # send whatever we want (e.g. html page)
    
    
    #luzes
    string_liga_luz=new_msg.find("GET /luz_on")
    string_desliga_luz=new_msg.find("GET /luz_off")
    if string_liga_luz!=-1:
        luzes1.on()
        luzes2.on()
    if string_desliga_luz!=-1:
        luzes1.off()
        luzes2.off()
    
    ##motores
    string_1=new_msg.find("GET /forward")
    string_2=new_msg.find('GET /backward')
    string_3=new_msg.find('GET /stop')
    
    if string_1!=-1: 
        motor_dc_A.mov_frente()
        motor_dc_B.mov_frente()
    elif string_2!=-1:
        motor_dc_A.mov_tras()
        motor_dc_B.mov_tras()
    elif string_3!=-1:
        motor_dc_A.parar()
        motor_dc_B.parar()

    # servos
    string_A=("?value=")
    string_B=('& HTTP/')
    string_C=("?values=_")
    encontra_string_1=new_msg.find(string_A)
    encontra_string_3=new_msg.find(string_C)
    
    if encontra_string_1!=-1: #verifica os indices e se é inteiro o valor devolvido
        posicao_1=procura_indice_string(new_msg, string_A)  
        posicao_2=procura_indice_string(new_msg, string_B) 
        posicao_final_real=posicao_1+len(string_A)-1rar o respetivo indice da ultima letra
        posicao_servo_pretendida=new_msg[posicao_final_real+1:posicao_2]
        valor_inteiro=verif_int(posicao_servo_pretendida) 
        
        if valor_inteiro!=-1: #caso o valor seja do tipo inteiro, entra na condição
            servo1.converter_valor(valor_inteiro)
            servo3.converter_valor(valor_inteiro)
        else: print("Não foi possível realizar a operação")

        
    elif encontra_string_3!=-1:
        posicao_1=procura_indice_string(new_msg, string_C) #procura a string_1 dentro da mensagem recebida e devolve o respetivo indice 
        posicao_2=procura_indice_string(new_msg, string_B) #procura a string_2 dentro da mensagem recebida e devolve o respetivo indice
        posicao_final_real=posicao_1+len(string_C)-1 #uma vez que a função procura_indice_string devolve o indice da primeira letra encontrada é feita a procura para encontrar o respetivo indice da ultima letra
        posicao_servo_pretendida=new_msg[posicao_final_real+1:posicao_2] # procura na mensagem o valor do ângulo
        valor_inteiro=verif_int(posicao_servo_pretendida) # verifica se o valor obtido é do tipo inteiro, pois apenas esse é o pretendido
        print(valor_inteiro)
        if valor_inteiro!=-1: #caso o valor seja do tipo inteiro, entra na condição
            servo2.converter_valor(valor_inteiro)
        else: print("Não foi possível realizar a operação")
    
    conn.close() # close temporary socket
        
    
s.close() # to close the main socket, the loop must be broken
