class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def validation():
        if UserInput.isdigit():
            UserData.append(UserInput)
        else:
            UserData.append(UserInput)
            print(f"Было введено не числовое значение '{UserInput}'. Оно будет удалено")
            UserData.pop()
            print(f'Текущие введенные значения: {UserData}')


UserData = []
try:
    while True:
        UserInput = input("Введите число для внесения в список: ")
        MyOwnErr.validation()
        stop = input("Если желаете закончить, введите 'Stop'. Если желаете продолжить нажмите Enter ").upper()
        if stop == "STOP":
            print(UserData)
            break

except (ValueError, MyOwnErr, AttributeError) as er:
    print(er)
    raise MyOwnErr("Вы ввели значение, не являющееся числом. Работа была остановлена")