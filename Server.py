#Database
import sqlite3

from datetime import datetime

import socket
from threading import Thread

class ThreadedServer(Thread):
    def __init__(self, host, port, timeout=60, debug=False):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.debug = debug
        Thread.__init__(self)

    # Iniciando Thread Server
    def run(self):
        if self.debug:
            print(datetime.now())
            print('Iniciando Server...', '\n')

        self.listen()

    def listen(self):
        # Criando Instancia para o Socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # ligando o soquete ao host e porta
        self.sock.bind((self.host, self.port))
        if self.debug:
            print(datetime.now())
            print('SERVIDOR do Socket Conectado ao', self.host, self.port, '\n')

        # start listening for a client
        self.sock.listen(5)
        if self.debug:
            print(datetime.now())
            print('SERVER Recebendo...', '\n')
        while True:
            # get the client object and address
            client, address = self.sock.accept()

            # Definir tempo limite
            client.settimeout(self.timeout)

            if self.debug:
                print(datetime.now())
                print('CLIENTE conectado', client, '\n')

            #
            # iniciando um Threado para receber do cliente
            Thread(target = self.listenToClient,args = (client,address)).start()


    def listenToClient(self, client, address):
        # Difinindo o tamanho do buffer (pode ser 2048 ou 4096 / potência de 2)
        size = 1024
        while True:
            try:
                # Tentando receber dados do Cliente
                data = client.recv(size).decode('utf-8')
                if data:
                    #data = loads(data.rstrip('\0'))
                    if self.debug:
                        print(datetime.now())
                        print('CLIENT Data Recebido', client)
                        print('Data:')
                        print(data)
                        if (data) == "Connected":
                            print("Sucess")
                        if(data) == "break":
                            break
                        #pprint(data, width=1)
                        print('\n')
                        client.send((data).encode('utf-8'))
                        print("END")

                    #send a response back to the client
                    '''res = {
                        'cmd': data['cmd'],
                        'data': data['data']
                    }'''

                    #response = dumps(res)

                else:
                    raise socket.error('Erro Cliente Desconectado')



            except:
                if self.debug:
                    print(datetime.now())
                    print('CLIENT Desconectado:', client, '\n')
                client.close()
                return False
class commands():
    def key_conection(self):
        print("")


if __name__ == "__main__":
    #iniciando Server(ip,porta, tempo maximo resposta, debug)
    ThreadedServer('127.0.0.1', 8008, timeout=86400, debug=True).start()



