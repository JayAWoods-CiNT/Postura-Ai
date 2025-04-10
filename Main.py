# postura.py

class Postura:
    def __init__(self):
        self.state = "initialized"

    def boot(self):
        print("[Postura] Booting up...")
        self.state = "ready"

    def run(self):
        print("[Postura] Running behavioral loop...")
        while True:
            user_input = input("[You] > ")
            if user_input.lower() in ["exit", "quit"]:
                print("[Postura] Shutting down.")
                break
            print(f"[Postura] You said: {user_input}. I'm learning...")
