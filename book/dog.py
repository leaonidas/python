class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " in now sitting.")

    def roll(self):
        print(self.name.title() + " rolls over!")


if __name__ == '__main__':
    valentim = Dog("Valentim", "1")
    print(valentim.name)
    valentim.sit()
