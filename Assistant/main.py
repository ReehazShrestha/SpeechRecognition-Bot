import google.generativeai as genai
import pyttsx3
import speech_recognition as sr


recognize = sr.Recognizer()
genai.configure(api_key="AIzaSyDamDyhxxAKQXhfsFbImw65-L_rehmbcQg")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
print(":")

while True:

    try:
        with sr.Microphone() as mic:
            recognize.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognize.listen(mic)

            text = recognize.recognize_google(audio)
            text = text.lower()
            print(f"User: {text}")
            if text == "exit":
                break
            else:    
                chat.send_message(f"{text} provide information under 100 lines or less !")
                prompt = chat.last.text
                voice = pyttsx3.init()
                voice.say(prompt)
                voice.runAndWait()
                print(f"Bot: {prompt}")

    except:
        recognize = sr.Recognizer()
        if text == "exit":
            breaK
        continue


