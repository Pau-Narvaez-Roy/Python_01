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

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color.casefold()}")
        if self.bloomed == 0:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.bloomed = 1
        self.show()
        print(f" {self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, years: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, years)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shades of",
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(self, name: str, height: float, years: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, years)
        self.harvest_season = harvest_season.capitalize()
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self, grow: float) -> None:
        super().grow(grow)
        print(f"[make {self.name.casefold()} grow for {round(grow, 1)}cm]")
        self.nutritional_value += int(grow)
        self.show()

    def age(self, age: int) -> None:
        super().age(age)
        print(f"[make {self.name.casefold()} age for {age} days]")
        self.nutritional_value += age
        self.show()

    def grow_and_age(self, grow: float, age: int) -> None:
        super().grow(grow)
        super().age(age)
        print(
            f"[make {self.name.casefold()}",
            f"grow for {round(grow, 1)}cm",
            f"and age for {age} days]"
        )
        self.nutritional_value += int(grow)
        self.nutritional_value += age
        self.show()


if __name__ == "__main__":
    flower = Flower("Rose", 15, 10, "Red")
    tree = Tree("Oak", 200, 365, 5.0)
    vegetable = Vegetable("Tomato", 5, 10, "April", 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower.show()
    flower.bloom()
    print()
    print("=== Tree")
    tree.show()
    tree.produce_shade()
    print()
    print("=== Vegetable")
    vegetable.show()
    vegetable.grow(3)
    vegetable.age(5)
    vegetable.grow_and_age(5, 3)
