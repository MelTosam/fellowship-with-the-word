def classify_number(number):
    if number == 0:
        return "zero"
    elif number % 2:
        return "even"
    else:
        return "odd"

print(classify_number(0))   
print(classify_number(5))
print(classify_number(8))