for persents in range(101):
    if persents % 10 == 1 and persents % 100 != 11:
        print(persents, "процент,")
    elif 1 < persents % 10 < 5 and not 11 < persents % 100 < 15:
        print(persents, "процента,")
    else:
        print(persents, "процентов,")