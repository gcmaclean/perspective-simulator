import random

class Reframer:

    def __init__(self):
        self.responses = {
            "Academic": [ 
                "This is feedback, not failure.",
                "Mistakes are part of learning.",
                "You now know exactly what to improve."  
            ], 

            "Career": [
                "This is redirection toward a better opportunity.",
                "Rejection is data, not defeat.",
                "Every no is progress toward the right yes."   
            ],

            "Social": [
                "Relationships shift to better align over time.",
                "This moment doesn't define your social value.",
                "People come and go, but growth stays."
            ],

            "General": [
                "This moment is temporary.",
                "You are reacting to one monment, not your whole life.",
                "Perspective changes everything."
            ]
        }

        self.actions = {
            "Academic": ["Review mistakes", "Study in smaller chunks", "Start studying earlier", "Ask for help"],
            "Career": ["Improve resume", "Apply more", "Learn new skill"],
            "Social": ["Communicate clearly", "Reflect on interaction", "Focus on others"],
            "General": ["Take a break", "Write thoughts", "Focus on one task"]
        }

        self.situations = {
            "stolen_item": {
                "keywords": ["stole", "stolen", "taken", "took"],
                "reframes": [
                    "Losing an item is frustrating, but it's replaceable.",
                    "This is a property loss, not a personal loss.",
                    "Your day is not defined by one missing object."
                ],
                "actions": [
                    "Try to recover or replace it",
                    "Report it if necessary",
                    "Focus on what you still have"
                ]
            }
        }

    def generate(self, text, category):

        text_lower = text.lower()

        #1. Specific situations first
        for key, data in self.situations.items():
                for word in data["keywords"]:
                     if word in text_lower:
                        
                        return {
                            "old_mood": random.randint(30, 50),
                            "new_mood": random.randint(60, 95),
                            "reframe": random.choice(data["reframes"]),
                            "actions": data["actions"]
                        }
            
        #2 Fallback to category logic
        return {
            "old_mood": random.randint(30, 60),
            "new_mood": random.randint(55, 95),
            "reframe": random.choice(self.responses[category]),
            "actions": self.actions[category]
        }


def generate_response(text, category):
    engine = Reframer()
    return engine.generate(text, category)