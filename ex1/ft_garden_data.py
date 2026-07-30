#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def print_plant(self) -> None:
        print(
            f"{self.name.capitalize()}:",
            f"{round(self.height, 1)}cm,",
            f"{self.age} days old"
        )


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    plant.print_plant()
    plant = Plant("Sunflower", 80, 45)
    plant.print_plant()
    plant = Plant("Cactus", 15, 120)
    plant.print_plant()
