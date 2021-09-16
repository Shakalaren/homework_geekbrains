prices = [57.8, 46.51, 97, 120, 256, 753, 136, 275, 48.15, 345.99]

for i in prices:
    rub, kop = int(i // 1), int(f"{i % 1:.02f}"[2:])
    print(f"{rub} руб {kop:02d} коп, ")