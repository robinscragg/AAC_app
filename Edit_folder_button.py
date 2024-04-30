import kivy
kivy.require ('2.2.1')

from AllButtons import AllButtons 

from Play_button import PlayButton
from Text_input import TextInputBox

editMode = False

class EditFolderButton(AllButtons):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    #hides or shows relevant widgets
    def HideShowWidgets(self):
        #gets widgets by their id
        playButton = self.parent.parent.parent.ids.play
        textInput = self.parent.parent.parent.ids.textInput
        
        #if not in edit mode, hides buttons and turns on edit mode
        global editMode
        if (editMode == False):
            self.text = "Exit edit folder mode"
            PlayButton.MakeInvisible(playButton)
            TextInputBox.MakeInvisible(textInput)
            editMode = True
        
        #if in edit mode, shows buttons and turns off edit mode
        elif (editMode == True):
            self.text = "Enter edit folder mode"
            PlayButton.MakeVisible(playButton)
            TextInputBox.MakeVisible(textInput)
            editMode = False