
################################ question 6 (daf)
full_name = input()
print('hi')
print(full_name[-5:]) # five last character
print(full_name[:len(full_name) // 3]) # first third part
print(full_name[-1 * len(full_name) // 3:]) # last third part

################################ question 2
# '3 + 4 = 7'
#"5" + "5" == "55"
_targil = input('Please enter a targil: ')
list_targil = _targil.split()
print(list_targil)
num1 = float(list_targil[0])
sign = list_targil[1]
num2 = float(list_targil[2])
shave = list_targil[3] # redundent
result = float(list_targil[4])
# '3+4=7' => '3+4==7'
if sign == '+':
    print (result == num1 + num2)
elif sign == '-':
    #if result == num1 - num2:
    #    print(True)
    #else:
    #    print(False)
    # same
    print (result == num1 - num2)
elif sign == '*':
    print(result == num1 * num2)
elif sign == "/":
    print(result == num1 / num2)
else:
    print('unknown sign')
