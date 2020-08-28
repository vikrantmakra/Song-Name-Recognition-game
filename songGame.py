from pygame import mixer
import requests
import json
import speech_recognition as sr
import time

def play(file,stopper):    
    print("Playing Now for 30 secs.....")
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    a=takeCommand().lower()
    if  a==stopper:
        mixer.music.stop()
        return "correct"    
    else:
        mixer.music.stop
        return "wrong"
        
def songDetector(file):
    data = {
    'api_token': 'test',
    'return': 'apple_music,spotify',
    }
    files = {
    'file': open(file, 'rb'),
    }
    result = requests.post('https://api.audd.io/', data=data, files=files)
    jsonString=(result.text)
    content = json.loads(jsonString)
    title=content["result"]["title"]
    return title

def takeCommand():
    time.sleep(30)
    mixer.music.pause()
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say your Answer...")
        r.pause_threshold =1
        audio=r.listen(source)
    
    try:
        print("Recogonising...")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        print("Time is Up")
        return "None"

    return query

if __name__ == "__main__":
    score=0
    for i in range(5):
        songName=songDetector(str(i)+".mp3").lower()
        a=play(str(i)+".mp3",songName)
        if(a=="correct"):
            score=score+1
            print(f"You are correct and score is {score}")
        else:
            print(f"You are Wrong and score is {score}")