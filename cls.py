class Person:
	numberOfPeople = 0

	def __init__(self, name):
		self.name = name
		Person.addPeople()
		#Person.numberOfPeople += 1

	@classmethod
	def getNumOfPeople(cls):
		return cls.numberOfPeople

	@classmethod
	def addPeople(cls):
		cls.numberOfPeople += 1

class Math:

	@staticmethod
	def add5(x):
		return x + 5

p1 = Person("Tim")
p2 = Person("Jill")
print(Person.getNumOfPeople())

print(Math.add5(5))
