sermons = [
    {"title": "The nature of God",
     "description": "We have received a nature that is incorruptible",
      "date": "29-06-2026"},

      {"title": "Righteousness by faith",
       "description": "We have become the righteousness of God in Christ",
       "date": "30-06-2026"},

       {"title": "Faith and works",
        "description": "true faith produces works that glorify Christ",
        "date": "22-06-2026"}
]

def latest_sermon(sermons):
    latest = sermons[0]
    for sermon in sermons:
        if sermon["date"] > latest["date"]:
            latest = sermon
    return latest    
result = latest_sermon(sermons)
print("title:", result["title"])
print("description:", result["description"])
print("date:", result["date"])

            