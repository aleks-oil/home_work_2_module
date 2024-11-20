from operator import index
from typing import List, Any

print('практическое задание "цикл while"')
my_list: list[int | Any] = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
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
