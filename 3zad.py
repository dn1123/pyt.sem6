#Задача: предложить улучшения кода(3-5задач) для уже решённых задач.
#С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


input_num = int(input('Введите число:'))
List = lambda a, b:  a * b
factorial = 1
for i in range(input_num):
    i += 1
    factorial = List(factorial, i)
    print(factorial, end=' ')