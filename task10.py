# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

num = int(input("Enter the number of coins: "))
heads = 0
tails = 0

while (heads + tails) < num:
    a = int(input("Heads or tails (0 or 1): "))
    if a != 0 and a != 1:
        print("wrong enter!")
    else:
        if a == 0:
            heads += 1
        if a == 1:
            tails += 1

print(f"Heads: {heads}, Tails: {tails}")

if heads < tails:
    mini = heads
else:
    mini = tails

print(f"Need to flip {mini} coins")
