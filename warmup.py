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

def devotional_keyword(devotionals, keyword):
    matching = []
    for devotional in devotionals:
        if keyword.lower() in devotional["title"].lower() or keyword.lower() in devotional["explanation"].lower():
            matching.append(devotional)
    return matching  
      
result = devotional_keyword(devotionals, "Christ")       
for devotional in result:
    print("title:", devotional["title"])
    print("explanation:", devotional["explanation"])
    print("---")




