from commands import handle_commands
from voice import takeCommand

while True:
    query = takeCommand()

    if query:
        handle_commands(query)

        print(f"COMMAND: {query}")