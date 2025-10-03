import yaml # pyright: ignore[reportMissingModuleSource]
from framework.threat_taxonomy import load_threats

def map_threats_to_model(model_profile_path):
    with open(model_profile_path, "r") as f:
        model_profile = yaml.safe_load(f)

    threats = load_threats()
    relevant_threats = [
        t for t in threats if t.lifecycle_stage in model_profile["lifecycle"]
    ]

    for threat in relevant_threats:
        print(f"[{threat.severity}] {threat.name} → {threat.mitigation}")

if __name__ == "__main__":
    import sys
    map_threats_to_model(sys.argv[1])