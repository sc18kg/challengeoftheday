x = input("Please enter the starting range number: ")
y = input("Please enter the end range number: ")
200
range1 = int(x)
range2 = int(y)

def alleven(number):
    num_str = str(number)
    digit_bool = []
    for digit in num_str:
        if int(digit) % 2 == 0:
            digit_bool.append(True)
        else:
            digit_bool.append(False)
    return digit_bool

mylist = [i for i in range(range1, range2) if all(alleven(i))]
print(','.join([str(i) for i in mylist]))