devotionals = [
    {"title": "Righteousness",
    "verse": "Romans 5:17",
    "explanation": "We have become Gods righteousness in christ",
    "date": "25-06-2026"},

    {"title": "The nature of God",
     "verse": "James 1:17",
     "explanation": "The character of God is seen in Christ",
     "date": "24-05-2026"
     },

     {"title": "Justification",
      "verse": "romans 3:9",
      "explanation": "We have been justified by grace through faith",
      "date": "23-06-2026"}
      ]

today = "25-06-2026"
def todays_devotional(devotional, date):
    for devotional in devotionals:
        if (devotional["date"]) == today:
           return devotional 
    return None

result = todays_devotional(devotionals, today)
print("title:", result["title"])
print("verse:", result["verse"])
print("explanation:", result["explanation"])
print("date:", result["date"])
