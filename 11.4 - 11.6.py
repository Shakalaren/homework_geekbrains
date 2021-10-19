class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def validation():
        if PrintInput.isalpha() or ScannerInput.isalpha() or XeroxInput.isalpha():
            raise MyOwnErr("Введены неправильные числовые данные, работа останавливается")
        else:
            pass


class Storage:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.name, []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

    @property
    def dict(self):
        return self._dict


class Equipment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'{self.value}'


class Printer(Equipment):
    def __init__(self, name, value):
        super().__init__(name, value)
        self.value = value


class Scanner(Equipment):
    def __init__(self, name, value):
        super().__init__(name, value)
        self.value = value


class Xerox(Equipment):
    def __init__(self, name, value):
        super().__init__(name, value)
        self.value = value


try:
    PrintInput = input("Введите число принтеров: ")
    ScannerInput = input("Введите число сканнеров: ")
    XeroxInput = input("Введите число ксероксов: ")
    st = Storage()
    scanner = Scanner('Сканнеры', PrintInput)
    st.add_to(scanner)
    printer = Printer('Принтеры', ScannerInput)
    st.add_to(printer)
    xerox = Xerox('Ксероксы', XeroxInput)
    st.add_to(xerox)
    print(st.dict)
    MyOwnErr.validation()
    print(st.dict)
    st.extract('Принтеры')
    print(st.dict)
except(MyOwnErr, AttributeError) as er:
    print(er)