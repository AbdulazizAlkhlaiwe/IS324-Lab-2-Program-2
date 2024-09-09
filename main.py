table = [['A', 'B' , 'C'], ['D', 'E' , 'F']]
for row in table:
    print(row[:2])
transpose = [[0, 0] for z in range(3)]
for i in range(2):
    for j in range(3):
        transpose[j][i] = table[i][j]
print(transpose)
