class employee():
    def __init__(self):
        self.__maxearn = 30000

    def earn(self):
        print("earning is: {}".format(self.__maxearn))

    def setmaxearn(self, earam):
        self.__maxearn = earam

emp1 = employee()
emp1.earn()

emp1.__maxearn = 10000
emp1.earn()

emp1.setmaxearn(15000)
emp1.earn()
