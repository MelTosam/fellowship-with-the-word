devotional = {"title": "Putting on Christ", "date": "01-08-2026"}

def describe_devotional(devotional):
    return f"title: {devotional["title"]} | date: {devotional["date"]}"
print(describe_devotional(devotional))