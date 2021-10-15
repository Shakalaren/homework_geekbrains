from random import choice


class Car:
    direction = ['north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest']

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'New car: {n} has a color: {c}.\nIs the car a police car? {p}')

    def go(self):
        print(f'{self.name}: Car went')

    def stop(self):
        print(f'{self.name}: Car stopped')

    def turn(self):
        print(f'{self.name}: Car turned {choice(self.direction)}')

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}.speeding!' if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed} speeding!' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """ничего не сказано"""


class PoliceCar(Car):
    def __init__(self, n, c, s, p=True):
        super().__init__(n, c, s, p)


police_car = PoliceCar('"Полицейская"', 'белый', 80)
work_car = WorkCar('"Грузовик', "хаки", 40)
sport_car = SportCar('"Спортивная', 'красный', 120)
town_car = TownCar('"Городская', 'желтый', 65)

list_of_cars = [police_car, work_car, sport_car, town_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()