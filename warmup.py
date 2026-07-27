numbers = [3, 17, 2, 45, 8, 31, 6]

def filter_above(numbers, minimum):
    result = []
    for number in numbers:
        if number > minimum:
            result.append(number)
    return result
result = filter_above(numbers, 2)
print(result)

def find_highest(numbers):
    winner = numbers[0]
    for number in numbers:
        if number > winner:
            winner = number 
    return winner 

print(find_highest(numbers))        



