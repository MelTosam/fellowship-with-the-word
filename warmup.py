devotionals = [
    {"title": "Righteousness",
    "verse": "Romans 5:17",
    "explanation": "We have been made the rightness of God",
    "date": "22-06-2026"},

    {"title": "The nature of God",
     "verse": "James 1:17",
     "explanation": "God is light and his character is revealed in Christ",
     "date": "22-06-2026"}
    ]

def devotional_key_word(devotionals, keyword):
    matching = []
    for devotional in devotionals:
        if keyword in devotional["title"]:
            matching.append(devotional)
    return matching
        
result = devotional_key_word(devotionals, "God")   
for devotional in result:
    print("title:", devotional["title"])
    print("....")     
        




