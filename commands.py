import webbrowser
import os
import datetime
import time 
from voice import say
from brain import chat, ai

def handle_commands(query):
                sites = [
                    ["youtube", "https://www.youtube.com"],
                    ["wikipedia", "https://www.wikipedia.org"],
                    ["facebook", "https://www.facebook.com"],
                    ["instagram", "https://www.instagram.com"],
                ]
                handled = False

                for site in sites:

                    if ("open " + site[0]).lower() in query.lower():
                        say(f"Opening {site[0]} sir")
                        webbrowser.open(site[1])
                        handled = True
                        break
                    if handled:
                        continue

                if "open music" in query.lower():
                        musicpath = r"C:\Users\azmai\Documents\CODE\Project\SSpotify clone\songs\t1.mp3"
                        say(f"Opening sir")
                        os.startfile(musicpath)

                elif "open riot" in query.lower():
                        riotpath= f"C:\Riot Games\Riot Client\RiotClientServices.exe"
                        say(f"Opening sir")
                        os.startfile(riotpath)  
                elif "open spotify".lower() in query.lower():
                        say(f"Opening sir")
                        webbrowser.open("https://open.spotify.com")
                elif "call your father".lower() in query.lower():
                        say(f"Opening sir")
                        webbrowser.open("https://chatgpt.com")
                elif "what time is it" in query.lower():
                        say(datetime.datetime.now().strftime("%H:%M"))

                elif "using artificial intelligence".lower() in query.lower():
                        say(f"Using")
                        ai(prompt=query)
                elif "let's turn off".lower() in query.lower():
                        say(f"Bye")
                        exit()
                elif "reset chat".lower() in query.lower():
                        chatStr = ""
                else:
                    print("chatting...")
                    chat(query)