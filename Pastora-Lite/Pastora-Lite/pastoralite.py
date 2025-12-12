import json

class PastoraLite:
    def __init__(self, persona_path="persona.json"):
        with open(persona_path, "r", encoding="utf-8") as f:
            self.persona = json.load(f)

    def get_persona(self):
        return self.persona
