#!/usr/bin/env python3

def show_stats(
        name: str, grow: int, age: int, show: int, shade: int, tree: bool
) -> None:
    print(
        f"[statistics for {name}]\n"
        f"Stats: {grow} grow, {age} age, {show} show"
    )
    if tree:
        print(f" {shade} shade")


class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._aged = 0
            self._show = 0

        def increment_grow(self) -> None:
            self._grow += 1

        def increment_age(self) -> None:
            self._aged += 1

        def increment_show(self) -> None:
            self._show += 1

        def get_grow(self) -> int:
            return self._grow

        def get_aged(self) -> int:
            return self._aged

        def get_show(self) -> int:
            return self._show

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
        self.stats = self.Stats()

    @staticmethod
    def older_year(days: int) -> None:
        print(f"Is {days} days more than a year? -> {days > 365}")

    @classmethod
    def unknown_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        print(
            f"{self.name}:",
            f"{round(self._height, 1)}cm,",
            f"{self._years} days old"
        )
        self.stats.increment_show()

    def grow(self, grow: float) -> None:
        self._height += grow
        self.stats.increment_grow()

    def age(self, age: int) -> None:
        self._years += age
        self.stats.increment_age()

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

    def get_name(self) -> str:
        return self.name

    def get_grow(self) -> int:
        return self.stats.get_grow()

    def get_aged(self) -> int:
        return self.stats.get_aged()

    def get_show(self) -> int:
        return self.stats.get_show()


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
        else:
            print(f" {self.name} is blooming beautifully!")

    def set_bloomed(self) -> None:
        self.bloomed = 1

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.set_bloomed()

    def grow_and_bloom(self, grow: float) -> None:
        print(f"[asking the {self.name} to grow and bloom]")
        super().grow(grow)
        self.set_bloomed()


class Seed(Flower):
    def __init__(self, name: str, height: float, years: int,
                 color: str) -> None:
        super().__init__(name, height, years, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def grow_age_bloom(self, grow: float, age: int) -> None:
        print(f"[make the {self.name} grow, age and bloom]")
        super().grow(grow)
        super().age(age)
        super().set_bloomed()
        self._seeds += 42


class Tree(Plant):
    def __init__(self, name: str, height: float, years: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, years)
        self.trunk_diameter = trunk_diameter
        self._shade = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shades of",
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )
        self._shade += 1

    def get_shade(self) -> int:
        return self._shade


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
    print("=== Garden Plant Types ===")

    print("=== Check year-old")
    Plant.older_year(30)
    Plant.older_year(400)
    print()

    print("=== Flower")
    flower = Flower("Rose", 15, 10, "Red")
    flower.show()
    show_stats(
        flower.get_name(),
        flower.get_grow(),
        flower.get_aged(),
        flower.get_show(),
        0,
        False
    )
    flower.grow_and_bloom(8)
    flower.show()
    show_stats(
        flower.get_name(),
        flower.get_grow(),
        flower.get_aged(),
        flower.get_show(),
        0,
        False
    )
    print()

    print("=== Tree")
    tree = Tree("Oak", 200, 365, 5.0)
    tree.show()
    show_stats(
        tree.get_name(),
        tree.get_grow(),
        tree.get_aged(),
        tree.get_show(),
        tree.get_shade(),
        True
    )
    tree.produce_shade()
    show_stats(
        tree.get_name(),
        tree.get_grow(),
        tree.get_aged(),
        tree.get_show(),
        tree.get_shade(),
        True
    )
    print()

    print("=== Seed")
    seed = Seed("Sunflower", 80, 45, "yellow")
    seed.show()
    seed.grow_age_bloom(30, 20)
    seed.show()
    show_stats(
        seed.get_name(),
        seed.get_grow(),
        seed.get_aged(),
        seed.get_show(),
        0,
        False
    )
    print()

    print("=== Anonymous")
    planta = Plant.unknown_plant()
    planta.show()
    show_stats(
        planta.get_name(),
        planta.get_grow(),
        planta.get_aged(),
        planta.get_show(),
        0,
        False
    )
