import pyttsx3


class pytts():
    def speak(self, message):
        self.server = pyttsx3.init()
        self.voice = self.server.getProperty("voice")
        self.speak = pyttsx3.speak(message)
        self.server.runAndWait()




if __name__ == "__main__" :
    obj = pytts()
    obj.speak("hello")