# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите трехзачное число: '))
a = int(n//100)
b = int(n % 100//10)
c = int(n % 10)
print(a+b+c)