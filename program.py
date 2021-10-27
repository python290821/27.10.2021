

#          0         1       len: 2
#_l1 = [ [1,2,3,4], [5,6,7] ]
#for i in range(len(_l1)):
#    for j in range(len(_l1[i])):
#        print(_l1[i][j])

# rows = 3
# columns = 3
print('welcome to theater designer')
_rows = int(input('how many rows? ')) #3
_columns = int(input('how many seats in each row? '))
_seats = [ ]


for i in range(_rows):
    one_row = []
    for j in range(_columns):
        one_row.append(0)
    _seats.append(one_row)

for i in range(len(_seats)):
    for j in range(len(_seats[i])):
        print(f'{{{_seats[i][j]}}}', end=' ')
    print()

# purchase tickets
# ask for row, ask for column
# 1: 0, 0
# 2: 0,0 --- NO! occupied!




