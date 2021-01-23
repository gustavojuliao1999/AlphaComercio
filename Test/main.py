from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class WelcomeScreen(Screen):
    pass


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ScreenManager(ScreenManager):
    pass


class CrimePrevention(BoxLayout):
    pass


Builder.load_file("main.kv")


class TestApp(App):
    title = 'Kivy ScreenManager & ActionBar Demo'

    def build(self):
        return CrimePrevention()


if __name__ == '__main__':
    TestApp().run()