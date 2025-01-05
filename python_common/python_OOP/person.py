class Person():
    """Person model"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Hello, I'm {} and I'm {} years old".format(self.name, self.age))

    def sing(self):
        """Sings a song"""
        print(self.name + " is singing.")   

    def dance(self):
        """Dances a song"""
        print(self.name + " is dancing.")

man = Person("Ivan", 25)       
woman = Person("Elena", 23) 
woman.sing()
