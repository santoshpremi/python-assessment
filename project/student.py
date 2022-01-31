
class Student(object):
    def __init__(self, first_name, last_name, roll, age, major):
        self.first_name = first_name
        self.last_name = last_name
        self.roll = roll
        self.age = age
        self.major = major

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.get_full_name()} \t {self.roll} \t {self.age} \t {self.major}'
