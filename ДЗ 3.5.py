from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
user_input = int(input("введите количество шуток: "))


def get_jokes(*args):
    """i = 0
    while i != user_input:
        i = i + 1
        print(choice(nouns), choice(adverbs), choice(adjectives))"""


get_jokes(user_input)
