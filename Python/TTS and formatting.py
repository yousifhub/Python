import pyttsx3 as tts


def speak(text):
    engine = tts.init()
    engine.say(text)
    engine.runAndWait()
    
list = []
while True:
    item = input("Enter money ('0' to finish): ")
    if item == "0":
        break
    list.append(item)
    
for x in list:
    x = int(x)
    print("${:,}".format(x))
    speak(x)
    
print("Exited correctly.")