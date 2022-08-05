import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something: ")
    audio = recognizer.listen(source)

words = recognizer.recognize_google(audio)

if "hello" in words:
    print("Hello to yo too!")
elif "how are you" in words:
    print("I am well, thanks")
elif "goodbye" in words:
    print("Goodbye to you  too!")
else:
    print("Huh?")
