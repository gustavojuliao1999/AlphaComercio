

import socket #pacote comunicação
from threading import Thread


#InterFace Gráfica Kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import ActionBar
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang import Builder

global login
global password
class conection():
	print("Inicando Socket")
	# Iniciando o TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Conectando Socket
	server_address = ('localhost', 8008)
	sock.connect(server_address)

	conection_key = ""


	def msg_send(self,msg):
		# Envia Mensagem
		self.sock.send(bytes(msg,'utf_8'))
	def msg_recv(self):
		res = self.sock.recv(1024)
		data = res.decode('utf_8')

	def get_conn(self,login,password):
		print("Login:",str(login))
		print("Password:", str(password))

class widgets():
	def add_widget(self,name):

		switcher = {
			"Login": LoginScreen,
			"Menu": Menu,
			"Connected": Connected
		}
		try:
			self.manager.add_widget(switcher.get(name, "Erro")(name=name))

		except:
			print("problema ao adicionar Widget ",name)
	def remove_widget(self,remov):
		janelas = widgets.list_widgets(self)
		try:
			b = janelas.index(remov)
			self.manager.remove_widget(self.manager.get_screen(remov))
		except ValueError:
			print("Problema ao Remover Widget não existe ",remov)
	def list_widgets(self):
		screens = self.manager.screen_names
		print("Screens:", str(screens))
		return screens



class LoginScreen(Screen):

	print("Starting")
	login = ObjectProperty()
	def Login(self,login,password):
		print("Login:",login)
		print("Pass:",password)
		if(str(login) == "test" and str(password) == "123"):
			conection.msg_send(conection,"Connected")
			widgets.add_widget(self, "Connected")
			widgets.remove_widget(self,"Login")
			print("Connected")

		else:
			return LoginScreen()
		print("Ending")

class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()
        app.username = loginText
        app.password = passwordText

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

        app.config.read(app.get_application_config())
        app.config.write()
    def resetForm(self):
        self.ids['login'].text = ("")
        self.ids['password'].text = ("")

class Connected(Screen):

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
class Menu(Screen):
	def screens(self):
		screens = widgets.list_widgets()

class Interface(App):
	kv_directory = 'Client'

	def build(self):
		#self.manager = ScreenManager()
		#widgets.add_widget(self, "Menu")
		#widgets.add_widget(self,"Login")




		return self.manager




if __name__ == '__main__':
    Interface().run()
