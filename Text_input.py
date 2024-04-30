import kivy 
kivy.require ('2.2.1')

from kivy.uix.textinput import TextInput

class TextInputBox(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    #returns text in text input box
    def GetText(ti):
        inputtedText = ti.text
        return inputtedText
    
    #inserts phrase where cursor is
    def SetText(self, phrase):
        self.insert_text(phrase, from_undo = False)
        self.text += " "
    
    #makes text input box invisible
    def MakeInvisible(self):
        self.opacity = 0
    
    #makes text input box visible
    def MakeVisible(self):
        self.opacity = 1
    