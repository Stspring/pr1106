# Ручное тестирование.

import math

def root(a,b):
    return math.sqrt((a-b)**3/(a+b)**2)
try:
    result = root(0.2,0.1)
    print(result)
   
except(ZeroDivisionError):
    print('Деление на ноль')

except(TypeError):
    print('Ошибка типов данных')

except(ValueError):
    print('Извлечение корня из отрицательного числа')

except Exception as e:
    print(f'Тип ошибки: {e}') 

"""
1. 2 положительных числа не одинаковых на вход (+)
2. 2 нуля (+)
3. 2 положительных одинаковых (+) 
4. 2 отрицательных одинаковых (+)
5. 2 отрицательных не одинаковых (+)
6. 1 положительное, 2 отрицательное (+)
7. 1 равное нулю, 2 не равное нулю (+)
8. Ввести текст (+)
9. 2 дробных числа (+)
10. 2 типа данных (+)
11. пустой ввод (+)

"""