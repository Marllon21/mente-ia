import speech_recognition as sr
import edge_tts
import asyncio
import os

async def speak_async(text: str):
    communicate = edge_tts.Communicate(text=text, voice="pt-BR-FranciscaNeural")
    await communicate.save("response.mp3")
    os.system("mpg123 response.mp3") # ou outro player de áudio

def speak(text: str):
    asyncio.run(speak_async(text))

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {query}")
        return query
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return ""
    except sr.RequestError as e:
        print(f"Erro no serviço de fala; {e}")
        return ""

if __name__ == "__main__":
    speak("Olá, eu sou a Mente IA. Como posso ajudar?")
    comando = listen()
    if comando:
        speak(f"Você disse: {comando}")
