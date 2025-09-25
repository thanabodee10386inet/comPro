class dog:
    species = 'mammal'  # class attribute
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

dog1 = dog("Philo", 5)
dog2 = dog("Mikey", 6)

print("{} is {} and {} is {}"
.format(dog1.name, dog1.age, dog2.name, dog2.age))

if dog1.species == "mammal":
    print("{} is a {}".format(dog1.name, dog1.species))