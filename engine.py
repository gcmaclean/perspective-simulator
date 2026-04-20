from classifier import classify
from reframe_engine import generate_response
from mood_tracker import MoodTracker
from utils.file_handler import save_entry, load_history, clear_file

tracker = MoodTracker()

def run_analysis(text):
    category = classify(text)
    result = generate_response(text, category)

    mood_change = result["new_mood"] - result["old_mood"]
    tracker.update(mood_change)

    entry = {
        "input": text,
        "category": category,
        "reframe": result["reframe"],
        "actions": result["actions"],
        "mood_change": mood_change
    }

    save_entry(entry)

    print("\n--- ANALYSIS ---")
    print("Category:", category)
    print("Reframe:", result["reframe"])
    print("Actions:")
    for a in result["actions"]:
        print("-", a)
    print("Mood Change:", mood_change)


def view_history():
    history = load_history()

    print("\n--- HISTORY ---")
    for item in history[-10:]:
        print(item)


def clear_history():
    clear_file()
    print("History cleared.")