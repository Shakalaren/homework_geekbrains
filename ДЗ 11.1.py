class Date:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def get_date(cls, date):
        my_date = []
        for i in date.split():
            if i != '-':
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            print("День в порядке")
        else:
            print("Неправильный день")
        if 1 <= month <= 12:
            print("Месяц в порядке")
        else:
            print("Неправильный месяц")
        if year >= 1900:
            print("Год в порядке")
        else:
            print("Неправильный год")


result = Date
print(Date.get_date("13 - 06 - 1998"))
print(Date.validation(13, 6, 1998))