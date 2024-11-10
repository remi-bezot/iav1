import json

def export_training_statistics(stats):
    with open("exported_statistics.json", "w") as file:
        json.dump(stats, file, indent=4)
