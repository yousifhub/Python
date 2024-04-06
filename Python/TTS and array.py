import pyttsx3 as tts

def speak(text):
    engine = tts.init()
    engine.say(text)
    engine.runAndWait()

list = []
while True:
    item = input("Enter an item ('0' to finish): ")
    if item == "0":
        break
    list.append(item)
    
for x in list:
    print(x)
    speak(x)
    
print("Exited correctly!")