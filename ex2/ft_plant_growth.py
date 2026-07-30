#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def print_plant(self) -> None:
        print(
            f"{self.name.capitalize()}:",
            f"{round(self.height, 1)}cm,",
            f"{self.age} days old"
        )

    def set_grown(self, grown: float) -> None:
        self.height += grown

    def set_aged(self, aged: int) -> None:
        self.age += aged

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.age


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)
    height_before = int(plant.get_height())
    print("=== Garden Plant Growth ===")
    plant.print_plant()
    print("=== Day 1 ===")
    plant.set_grown(0.5)
    plant.set_aged(1)
    plant.print_plant()
    print("=== Day 2 ===")
    plant.set_grown(0.7)
    plant.set_aged(1)
    plant.print_plant()
    print("=== Day 3 ===")
    plant.set_grown(0.3)
    plant.set_aged(1)
    plant.print_plant()
    print("=== Day 4 ===")
    plant.set_grown(2)
    plant.set_aged(1)
    plant.print_plant()
    print("=== Day 5 ===")
    plant.set_grown(1.2)
    plant.set_aged(1)
    plant.print_plant()
    print("=== Day 6 ===")
    plant.set_grown(0.1)
    plant.set_aged(1)
    plant.print_plant()
    print("=== Day 7 ===")
    plant.set_grown(0)
    plant.set_aged(1)
    plant.print_plant()
