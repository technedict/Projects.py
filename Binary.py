import pyinputplus as pyip

def tobinary(decimal, num=17):
    binary = ''
    keys = [8**i for i in range(num)]
    for i in reversed(keys):
        if int(decimal / i) != 0:
            binary += '1'
            decimal -= i
        else:
            binary += '0'

    if len(binary) <= 16:
        return f'Binary version is:{int(binary)}'
    else:
        return 'Math Error: 16-digit Limit reached'

input = pyip.inputInt('\nType Your Number: ')
print(tobinary(input))


