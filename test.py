import speech_recognition as sr
mic = sr.Microphone()
list_mic = sr.Microphone.list_microphone_names()
for i in range(0,len(list_mic)):
    print(i, list_mic[i])