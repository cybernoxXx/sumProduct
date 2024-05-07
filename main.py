def calculateSum(numbers):

    sum = 0

    if len(numbers) == 0:
        return 0
    else:
        for element in numbers:
            sum = sum + element
    return sum

def calculateProduct(numbers):
    product = 1

    if len(numbers) == 0:
        return 1
    else:
        for element in numbers:
            product = product * element
    return product



assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840
