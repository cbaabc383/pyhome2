# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
# не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Enter N: "))
k = 0
degree = 1
while degree <= n:
    print (degree)  
    k += 1
    degree *= 2
