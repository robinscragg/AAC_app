import kivy
kivy.require ('2.2.1')

from AllButtons import AllButtons
import Edit_folder_button
import Phrase_Lists
from timeit import default_timer
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from functools import partial

currentPhrase = 0
#inherits from all buttons
class PhraseButton(AllButtons):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def StartTimer(self):
        self.start = default_timer()
        
    def StopTimer(self, currentFolder):
        self.stop = default_timer() - self.start
        phraseLists = Phrase_Lists.PhraseLists()
        phrases = phraseLists.pickleLoad("Phrases.pkl")
        global currentPhrase
        try:
            currentPhrase = phrases[currentFolder].index(self.text)
        except:
            pass
        if(Edit_folder_button.editMode == True):
            if(self.stop >=0.5):
                layout = BoxLayout(orientation = 'vertical')
                label = Label(text = "Are you sure you want to delete?")
                layout.add_widget(label)
                
                confirmButton = Button(text = "Yes")
                noButton = Button(text = "No")
                buttonLayout = BoxLayout(orientation = "horizontal")
                buttonLayout.add_widget(confirmButton)
                buttonLayout.add_widget(noButton)
                layout.add_widget(buttonLayout)
                
                self.popup = Popup(title = "Confirm deletion", content = layout)
                deleteMethod = partial(self.Delete, currentFolder)
                confirmButton.bind(on_press = deleteMethod)
                noButton.bind(on_press = self.popup.dismiss)
                self.popup.open()                
              
            else:
                try:
                    self.parent.parent.parent.parent.parent.manager.current = "changePhraseScreen"
                except:
                    self.parent.parent.parent.manager.current = "homeScreen"
        else:
            self.SendTextToTextInput()
            
    def SendTextToTextInput(self):
        textin = self.parent.parent.parent.parent.parent.ids.textInput
        textin.SetText(self.text)
    
    def ChangeName(self, phraseName, currentFolder):
        phraseLists = Phrase_Lists.PhraseLists()
        phrases = phraseLists.pickleLoad("Phrases.pkl")
        changedPhrase = phraseName.text
        
        global currentPhrase
        oldPhrase = phrases[currentFolder][currentPhrase]
        phrases[currentFolder][currentPhrase] = changedPhrase
        
        
        phraseButtons = self.parent.parent.parent.manager.get_screen("homeScreen").ids.phraseGrid

        for phraseWidget in phraseButtons.children:
            for phraseText in phrases[currentFolder]:
                if(phraseWidget.text == oldPhrase):
                    phraseWidget.text = changedPhrase
            
        phraseLists.pickleDump("Phrases.pkl", phrases)

    def Delete(self, currentFolder, button):
        self.popup.dismiss()
        phraseButtons = self.parent.parent.parent.parent.parent.ids.phraseGrid
        phraseButtons.remove_widget(self)
        
        phraseLists = Phrase_Lists.PhraseLists()
        phrases = phraseLists.pickleLoad('Phrases.pkl')
        
        folderList = phrases[currentFolder]
        
        for phrase in folderList:
            if (self.text == phrase):
                phrases[currentFolder].remove(phrase)
                
        phraseLists.pickleDump('Phrases.pkl', phrases)