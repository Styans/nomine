from functools import reduce

numbers = input("Введите числа через пробел: ").split()

numbers = list(map(int, numbers))

even_numbers = filter(lambda x: x % 2 == 0, numbers)

squared_even_numbers = map(lambda x: x ** 2, even_numbers)

sum_of_squares = reduce(lambda acc, x: acc + x, squared_even_numbers, 0)

print("Сумма квадратов четных чисел:", sum_of_squares)
