def add_list(lst):
    total = 0
    for item in lst:
        if type(item) is int:
            total += item
        else:
            total += add_list(item)
    return total


numbers = [
    [1, 2, 3, 4],
    [3, 6, [5, 6], 8, 2, [2, 4], 9],
    [4, 2, [6, 7, [2, 6, 1]]]
]

print("The sum is", add_list(numbers))
