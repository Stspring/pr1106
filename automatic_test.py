# Автоматическое тестирование
import math
import unittest


def root(a,b):
    return math.sqrt((a-b)**3/(a+b)**2)

def heand(a,b):
    try:
        result = root(a,b)
        print(result)
    
    except(ZeroDivisionError):
        result = 'Деление на ноль'
        print('Деление на ноль')
    except(TypeError):
        result = 'Ошибка типов данных'
        print('Ошибка типов данных')
    except(ValueError):
       result = 'Извлечение корня из отрицательного числа'
       print('Извлечение корня из отрицательного числа')
    except Exception as e:
        result = 'Тип ошибки: {e}'
        print(f'Тип ошибки: {e}') 
    return result


class Test_root(unittest.TestCase):

    def test_dif_pos_int(self):
        self.assertEqual(heand(1,2),'Извлечение корня из отрицательного числа')
        self.assertEqual(heand(2,1), 0.3333333333333333)
    
    def test_two_zero(self):
        self.assertEqual(heand(0,0),'Деление на ноль')

    def test_int_equal(self):
        self.assertEqual(heand(1,1), 0.0)
        self.assertEqual(heand(-1,-1), 0.0)

    def test_dif_neg_int(self):
        self.assertEqual(heand(-1,-2), 0.3333333333333333)
        self.assertEqual(heand(-2,-1), 'Извлечение корня из отрицательного числа')

    def teat_one_neg_one_pos(self):
        self.assertEqual(heand(-1,2),'Извлечение корня из отрицательного числа')
        self.assertEqual(heand(1,-2),5.196152422706632)

    def test_one_zero(self):
        self.assertEqual(heand(-1,0),'Извлечение корня из отрицательного числа')
        self.assertEqual(heand(1,0),1.0)
        self.assertEqual(heand(0,1),'Извлечение корня из отрицательного числа')
    
    def test_str(self):
        self.assertEqual(heand("a",0),'Ошибка типов данных')

    def test_zero_input(self):
        self.assertEqual(heand("",0),'Ошибка типов данных')
    
    def test_two_float(self):
        self.assertEqual(heand(0.1,0.1),0.0)
        self.assertEqual(heand(0.1,-0.1),'Деление на ноль')
        self.assertEqual(heand(-0.1,0.1),'Деление на ноль')
        self.assertEqual(heand(0.1,0.2),'Извлечение корня из отрицательного числа')
        self.assertEqual(heand(0.2,0.1),0.10540925533894598)
    
    def test_two_type(self):
        self.assertEqual(heand(0.1,1),'Извлечение корня из отрицательного числа')

if __name__== "__main__":
    unittest.main()