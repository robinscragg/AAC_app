import kivy
kivy.require ('2.2.1')

from AllButtons import AllButtons 

#inherits from all buttons
class SettingsButton(AllButtons):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)