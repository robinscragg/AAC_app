import kivy
kivy.require ('2.2.1')

from AllButtons import AllButtons
import Phrase_Lists
import Phrase_button
import Edit_folder_button
from timeit import default_timer
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

currentFolder = 0
previousFolder = 0
folderWidgets = []

class FolderButton(AllButtons):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.start = 0
        self.stop = 0
        self.folderColour = "fff2ccff"
        self.folderText = "000000ff"
        self.phraseColour = "fff2ccff"
        self.phraseText = "000000ff"
  
    def StartTimer(self):
        self.start = default_timer()
            
    def StopTimer(self):
        self.stop = default_timer() - self.start
        
        global currentFolder
        global previousFolder
        if(currentFolder !=0 & previousFolder !=0):
            previousFolder = currentFolder
        try:
            currentFolder = folderWidgets.index(self)
        except:
            pass
        
        if(Edit_folder_button.editMode == True):
            if (self.stop >= 0.5):
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
                confirmButton.bind(on_press = self.Delete)
                noButton.bind(on_press = self.popup.dismiss)
                self.popup.open()
            else:
                try:
                    self.parent.parent.parent.parent.parent.manager.current
                except:
                    self.parent.parent.parent.manager.current = "homeScreen"
                else:
                    self.parent.parent.parent.parent.parent.manager.current = "changeFolderScreen"     
        else:
            self.OpenFolder()
    
    def ChangeName(self, folderName):
        phraseLists = Phrase_Lists.PhraseLists()
        folders = phraseLists.pickleLoad('Folders.pkl')
        
        oldFolder = folders[currentFolder]
        
        folders[currentFolder] = folderName.text
        folderWidgets[currentFolder].text = folderName.text
        
        phraseLists.pickleDump('Folders.pkl', folders)
        
        folderGrid = self.parent.parent.parent.manager.get_screen("homeScreen").ids.folderView
        
        for folder in folderGrid.children:
            if(folder.text == oldFolder):
                folder.text = folderName.text
            
        self.parent.parent.parent.manager.current = "homeScreen"
        
    def OpenFolder(self):
        phraseButtons = self.parent.parent.parent.parent.parent.ids.phraseGrid
        
        phraseButtons.clear_widgets()
        
        position = folderWidgets.index(self)
        
        phraseList = Phrase_Lists.PhraseLists()
        phrases = phraseList.pickleLoad("Phrases.pkl")
        
        try:
            phrases[position]
        except:
            pass 
        else:
            phraseList = phrases[position]
            #creates phrase buttons using the list from above
            for phrase in phraseList:
                if(self.phraseColour == "fff2ccff"):
                    self.phraseColour = App.get_running_app().phraseColour
                if(self.phraseText == "000000ff"):
                    self.phraseText = App.get_running_app().phraseText
                phraseButtons.add_widget(Phrase_button.PhraseButton(text = phrase, background_normal = "", background_color = self.phraseColour, color = self.phraseText, font_name = App.get_running_app().font, font_size = App.get_running_app().fontsize))
                
    def Delete(self, button):
        self.popup.dismiss()
        folderLayout = self.parent.parent.parent.parent.parent.ids.folderView
        folderLayout.remove_widget(self)
        
        phraseLists = Phrase_Lists.PhraseLists()
        folders = phraseLists.pickleLoad('Folders.pkl')
        phrases = phraseLists.pickleLoad('Phrases.pkl')
        
        for folder in folderWidgets:
            if (folder == self):
                position = folderWidgets.index(self)
                folderWidgets.remove(self)
                folders.remove(self.text)
        
        try:
            folderList = phrases[position]
        except:
            pass
        else:
            phrases.remove(folderList)
              
        phraseLists.pickleDump('Folders.pkl', folders)
        phraseLists.pickleDump('Phrases.pkl', phrases)
        
        global currentFolder
        global previousFolder
        currentFolder = previousFolder
        
    
    