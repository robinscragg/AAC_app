import kivy
kivy.require ('2.2.1')

import Tts
import Phrase_Lists

import Settings_button
import Guide_button
import Text_input
import Play_button
import Folder_button
import Create_folder_button
import Upload_folder_button
import Phrase_button
import Create_phrase_button
import Edit_folder_button

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.settings import SettingsWithSidebar
from kivy.uix.label import Label

#app
class AacApp(App):

    def build(self):
        self.settingsButton = Settings_button.SettingsButton()
        self.guideButton = Guide_button.GuideButton()
        self.playButton = Play_button.PlayButton()
        self.createFolder = Create_folder_button.CreateFolderButton()
        self.uploadFolder = Upload_folder_button.UploadFolderButton()
        self.createPhrase = Create_phrase_button.CreatePhraseButton()
        self.editFolder = Edit_folder_button.EditFolderButton()
        self.phraseButtons = Phrase_button.PhraseButton()

        self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False
        
        self.textToSpeech = Tts.Initialise()
        
        self.voice = self.config.get('Voice', 'voiceoptions')
        if(self.voice == "Male"):
            Tts.CreateMaleVoice(self.textToSpeech)
        elif(self.voice == "Female"):
            Tts.CreateFemaleVoice(self.textToSpeech)
        
        self.rate = self.config.get('Voice', 'speed')
        Tts.SetSpeakSpeed(self.textToSpeech, int(self.rate))
        
        self.font = self.config.get('Text', 'fontoptions')
        self.fontsize = self.config.get('Text', 'size')
        
        self.allColour = self.config.get('Colours', 'allColour')
        self.textColour = self.config.get('Colours', 'textColour')
        self.folderColour = self.config.get('Colours', 'folderColour')
        self.folderText = self.config.get('Colours', 'folderText')
        self.phraseColour = self.config.get('Colours', 'phraseColour')
        self.phraseText = self.config.get('Colours', 'phraseText')
        
        self.currentFolder = self.config.get('Style', 'currentFolder')
        self.currentFolderText = self.config.get('Style', 'currentFolderText')
        self.currentPhrase = self.config.get('Style', 'currentPhrase')
        self.currentPhraseText = self.config.get('Style', 'currentPhraseText')
    
        self.phraselists = Phrase_Lists.PhraseLists()
        self.originalFolders = ["Needs", "Feelings", "Greetings"]
        self.originalPhrases = [["I need to use the bathroom", "Can we leave?", "I'm going to go", "I'm overwhelmed", "I want some space"], ["I like that", "I feel uncomfortable"], ["How are you?", "I'm doing well, thanks"]]
        self.folders = self.phraselists.checkForFolderDump(self.originalFolders)
        self.phrases = self.phraselists.checkForPhraseDump(self.originalPhrases)
            
        kv = Builder.load_file("kivy_file.kv")
        return kv
    
    def build_config(self, config):
        config.adddefaultsection('Voice')
        config.setdefaults('Voice', {'voiceoptions': 'Male', 'speed': '50'})
        config.setdefaults('Text', {'fontoptions': 'Arial', 'size': '20'})
        config.setdefaults('Colours', {'allColour' : "fff2ccff", 'textColour' : "000000ff",  'folderColour' : "fff2ccff", 'folderText' : "000000ff", 'phraseColour' : "fff2ccff", 'phraseText' : "000000ff"})
        config.setdefaults('Style', {'currentFolder' : "fff2ccff", 'currentFolderText' : "000000ff", 'currentPhrase' : "fff2ccff", 'currentPhraseText' : "000000ff"})

    def build_settings(self, settings):
        settings.add_json_panel('Voice', self.config, 'Voice_settings.json')
        settings.add_json_panel('Text', self.config, 'Text_settings.json')
        settings.add_json_panel('Colours', self.config, 'Colour_settings.json')
        settings.add_json_panel('Style', self.config, 'FolderStyle.json')
        
    def on_config_change(self, config, section, key, value):
        self.voice = self.config.get('Voice', 'voiceoptions')
        if(self.voice == "Male"):
            Tts.CreateMaleVoice(self.textToSpeech)
        elif(self.voice == "Female"):
            Tts.CreateFemaleVoice(self.textToSpeech)
        
        self.rate = int(self.config.get('Voice', 'speed'))
        popup = Popup(title='Change input', content=Label(text='Enter a value between 1 and 100'), size_hint = (0.5,0.5))
        if (1<= self.rate <=100):
            Tts.SetSpeakSpeed(self.textToSpeech, self.rate)
        else:
            popup.open()
                
        self.font = self.config.get('Text', 'fontoptions')
        self.settingsButton.ChangeFont(self.font)
        self.guideButton.ChangeFont(self.font)
        self.createFolder.ChangeFont(self.font)
        self.uploadFolder.ChangeFont(self.font)
        self.createPhrase.ChangeFont(self.font)
        self.editFolder.ChangeFont(self.font)
        
        self.fontsize = int(self.config.get('Text', 'size'))
        fontpopup = Popup(title='Change input', content=Label(text='Entering a negative value removes the text'), size_hint = (0.5,0.5))
        if(self.fontsize <=0):
            fontpopup.open()
        else:
            self.settingsButton.ChangeFontSize(self.fontsize)
            self.guideButton.ChangeFontSize(self.fontsize)
            self.createFolder.ChangeFontSize(self.fontsize)
            self.uploadFolder.ChangeFontSize(self.fontsize)
            self.createPhrase.ChangeFontSize(self.fontsize)
            self.editFolder.ChangeFontSize(self.fontsize)

        currentFolderWidget = Folder_button.folderWidgets[Folder_button.currentFolder]
        
        self.folderColour = self.config.get('Colours', 'folderColour')
        self.folderText = self.config.get('Colours', 'folderText')
        for folder in Folder_button.folderWidgets:    
                if(folder.folderColour == "fff2ccff"): 
                    folder.folderColour = self.folderColour
                folder.ChangeColour(folder.folderColour)
                if(folder.folderText == "000000ff"):
                    folder.folderText = self.folderText
                folder.ChangeTextColour(folder.folderText)
                folder.ChangeTextColour(folder.folderText)
                folder.ChangeFont(self.font)
                folder.ChangeFontSize(self.fontsize)
            
        self.phraseColour = self.config.get('Colours', 'phraseColour')
        self.phraseText = self.config.get('Colours', 'phraseText')
        for phrase in self.phraseButtons:
            phrase.ChangeColour(self.phraseColour)
            phrase.ChangeTextColour(self.phraseText)
            phrase.ChangeFont(self.font)
            phrase.ChangeFontSize(self.fontsize)

        self.allColour = self.config.get('Colours', 'allColour')
        self.settingsButton.ChangeColour(self.allColour)
        self.guideButton.ChangeColour(self.allColour)
        self.playButton.ChangeColour(self.allColour)
        self.createFolder.ChangeColour(self.allColour)
        self.uploadFolder.ChangeColour(self.allColour)
        self.createPhrase.ChangeColour(self.allColour)
        self.editFolder.ChangeColour(self.allColour)
        
        self.textColour = self.config.get('Colours', 'textColour')
        self.settingsButton.ChangeTextColour(self.textColour)
        self.guideButton.ChangeTextColour(self.textColour)
        self.createFolder.ChangeTextColour(self.textColour)
        self.uploadFolder.ChangeTextColour(self.textColour)
        self.createPhrase.ChangeTextColour(self.textColour)
        self.editFolder.ChangeTextColour(self.textColour)
        
        if((self.config.get('Style', 'currentFolder') != self.currentFolder) or (self.config.get('Style', 'currentFolderText') != self.currentFolderText) or (self.config.get('Style', 'currentPhrase') != self.currentPhrase) or (self.config.get('Style', 'currentPhraseText') != self.currentPhraseText)):
            self.currentFolder = self.config.get('Style', 'currentFolder')
            self.currentFolderText = self.config.get('Style', 'currentFolderText')
            self.currentPhrase = self.config.get('Style', 'currentPhrase')
            self.currentPhraseText = self.config.get('Style', 'currentPhraseText')
            
            currentFolderWidget.folderColour = self.currentFolder
            currentFolderWidget.folderText = self.currentFolderText
            currentFolderWidget.phraseColour = self.currentPhrase
            currentFolderWidget.phraseText = self.currentPhraseText
            
            currentFolderWidget.ChangeColour(currentFolderWidget.folderColour)
            currentFolderWidget.ChangeTextColour(currentFolderWidget.folderText)
                
            for phrase in self.phraseButtons:
                phrase.ChangeColour(currentFolderWidget.phraseColour)
                phrase.ChangeTextColour(currentFolderWidget.phraseText)
                
            Folder_button.folderWidgets[Folder_button.currentFolder] = currentFolderWidget
        
class HomeScreen(Screen):
    def GetButtons(self):
        App.get_running_app().settingsButton = self.ids.settings.__self__
        App.get_running_app().guideButton = self.ids.guide.__self__
        App.get_running_app().playButton = self.ids.play.__self__
        App.get_running_app().createFolder = self.ids.createFolder.__self__
        App.get_running_app().uploadFolder = self.ids.UploadFolder.__self__
        App.get_running_app().createPhrase = self.ids.createPhrase.__self__
        App.get_running_app().editFolder = self.ids.editFolder.__self__
        App.get_running_app().phraseButtons = self.ids.phraseGrid.__self__.children
        
        App.get_running_app().open_settings()
        
class GuideScreen(Screen):
    pass

class NewFolderScreen(Screen):
    pass

class NewPhraseScreen(Screen):
    pass

class ChangeFolderNameScreen(Screen):
    pass

class ChangePhraseNameScreen(Screen):
    pass

class AppScreenManager(ScreenManager):
    pass
        
if __name__ == '__main__':
    AacApp().run() 
    
