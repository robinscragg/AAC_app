import kivy
kivy.require ('2.2.1')

from AllButtons import AllButtons 

class UploadFolderButton(AllButtons):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)