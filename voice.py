import speech_recognition as sr
import pyttsx3

def say(text):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 155)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":
    print("AXIOM")
    say("Hello Sir")

r = sr.Recognizer()
def takeCommand():
            with sr.Microphone() as source:
                print("Listening...")

                r.pause_threshold = 0.8
                r.adjust_for_ambient_noise(source, duration=1)
                try:
                    audio = r.listen(
                    source,
                    timeout=9,
                    phrase_time_limit=5
                    )
                    query = r.recognize_google(audio, language="en-US")
                    return query
                # print("You said:", query)
                except sr.WaitTimeoutError:
                    print("No speech detected.")
                    return""
                except sr.UnknownValueError:
                    print("Could not understand audio.")
                    return""
                except Exception as e:
                    print(e)
                    return""
