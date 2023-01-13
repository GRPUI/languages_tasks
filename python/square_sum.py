"""
Завершите функцию квадратной суммы так, чтобы она возводила в квадрат каждое переданное в нее число, а затем суммировала результаты вместе.

Например, для [1, 2, 2] он должен возвращать 9, потому что 1^2 + 2^2 + 2^2 = 9.
"""

def square_sum_simple(numbers):
	res = 0
	for num in numbers:
   		res = res + num*num
	return res


def square_sum_advanced(numbers):
    return sum(list(map(lambda x: x ** 2, numbers)))
  
print(square_sum_simple([0, 3, 4, 5]))
#ожидаемый результат: 50
print(square_sum_advanced([-1,0,1]))
#ожидаемый результат: 2
