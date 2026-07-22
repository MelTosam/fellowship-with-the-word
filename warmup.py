words = ["prayer", "faith", "go", "sanctification", "love", "word"]

def filter_by_length(words, minimum):
    result = []
    for word in words:
        if len(word) > minimum:
            result.append(word)
    return result 
result = filter_by_length(words, 5)
print(result)

def find_longest(words):
    winner = words[0]
    for word in words:
        if len(word) > len(winner):
            winner = word
    return winner

print(find_longest(words))       