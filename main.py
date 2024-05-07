def calculateSum(numbers):
    # Using result and not sum because sum is already a function in python
    result = 0

    if len(numbers) == 0:
        return 0
    else:
        for element in numbers:
            result = result + element
    return result

def calculateProduct(numbers):
    # Product is not a function in python
    result = 1

    if len(numbers) == 0:
        return 1
    else:
        for element in numbers:
            result = result * element
    return result



assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840
