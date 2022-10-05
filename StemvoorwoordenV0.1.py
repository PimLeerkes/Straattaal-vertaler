import pyttsx3
# template stemgedeelte
class Speaking:
    def speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()
        #stem leest voor
class GFG:
    def Dictionary(self):
        woorden = open("woorden.txt", "r")
        woorden = woorden.readlines()
        speak = Speaking()
        speak.speak("Welk woord wil je horen?")
        word = woorden
        print(len(word))
        for woorden in word:
            print([woorden])
            speak.speak("" + (woorden))
if __name__ == '__main__':
    GFG()
    GFG.Dictionary(self=None)
