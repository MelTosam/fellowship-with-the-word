numbers = [12, 5, 28, 3, 45, 17, 19]

def filter_above(numbers, minimum):
    result = []
    for number in numbers:
        if number > minimum:
            result.append(number)
    return result
result = filter_above(numbers, 10)
print(result)

def find_highest(numbers):
    winner = numbers[0]
    for number in numbers:
        if number > winner:
            winner = number
    return winner

winner = find_highest(numbers)
print(winner)  

def find_lowest_above(numbers, minimum):
    lowest = []
    for number in numbers:
        if number > minimum:
            lowest.append(number)
    return lowest
lowest = find_lowest_above(numbers)
print(lowest)          