class employee(object):
    def __init__(self):
        self.__name = 'Peter'
        self.__age = 45
        self.__salary = 35000

object1 = employee()
print(object1.name)
print(object1.age)
print(object1.salary)