print('практическое задание "цикл while"')
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
        if my_list[a] > 0:
         print(my_list[a])
         a += 1
         continue
        elif my_list[a] ==0:
         pass
         a += 1
        elif my_list[a] < 0:
         break
print('проверка универсальности кода')
my_list = [42, 69, 322, 13, 0, 99, 0, 1, -5, 9, 8, 7, -6, 5]
print(my_list, 'код работает при встрече нескольких нулей в списке')
b = 0
while b < len(my_list):
        if my_list[b] > 0:
         print(my_list[b])
         b += 1
         continue
        elif my_list[b] ==0:
         pass
         b += 1
        elif my_list[b] < 0:
         break