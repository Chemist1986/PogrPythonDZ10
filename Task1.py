class Animal:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print("Я -", self.name)

    @staticmethod
    def create_animal(animal_type, **kwargs):
        if animal_type == "Mammal":
            return Mammal(**kwargs)
        elif animal_type == "Bird":
            return Bird(**kwargs)
        elif animal_type == "Reptile":
            return Reptile(**kwargs)
        else:
            raise ValueError("Unsupported animal type.")

class Mammal(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def can_fly_or_not(self):
        if self.can_fly:
            print("Я могу летать!")
        else:
            print("Я не умею летать.")

class Reptile(Animal):
    def __init__(self, name, num_of_legs):
        super().__init__(name)
        self.num_of_legs = num_of_legs

    def show_legs(self):
        print("У меня", self.num_of_legs, "ноги.")


animal1 = Animal.create_animal("Mammal", name="Лев", sound="Ррррр!")
animal2 = Animal.create_animal("Bird", name="Орел", can_fly=True)
animal3 = Animal.create_animal("Reptile", name="Крокодил", num_of_legs=4)

animal1.show_info()
animal1.make_sound()

animal2.show_info()
animal2.can_fly_or_not()

animal3.show_info()
animal3.show_legs()