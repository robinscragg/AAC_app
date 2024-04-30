import kivy 
kivy.require ('2.2.1')

from kivy.uix.button import Button

class AllButtons(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def ChangeColour(self, colour):
        self.background_color = colour
            
    def ChangeTextColour(self, colour):
        self.color = colour
        
    def ChangeFont(self, font):
        self.font_name = font
        
    def ChangeFontSize(self, size):
        self.font_size = size
            
    