import pyttsx3

#creates and returns engine
def Initialise():
    engine = pyttsx3.init()
    return engine

#set voice to be male
def CreateMaleVoice(engine):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

#set voice to be female  
def CreateFemaleVoice(engine):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

#sets speaking speed   
def SetSpeakSpeed(engine, rate):
    rate = int(rate)
    speed = rate + 150
    engine.setProperty('rate', speed)
    
#speaks   
def Speak(engine, phrase):
    engine.say(phrase)
    engine.runAndWait()
    
    
