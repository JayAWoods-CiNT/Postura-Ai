# main.py

from postura import Postura

def run():
    print("Starting Postura...")
    
    ai = Postura()
    ai.boot()
    ai.run()

if __name__ == "__main__":
    run()
