num_1 = input()
num_2 = input()
operator = input()

try:
    if num_1.isdigit() and num_2.isdigit() and num_1 != '0' and num_2 != '0' and operator in ('+', '-', '*', '/'):
        num_1 = int(num_1)
        num_2 = int(num_2)

        if operator == '+':
            res = num_1 + num_2
        elif operator == '-':
            res = num_1 - num_2
        elif operator == '*':
            res = num_1 * num_2
        elif operator == '/':
            if num_2 != 0:
                    res = num_1 / num_2
            else:
                raise ValueError
            
        print(res)
    else:
        raise ValueError
except ValueError:
    print('Некорректный ввод')