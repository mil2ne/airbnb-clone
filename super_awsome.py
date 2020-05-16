class Dog:
    def __init__(self):
        print("woof woof")

    def pee(self):
        print("i will pee")


class Puppy(Dog):
    def __init__(self):
        print("im tiny")
        super().__init__()


p = Puppy()
p
