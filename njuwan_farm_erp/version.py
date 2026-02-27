import json
from datetime import datetime

STATE_FILE = "project_state.json"

def increment_version():
    try:
        with open(STATE_FILE, "r") as f:
            state = json.load(f)
    except:
        state = {
            "version": "1.0.0",
            "last_updated": str(datetime.now()),
            "modules_completed": []
        }

    major, minor, patch = map(int, state["version"].split("."))

    # Increment patch version
    patch += 1

    state["version"] = f"{major}.{minor}.{patch}"
    state["last_updated"] = str(datetime.now())

    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

    return state["version"]