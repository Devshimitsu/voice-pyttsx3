import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# engine.setProperty('voice', voices[0].id) #Default Male Voice
engine.setProperty('voice', voices[1].id) #Cortana(Will Only Run When You Will install Cortana.reg)
# engine.setProperty('voice', voices[2].id) #Default Female Voice

engine.say("hi")
engine.say("this is how i sound")
engine.runAndWait()