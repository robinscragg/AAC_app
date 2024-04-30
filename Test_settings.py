import Tts

#choose male or female voice
def ChooseVoice(engine):
   option = input("Would you like a male or female voice ")

   if option == "m":
      Tts.CreateMaleVoice(engine)
   elif option == "f":
      Tts.CreateFemaleVoice(engine)
   else:
      print("Please enter f or m")
      option = input()

#set/change voice speed    
def ChooseVoiceSpeed(engine):
   print("How fast would you like the voice to speak?")
   print("The scale is from 1 to 100 with 50 being normal speed")
   rate = input()
   Tts.SetSpeakSpeed(engine, rate)

#enter phrase to speak
def ChooseSpeech(engine):
   phrase = input("Please enter the phrase to speak ")
   print("Once the phrase starts, press s at anytime to stop")
   Tts.Speak(engine, phrase)
   


engine = Tts.Initialise()
#ChooseVoice(engine)
#ChooseVoiceSpeed(engine)
#ChooseSpeech(engine)

#voices = engine.getProperty("voices")
#for voice in voices:
 #print(voice)

#while engine.isBusy():
   #tts.StopSpeech(engine)
   
