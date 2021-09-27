n = int(input("Введите число: "))
numbers_gen = (num for num in range(1, n + 1, 2))

for i in numbers_gen:
    print(i)