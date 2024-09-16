list_1 = []
list_2 = []
summary = 0

for i in range(1, 1000, 2):
    list_1.append(i**3)

for ind, val in enumerate(list_1):
    total = 0
    while val > 0:
        total += val % 10
        val //=10
    if total % 7 ==0:
        summary += list_1[ind]

print(summary)


for m in list_1:
    list_2.append(m * 17)

summary = 0

for ind, val in enumerate(list_2):
    total = 0
    while val > 0:
        total += val % 10
        val //= 10
    if total % 7 == 0:
        summary += list_2[ind]


print(summary)