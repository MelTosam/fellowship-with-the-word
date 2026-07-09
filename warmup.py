def highest_score(scores):
    winner = scores[0]
    for score in scores:
        if score > winner:
            winner = score
    return winner    
scores =[45, 89, 23, 67, 91, 34, 78]
print(highest_score(scores))
