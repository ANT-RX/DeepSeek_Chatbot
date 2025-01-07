import speech_recognition as sr

class microphone:
    def __init__(self, ):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def listen(self):
        with self.mic as source:
            print("Ajustando el microfono.")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Escuchando...")
            audio = self.recognizer.listen(source)
        
        try:
            text = self.recognizer.recognize_google(audio, language='es-ES')
            return text
        except sr.UnknownValueError:
            return "No pude comprender el audio"
        except sr.RequestError:
            return "Error al conectar con el servicio de reconocimiento."