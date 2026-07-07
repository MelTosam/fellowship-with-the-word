def get_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60 and score <70:
        return "B"
    elif score >= 50 and score < 60:
        return "C"
    else:
        return "F"
    
print(get_grade(85))
print(get_grade(63))
print(get_grade(52))
print(get_grade(30))

