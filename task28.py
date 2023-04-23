# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# подзадачи: вводим числа А и Б, функция число А увеличичвает на 1, а число Б паралелльно уменьшает
# выход 1: Б уменьшилось до 0
# выход 2: Б или А меньше 1 

def summa(A, B):
    if B > 0:
        A += 1
        B -= 1
        return summa(A, B)
    if B < 1 or A < 1: 
        return A + B
A = int(input("A = "))
B = int(input("B = "))
print(summa(A, B))