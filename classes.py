class person:
    def __init__(self,name,age,height,address,is_married):
        self.name = name
        self.age = age
        self.height = height
        self.address = address
        self.is_married = is_married

    def greet(self):
        return f"Hi my name is {self.name}"
        
person1=person("allan",22,"169cm","githu45",True)
person2=person("ken",21,"196cm","githu44",True)
print(person)
print(person1.name)
print(type(person1))

print(person1.greet())
print(person2.greet())