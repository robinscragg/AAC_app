import kivy
kivy.require ('2.2.1')

from AllButtons import AllButtons 
from Phrase_Lists import PhraseLists
import Folder_button

class CreateFolderButton(AllButtons):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
                   
    def CreateFolder(self, textinput, folderColour, textColour):
        folder_name = textinput.text
        
        phraseLists = PhraseLists()
        folders = phraseLists.pickleLoad('Folders.pkl')
        folders.append(folder_name)
        phraseLists.pickleDump('Folders.pkl', folders)
        
        folderButtons = textinput.parent.parent.parent.manager.get_screen("homeScreen").ids.folderView
        newFolder = Folder_button.FolderButton(text = folder_name, background_color = folderColour, color = textColour)
        folderButtons.add_widget(newFolder)
        Folder_button.folderWidgets.append(newFolder)
        
        textinput.parent.parent.parent.manager.current = "homeScreen"