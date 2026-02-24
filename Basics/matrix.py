# Matrix creation using nested loops
m = []

for i in range(5):
    m.append([])
    for j in range(5):
        m[i].append(j)

print(m)

# List comprehension
m = [[j for j in range(5)] for i in range(5)]
print(m)