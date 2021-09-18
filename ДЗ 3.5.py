from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
user_input = int(input("введите количество шуток: "))


def get_jokes(*args, repeat=False):
    """Код функции закомментирован, как требовалось в задании, задание выполнено с использованием user_input"""
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    list_of_j = []
    list_min = min(no, adv, adj)
    i = 0
    while i != user_input and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            list_of_j.append(f'{no.pop(num)} {adv.pop(num)} {adj.pop(num)}')
        else:
            list_of_j.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        i = i + 1
    return list_of_j


print(get_jokes(user_input))
