numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
odd_numbers = []
# Filtering nested lists using nested loops

for sublist in numbers:
    for num in sublist:
        if num % 2 != 0:
            odd_numbers.append(num)

print(odd_numbers)

#Using list comprehension
m = [[1,2,3],[4,5,6],[7,8,9]]
odds = [e for r in m for e in r if e % 2 != 0]
print(odds)