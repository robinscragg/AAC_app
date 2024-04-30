import pickle
import os

class PhraseLists():
    def __int__(self):
        pass
    
    def pickleDump(self, pickle_file, data):
        with open(pickle_file,'wb') as file:
            pickle.dump(data, file, protocol = 0)
        
    def pickleLoad(self, pickle_file):
        with open(pickle_file, 'rb') as file:
            loaded = pickle.load(file)
        return loaded
    
    def checkForFolderDump(self, folderObjects):
        if (os.stat('Folders.pkl').st_size == 0):
            with open('Folders.pkl','wb') as file:
                pickle.dump(folderObjects, file, protocol = 0)
        
        loaded = self.pickleLoad('Folders.pkl')
        return loaded
        
    def checkForPhraseDump(self, phraseObjects):
        if (os.stat('Phrases.pkl').st_size == 0):
            with open('Phrases.pkl','wb') as file:
                pickle.dump(phraseObjects, file, protocol = 0)
        
        loaded = self.pickleLoad('Phrases.pkl')
        return loaded
        
