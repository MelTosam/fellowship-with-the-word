sermons = [
    {"title": "The nature of God",
     "description": "We have received a nature that is incorruptible",
      "date": "29-06-2026"},

      {"title": "Righteousness by faith",
       "description": "We have become the righteousness of God in Christ",
       "date": "24-06-2026"},

       {"title": "Faith and works",
        "description": "true faith produces works that glorify Christ",
        "date": "22-06-2026"}
]
def sermons_keyword(sermons, keyword):
    result = []
    for sermon in sermons:
        if keyword.lower() in sermon["title"].lower() or keyword.lower() in sermon["description"].lower():
            result.append(sermon)
    return result

result = sermons_keyword(sermons, "God")
for sermon in result:
    print("title:", sermon["title"])
    print("description:", sermon["description"])
    print("---")              