print('практическое задание "Условная конструкция. Операторы if,elif,else"')
first = int(input('Введите первое целое число:', ))
second = int(input('Введите второе целое число:', ))
thrid = int(input('Введите третье целое число:', ))
if first == second and first == thrid:
    print(3)
elif first == second or first == thrid or second == thrid:
    print(2)
else:
    print(0)
