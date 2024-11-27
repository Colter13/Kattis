class Dog:
    # Class Attribute
    species = "canis familiaris"

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Another Instance Method
    def speak(self, sound):
        return f"{self.name} says {sound}"

my_dog = Dog("Rex", 5)
print(my_dog.description())
print(my_dog.speak("Woof"))
