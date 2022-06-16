from class_httphandler import HTTPHandler
from machine import Pin
from time import sleep_ms
import camera

#função que analisa o pedido de servidor
def handle_request(request):
    http = HTTPHandler

    headers = request.split('\n')
    get_content = headers[0].split()

    accept = headers[6].split()
    type_content = accept[1].split('/')

    filename = get_content[1]

    if get_content[0] == "GET" and get_content[1]!='/tira_foto_cam': #executa para responder aos pedidos de servidor
        content = http.get(None, get_content[1], type_content[0])
    if get_content[1]=='/tira_foto_cam': #executa sempre que é solicitada uma foto
        Pin(4,Pin.OUT).value(1)
        sleep_ms(1000)
        Pin(4,Pin.OUT).value(0)
        camera.init()
        buf=camera.capture()
        camera.deinit()
        content=buf        
        f= open('fotografia.jpg', 'wb')
        f.write(buf)
        f.close()
        print('Processo Terminado')
        
    return content
