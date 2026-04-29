import json

FILE = "leaderboard.json"

def save_score(score):
    try:
        with open(FILE) as f:
            data = json.load(f)
    except:
        data = []

    # автоматты username (input жоқ!)
    name = "Player"

    data.append({"name": name, "score": score})
    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)