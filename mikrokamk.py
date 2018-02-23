# kvnestedbox.py
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')
Config.set('graphics', 'resizable', False)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.slider import Slider
from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.factory import Factory
class ColorDownButton(Button):
    """
    Button with a possibility to change the color on on_press (similar to background_down in normal Button widget)
    """
    background_color_normal = ListProperty([1, 1, 1, 0.5])
    background_color_down = ListProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super(ColorDownButton, self).__init__(**kwargs)
        self.background_normal = ""
        self.background_down = ""
        self.background_color = self.background_color_normal

    def on_press(self):
        self.background_color = self.background_color_down

    def on_release(self):
        self.background_color = self.background_color_normal


########################################################################
class HBoxWidget(Widget):
    pass

########################################################################
class VBoxWidget(Widget):
    pass

########################################################################
class MikroKamKApp(App):
    """"""
    brightness = NumericProperty(50)
    contrast = NumericProperty(50)

    #----------------------------------------------------------------------
    def build(self):
        """"""
        return VBoxWidget()
    def checkActive1(self, *args):
        if args[1]:
            self.Status3 = "Devide On"
            print("Turning On")
        else:
            self.Status3 = "Device Off"
            print("Turning Off")

   

#----------------------------------------------------------------------
if __name__ == "__main__":
    
    app = MikroKamKApp()
    app.run()