

import socket #pacote comunicação
from threading import Thread


#InterFace Gráfica Kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.vector import Vector
from kivy.clock import Clock

class conection():
	def __init__(self):
		# Iniciando o TCP/IP socket
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# Conectando Socket
		server_address = ('localhost', 8008)
		self.sock.connect(server_address)
	def msg_send(self,msg):
		# Envia Mensagem
		self.sock.send(bytes(msg,'utf_8'))
	def msg_recv(self):
		res = self.sock.recv(1024)
		data = res.decode('utf_8')


class LoginScreen(Widget):
    username = ObjectProperty(None)

    def check_status(self, btn):
        print('button state is: {state}'.format(state=btn.state))
        print('text input text is: {txt}'.format(txt=self.txt_inpt))


class Interface(App):
    kv_directory = 'Client'

if __name__ == '__main__':
    Interface().run()
