class Parrot:


 species = "bird"


 def __init__(self, name, age):
         self.name = name
         self.age = age


Bluey = Parrot ("Bluey", 9)
Bingo = Parrot ("Bingo", 7)
print("Bluey is a {}".format(Bluey.species))
print("Bingo is also a {}".format(Bluey.species))


print("Bluey is {} years old".format(Bluey.age))
print("Bingo is younger, being {} years old".format(Bingo.age)) 
