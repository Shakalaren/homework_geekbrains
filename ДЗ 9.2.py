
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profut(self, weight = 25, thickness = 5):
        return f'{self._length} м * {self._width} м * {weight} кг * {thickness} см = '\
               f'{int(self._length * self._width * weight * thickness) / 1000} т'

road_1 = Road(5000, 20)
print(road_1.get_full_profut())