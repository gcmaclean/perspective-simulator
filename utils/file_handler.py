def save_entry(entry):
    with open("data/history.txt", "a") as file:
        file.write(str(entry) + "\n")


def load_history():
    try:
        with open("data/history.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def clear_file():
    open("data/history.txt", "w").close()