import random
print('дополнительное практическое задание по 2 модулю')
n = random.randint(3,20) #случайное первое число
def get_pasword(number):
    password = ''
    for i in range (1,number):
        for j in range (2,number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password
result = get_pasword(n)
print('Пароль: ',n,'-', result)