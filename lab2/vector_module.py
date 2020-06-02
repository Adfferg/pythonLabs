from math import sqrt


class Vector:

    def __init__(self, massive):
        self.coordinates = massive

    def __add__(self, other):
        print(str(self.get_len()) + '\n' + str(other.get_len()))
        if self.get_len() == other.get_len():
            new_coordinates = []
            for value_1, value_2 in zip(self.coordinates, other.get_coordinates()):
                new_coordinates.append(value_1 + value_2)
            return Vector(new_coordinates)
        else:
            print("Different dimensions.")

    def __sub__(self, other):
        if self.get_len() == other.get_len():
            new_coordinates = []
            for value_1, value_2 in zip(self.coordinates, other.get_coordinates()):
                new_coordinates.append(value_1 - value_2)
            return Vector(new_coordinates)
        else:
            print("Different dimensions.")

    def __mul__(self, other):
        if self.get_len() == other.get_len():
            result = 0
            for value_1, value_2 in zip(self.coordinates, other.get_coordinates()):
                result += value_1 * value_2
            return result

    def __str__(self):
        return str(self.coordinates)

    def __eq__(self, other):
        if self.get_len() != other.get_len():
            return False
        for value_1, value_2 in zip(self.coordinates, other.get_coordinates()):
            if value_2 != value_1:
                return False
        return True

    def __getitem__(self, key: int):
        return self.coordinates[key]

    def get_length(self):
        result = 0
        for value in self.coordinates:
            result += value * value
        return sqrt(result)

    def mul_number(self, number):
        massive = []
        for i in self.coordinates:
            massive.append(number * i)
        return Vector(massive)

    def get_coordinates(self):
        return self.coordinates

    def get_len(self):
        return len(self.get_coordinates())

    def set_coordinates(self, massive):
        if len(self.coordinates) == len(massive):
            self.coordinates = massive
        else:
            print("Different dimensions.")
