#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, years: int) -> None:
        self.name = name
        self.height = height
        self.years = years

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}:",
            f"{round(self.height, 1)}cm,",
            f"{self.years} days old"
        )


if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)
    plant.show()
    plant = Plant("Sunflower", 80, 45)
    plant.show()
    plant = Plant("Cactus", 15, 120)
    plant.show()
