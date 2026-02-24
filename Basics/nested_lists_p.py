matrix = [[1, 2, 3],
         [4, 5, 6], 
         [7, 8, 9]]
#Print element at row 2, column 3
print(matrix[1][2])
#Loop through entire matrix and print each element
for row in matrix:
    for element in row:
        print(element) 

#Print column sum
col_sum = 0
for row in matrix:
    col_sum += row[1]

print("Column sum:", col_sum)

#Print sum for all columns
cols = len(matrix[0])

for col in range(cols):
    col_sum = 0
    for row in matrix:
        col_sum += row[col]
    print(f"Sum of column {col}: {col_sum}")

#print matrix column-wise
cols = len(matrix[0])
for col in range(cols):
    column = [row[col] for row in matrix]
    print(f"Column {col}: {column}")