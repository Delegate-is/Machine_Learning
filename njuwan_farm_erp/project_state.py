import json

STATE_FILE = "project_state.json"

def load_state():
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def update_state(key, value):
    state = load_state()
    state[key] = value
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)