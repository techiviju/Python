import speech_recognition as sr
# get a voice
r=sr.Recognizer() 
# function
with sr.Microphone() as sourse:
    r.adjust_for_ambient_noise(sourse,duration=1)
    print('BOT: I Can Here You...')

    #listen mic
    audio=r.listen(sourse)
    try:
        tetx=r.recognize_google(audio)
        print(tetx)

    except:
        print("Say that again please....")