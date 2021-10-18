class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


Num1 = int(input("Введите число 1: "))
Num2 = int(input("Введите число 2: "))
UserInput = input("Введите +, -, * или / для совершения математического действия: ")

try:
    if UserInput == "+":
        print(f'Сумма {Num1} и {Num2} равняется {Num1 + Num2}')
    elif UserInput == "-":
        print(f'Разница {Num1} и {Num2} равняется {Num1 - Num2}')
    elif UserInput == "*":
        print(f'Произведение {Num1} и {Num2} равняется {Num1 * Num2}')
    elif Num2 == 0 and UserInput == "/":
        raise MyOwnErr("Делить на 0 не представляется возможным")
    elif UserInput == "/":
        print(f'Частное {Num1} и {Num2} равняется {Num1 / Num2}')
except (ZeroDivisionError, MyOwnErr) as er:
    print(er)