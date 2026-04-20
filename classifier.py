def classify(text):
    text = text.lower()

    categories = {
        "Academic": ["exam", "test", "school", "grade"],
        "Career": ["job", "interview", "work"],
        "Social": ["friend", "relationship", "people"]
    }

    for category, keywords in categories.items():
        for word in keywords:
            if word in text:
                return category

    return "General"