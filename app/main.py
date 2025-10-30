class Animal():
    alive = []
    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        Animal.alive.append(self)


class Carnivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.carnivore = True

    def bite(self, prey):
        if prey.herbivore == True and prey.hidden == False:
            prey.health -= 50
        if prey.health <= 0:
            prey.die()


class Herbivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.hidden = False
        self.herbivore = True

    def hide(self):
        if self.hidden == True:
             self.hidden = False
        else:
            self.hidden = True

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)




