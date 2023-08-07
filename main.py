import sys
import os

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    # turn off the console log if the app is frozen
    os.environ['KIVY_NO_CONSOLELOG'] = '1'

from kivy.app import App
from kivy.uix.label import Label
import itertools


class HelloLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hellos = itertools.cycle(['Hello to you!', 'Hey There!', "What's up?"])

    def say_hello(self):
        self.text = next(self.hellos)


class ExampleWithPyinstallerApp(App):
    pass


ExampleWithPyinstallerApp().run()
