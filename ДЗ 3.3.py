def thesaurus(*args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter in names_dict:
            names_dict[letter] += [i]
        else:
            names_dict[letter] = [i]
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Андрей", "Игорь", "Анна", "Мария", "Алексей", "Евгений", "Прохор"))