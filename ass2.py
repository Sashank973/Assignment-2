def find_duplicates(arr):
    frequency = {}
    duplicates = []

    
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    
    for num, count in frequency.items():
        if count == 2:
            duplicates.append(num)

    return duplicates


my_array = [1, 2, 3, 4, 4, 5, 6, 7, 7]
result = find_duplicates(my_array)
print(result)
