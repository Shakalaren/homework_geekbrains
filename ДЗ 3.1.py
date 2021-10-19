words = {"one": "один",
         "один": "one",
         "two": "два",
         "два": "two",
         "three": "три",
         "три": "three",
         "four": "четыре",
         "четыре": "four",
         "five": "пять",
         "пять": "five",
         "six": "шесть",
         "шесть": "six",
         "seven": "семь",
         "семь": "seven",
         "eight": "восемь",
         "восемь": "eight",
         "nine": "девять",
         "девять": "nine",
         "ten": "десять",
         "десять": "ten"}

user_input = input("введите число буквами: ")


def num_translate():
    print(f' Ваше слово переводится, как: {words.get(user_input.lower())}')


num_translate()