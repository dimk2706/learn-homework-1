"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def compare(st1, st2):
    if str(type(st1)) != "<class 'str'>" or str(type(st2)) != "<class 'str'>":
       return 0
    elif st1==st2:
       return 1
    elif len(st1) > len(st2):
       return 2
    elif st2 == "learn":
       return 3
      

def main():
    a = 2
    b = 1
    print(compare(a, b))
    a = "aaa"
    b = "aaa"
    print(compare(a, b))
    a = "aaaaaaaaaa"
    b = "bbbbb"
    print(compare(a, b))
    a = "aaa"
    b = "learn"
    print(compare(a, b))




  
    
if __name__ == "__main__":
    main()
