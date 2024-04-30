import kivy
kivy.require ('2.2.1')

from AllButtons import AllButtons
from Phrase_Lists import PhraseLists
import Phrase_button
import Folder_button

#inherits from all buttons
class CreatePhraseButton(AllButtons):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
    def CreatePhrase(self, currentOrNew, phraseInput):
        if(currentOrNew == 0):
            phraseName = phraseInput.parent.parent.parent.manager.get_screen("homeScreen").ids.textInput.text
        else:
            phraseName = phraseInput.text
      
        phraseLists = PhraseLists()
        phrases = phraseLists.pickleLoad('Phrases.pkl')
        currentFolder = Folder_button.currentFolder
        
        try:
            phrases[currentFolder]
        except:
            newPhraseList = [phraseName]
            phrases.insert(currentFolder, newPhraseList)
        else:
            phrases[currentFolder].append(phraseName)
            
        phraseLists.pickleDump('Phrases.pkl', phrases)
        
        phraseButtons = phraseInput.parent.parent.parent.manager.get_screen("homeScreen").ids.phraseGrid
        currentFolderWidget = Folder_button.folderWidgets[currentFolder]
        newPhraseButton = Phrase_button.PhraseButton(text = phraseName, background_normal = "", background_color = currentFolderWidget.phraseColour, color = currentFolderWidget.phraseText)      
        phraseButtons.add_widget(newPhraseButton)
            
        self.parent.parent.parent.manager.current = "homeScreen"
            
       
        