class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hobbies = []

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)
