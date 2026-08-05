#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, years: int) -> None:
        self.name = name
        self.height = height
        self.years = years

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}:",
            f"{round(self.height, 1)}cm,",
            f"{self.years} days old"
        )

    def grow(self, grow: float) -> None:
        self.height += grow

    def age(self, age: int) -> None:
        self.years += age

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.years


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)
    height_before = int(plant.get_height())
    print("=== Garden Plant Growth ===")
    plant.show()
    print("=== Day 1 ===")
    plant.grow(0.5)
    plant.age(1)
    plant.show()
    print("=== Day 2 ===")
    plant.grow(0.7)
    plant.age(1)
    plant.show()
    print("=== Day 3 ===")
    plant.grow(0.3)
    plant.age(1)
    plant.show()
    print("=== Day 4 ===")
    plant.grow(2)
    plant.age(1)
    plant.show()
    print("=== Day 5 ===")
    plant.grow(1.2)
    plant.age(1)
    plant.show()
    print("=== Day 6 ===")
    plant.grow(0.1)
    plant.age(1)
    plant.show()
    print("=== Day 7 ===")
    plant.grow(0)
    plant.age(1)
    plant.show()
    print(
        "Growth this week:",
        f"{round(plant.get_height() - height_before, 1)}cm"
    )
