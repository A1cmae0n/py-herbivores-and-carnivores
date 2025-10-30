class Animal():
    alive: list["Animal"] = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> list:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Carnivore(Animal):
    def bite(self, prey: Animal) -> None:
        if isinstance(prey, Herbivore) and prey.hidden is False:
            prey.health -= 50
        if prey.health <= 0:
            prey.die()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden
