#class que responde aos pedidos de servidor. Para apresentar a página HTML e enviar imagens
class HTTPHandler:

    def get(self, args, type_content):
        if args == '/':
            args = '/index.html'
            fin = open(args)
        if type_content != "image":
            fin = open(args)

        if type_content.find("html") == -1:
            image_data = open(args, 'rb')
            bytes_foto = image_data.read()          

            # Content-Type: image/jpeg
            content = bytes_foto
            image_data.close()
            return content        

        content = fin.read()
        fin.close()
        return content
