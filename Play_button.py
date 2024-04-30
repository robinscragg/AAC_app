import kivy

kivy.require ('2.2.1')

import Tts
from AllButtons import AllButtons

#inherits from all buttons
class PlayButton(AllButtons):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    #play speech
    def Play(self, textts):
        textin = self.parent.parent.parent.ids.textInput
        inputtedText= textin.GetText()
        
        #if no text entered, reminds user to enter text
        if (inputtedText == ""):
            Tts.Speak(textts, "Enter text to speak")
        else:
            Tts.Speak(textts, inputtedText)
    
    #makes play button invisible
    def MakeInvisible(self):
        self.opacity = 0
     
    #makes play button visible
    def MakeVisible(self):
        self.opacity = 1