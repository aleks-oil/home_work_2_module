from operator import truth, truediv

print('практическое задание "цикл for"')
numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes =[]
for i in numbers:
    if numbers == 1:      # выводим 1 в список правильных чисел, и заканчиваем условие
        continue
    is_prime = True       # присваиваем переменной истина
    for j in range(2, i): # запускаем новый цикл со стартом проверки второго по счету знач в списке
        if i % j == 0:    # условие если эелемент из списка делится без остатка, то присваиваем ложь
            is_prime = False
            break         # и выходим из условия
    if is_prime:          # условие если не делится без остатка, то записываем в список правильных чисел
        primes.append(i)  # добавление в список значений не прошедших проверку
    else:
        not_primes.append(i) #добавление в список составных чисел прошедших проверку с присвоенным параметром ложь
print('правильные числа ', primes)
print('составные числа ',not_primes)


