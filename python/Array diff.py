"""
Ваша цель в этом задании - реализовать функцию разности, которая вычитает один список из другого и возвращает результат.

Он должен удалить все значения из списка a, которые присутствуют в списке b, сохраняя их порядок.
array_diff([1,2],[1]) == [2]

Если значение присутствует в b, все его вхождения должны быть удалены из другого:
array_diff([1,2,2,2,3],[2]) == [1,3]
"""

def array_diff_simple(a, b):
    for item in b:
        if item in a:
            for count in range(a.count(item)):
                a.remove(item)
    return a
"""
В этой функции мы используем цикл. Мы будем перебирать список b.
item - элемент списка. В условии 'if item in a' мы проверяем, есть ли в списке a item, который является элементом списка b.
Если условие выполняется, то есть item есть в обоих списках - создаётся цикл, который будет выполняться столько, сколько раз item повторяется в списке a 'a.count(item)'.
Затем первый item удаляется из списка a 'a.remove(item)'. Возможно, что в списке будут несколько повторений, а remove удаляется лишь первое вхождение в списке, для этого необходим цикл.
И после прохождения по циклу b возвращаем получившийся список a 'return a'.
"""


def array_diff_advanced(a, b):
    return list(filter(lambda x: x not in b, a))
"""
Здесь мы используем функцию filter(). По названию можно понять, что она необходима для фильтрации.
Фунция filter() принимает аргументы function, iterable соотвественно. В данном случае используется используется анонимная(lambda) функция и список.
Список переданный в качестве аргумента - то, что нужно отфильтровать.
lambda x: x not in b проверяет, что каждый элемент итерируемого объекта(iterable), в этом случае списка НЕ находится в списке b.
Если результат положительный, то элемент остаётся. Если условие не выполняется, то элемент убирается.
В качестве выходных данных, функция filter возвращает объект filter. Чтобы получить список, необходимо передать результат функции filter() в функцию list() как аргумент.
И наконец возвращаем результат работы функции array_diff_advanced(a, b) используя return.
"""
    
if __name__ == "__main__":
    print(array_diff_simple([-17, 0], [-13, 0, 12, 0, -17, 6, -8, 15]))
  #ожидаемый вывод: []
    print(array_diff_advanced([-17, 0, 8], [-13, 0, 12, 0, -17, 6, -8, 15]))
  #ожидаемый вывод: [8]
  
"""
Сначала идёт проверка на то, что файл запущен прямо(не импортирован) 'if __name__ == "__main__":'. Затем мы передаём аргументы в функцию array_diff().
"""
  