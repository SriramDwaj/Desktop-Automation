import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):  # this function makes the jarvis speak
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # this function is used for wish or greet
    hour = int(datetime.datetime.now().hour)
    if hour <= 0 and hour < 12:
        speak("Good Morning Ram !")
        speak(" I am Jarvis how can i be your assistance")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon Ram !")
        speak(" I am Jarvis how can i be your assistance")
    else:
        speak("Good Evening Ram!")

        speak(" I am Jarvis how can i be your assistance")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)   #2 is returning 2 sentences from wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'D:\\MyMusic\\Englishsongs\\Favorite Songs2'   #path of the music directory
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))   
            os.startfile(music_dir)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open movies' in query:
            movPath = "E:\movies\Bhaag.Milkha.Bhaag.2013.1080p.BluRay.x264.ShAaNiG.com.mkv"  #path of the movie directory
            os.startfile(movPath)


