devotionals = ["joy", "justification", "grace", "righteousness", "predestination"]
def long_devotionals(devotionals):
    matching = []
    for devotional in devotionals:
        if len(devotional) > 5:
            matching.append(devotional)
    return matching
result = long_devotionals(devotionals)  
print(result)      