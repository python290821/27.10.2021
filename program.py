
def print_cinema():
    print('    ', end='')
    for i in range(len(_seats[0])):
        print (i,end='   ')
    print()
    for i in range(len(_seats)):
        print(f'{i}: ', end='')
        for j in range(len(_seats[i])):
            print(f'{{{_seats[i][j]}}}', end=' ')
        print()

def validate_row_col(_lst):
    if len(_lst) != 2 or _lst[0].isdigit() == False \
            or _lst[1].isdigit() == False:
        print('illegal')
        return False

    r = int(_lst[0])
    c = int(_lst[1])

    if r >= 0 and c >= 0 and r <= _rows and c <= _columns:
        if _seats[r][c] == 0:
            return True
        else:
            print('seat occupied, try again')
            return False
    else:
        print('illegal seat number')
        return False


def main():
    print('welcome to theater designer')
    _rows = int(input('how many rows? '))
    _columns = int(input('how many seats in each row? '))
    _seats = []

    for i in range(_rows):
        one_row = []
        for j in range(_columns):
            one_row.append(0)
        _seats.append(one_row)

    for counter in range(_rows * _columns):
        while True:
            print_cinema()
            _lst = input(('please enter row and columns (with space): ')).split()
            if validate_row_col(_lst):
                break
        r = int(_lst[0])
        c = int(_lst[1])
        _seats[r][c] = 1

main()