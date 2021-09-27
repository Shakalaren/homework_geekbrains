numbers_gen = (num for num in range(1, 100) if num % 2 != 0)

for i in numbers_gen:
    print(i)