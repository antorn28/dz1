# перше завдання

class Animal:
    habitat = "Unknown"

    def __init__(self, name, legs, can_fly=False, can_swim=False, sound="Unknown"):
        self.name = name
        self.legs = legs
        self.can_fly = can_fly
        self.can_swim = can_swim
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    def move(self):
        if self.can_fly:
            print(f"{self.name} is flying.")
        elif self.can_swim:
            print(f"{self.name} is swimming.")
        else:
            print(f"{self.name} is walking.")

tiger = Animal(name="Tiger", legs=4, sound="Roar")
eagle = Animal(name="Eagle", legs=2, can_fly=True, sound="Screech")
fish = Animal(name="Fish", legs=0, can_swim=True, sound="Bubble")
snake = Animal(name="Snake", legs=0, sound="Hiss")
elephant = Animal(name="Elephant", legs=4, sound="Trumpet")

tiger.make_sound()
tiger.move()

eagle.make_sound()
eagle.move()

fish.make_sound()
fish.move()

snake.make_sound()
snake.move()

elephant.make_sound()
elephant.move()