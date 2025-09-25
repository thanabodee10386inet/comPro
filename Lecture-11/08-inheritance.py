class Animal:
    def __init__(self, name):
        self.name = name
    
    def apeek(self):
        return "Some sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")

print(dog1.apeek())
print(dog1.speak())
