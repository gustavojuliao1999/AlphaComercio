
#InterFace Gráfica Kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

class LoginScreen(Widget):
    username = ObjectProperty(None)

    def check_status(self, btn):
        print('button state is: {state}'.format(state=btn.state))
        print('text input text is: {txt}'.format(txt=self.txt_inpt))


class Interface(App):
    kv_directory = 'Client'

if __name__ == '__main__':
    Interface().run()
