#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, years: int) -> None:
        self.name = name.capitalize()
        if height >= 0:
            self._height = height
        else:
            print(
                f"{self.name}:",
                "Error, height can't be negative",
                "setting height at default value of 0"
            )
            self._height = 0
        if years >= 0:
            self._years = years
        else:
            print(
                f"{self.name}:",
                "Error, age can't be negative",
                "setting age at default value of 0"
            )
            self._years = 0

    def show(self) -> None:
        print(
            f"{self.name}:",
            f"{round(self._height, 1)}cm,",
            f"{self._years} days old"
        )

    def grow(self, grow: float) -> None:
        self._height += grow

    def age(self, age: int) -> None:
        self._years += age

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            print(
                f"{self.name}:",
                "Error, height can't be negative"
            )
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._years = age
        else:
            print(
                f"{self.name}:",
                "Error, age can't be negative"
            )
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._years


class Flower(Plant):

    def __init__(self, name: str, height: float, years: int,
                 color: str) -> None:
        super().__init__(name, height, years)
        self.color = color
        self.bloomed = 0

    def show(self):
        super().show()
        print(f"Color: {self.color.casefold()}")
        if self.bloomed == 0:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.bloomed = 1


class Tree(Plant):
    def __init__(self, name: str, height: float, years: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, years)
        self.trunk_diameter = trunk_diameter
        self.shade = 0

    def show(self):
        super().show()
        print(f"Color: {self.color.casefold()}")
        if self.shade == 0:
            print(
                f"Tree {self.name} now produces a shades of",
                f"{self._height}cm long and {self.trunk_diameter}cm wide."
            )
        else:
            print(f"{self.name} is blooming beautifully!")
    
    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        self.shade = 1


class Vegetable(Plant):
    def __init__(self, name: str, height: float, years: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, years)
        self.harvest_season = harvest_season


if __name__ == "__main__":
    flower = Flower("Rose", 15, 10, "Red")
    flower = Tree("Rose", 200, 365, "Red")
    flower = Vegetable("Rose", 5, 10, "Red")
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower.show()
    flower.bloom()
    flower.show()
    print()
    print("=== Tree")
