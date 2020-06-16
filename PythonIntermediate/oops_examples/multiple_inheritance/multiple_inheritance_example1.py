class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Student:
    def __init__(self,id):
        self.id = id

    def getId(self):
        return self.id


class Resident(Person, Student):
    def __init__(self,name,age,id):
        Person.__init__(self,name,age)
        Student.__init__(self,id)


resident = Resident("Vikas", 22, 1992)

print("Name of Resident: ", resident.getName())
print("Age of Resident: ", resident.getAge())
print("Id of Resident: ", resident.getId())