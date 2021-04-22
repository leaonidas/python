class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name + ' is a ' + self.cuisine_type + ' restaurant.')

    def open_restaurant(self):
        print(self.name + ' is now open!')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def print_flavors(self):
        print(self.name + ' has the following ice cream flavors:')
        for flavor in self.flavors:
            print(flavor.title())


if __name__ == '__main__':
    first_res = Restaurant('Dominos', 'fast food')
    first_res.describe_restaurant()
    second_res = Restaurant('Pregaria', 'sandwich')
    second_res.describe_restaurant()
    third_res = Restaurant('Marco Bellini', 'pizza')
    third_res.describe_restaurant()

    print(third_res.name + " has served " +
          str(third_res.number_served) + " people.")
    third_res.set_number_served(5)
    print(third_res.name + " has served " +
          str(third_res.number_served) + " people.")
    third_res.increment_number_served(5)
    print(third_res.name + " has served " +
          str(third_res.number_served) + " people.")

    sabores = IceCreamStand('Sabores', 'ice cream')
    sabores.print_flavors()
