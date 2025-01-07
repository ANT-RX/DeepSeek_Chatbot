# Prueba del código de reconocimiento de voz individualmente,
# Comprueba el funcionamiento del microfono y del algoritmo
import speech_recognition as sr

recognizer = sr.Recognizer()

mic = sr.Microphone()

with mic as source:
    audio = recognizer.listen(source)

text = recognizer.recognize_google(audio, language = 'ES')

print(f'Has dicho: {text}')