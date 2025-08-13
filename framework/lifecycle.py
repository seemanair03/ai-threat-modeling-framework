# framework/lifecycle.py        
class AILifecycleStage:
    def __init__(self, name, description):
        self.name = name
        self.description = description

LIFECYCLE_STAGES = [
    AILifecycleStage("Data Collection", "Sources, labeling, privacy"),
    AILifecycleStage("Model Training", "Architecture, hyperparameters, training data"),
    AILifecycleStage("Deployment", "Serving, APIs, cloud environment"),
    AILifecycleStage("Monitoring", "Drift detection, logging, feedback loops")
]