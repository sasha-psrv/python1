# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def chislo(n):
    if n==1 or n ==0:
        return 'непростое'
    for i in range(2, n):
        if n % i == 0:
            return 'непростое'
    return 'простое'    


print(chislo(5))
