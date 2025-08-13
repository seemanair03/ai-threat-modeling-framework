import json

class Threat:
    def __init__(self, id, name, category, severity, lifecycle_stage, mitigation):
        self.id = id
        self.name = name
        self.category = category
        self.severity = severity
        self.lifecycle_stage = lifecycle_stage
        self.mitigation = mitigation

def load_threats(filepath="data/plot4ai_threats.json"):
    with open(filepath, "r") as f:
        threats = json.load(f)
    return [Threat(**t) for t in threats]