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
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    print("=== Plant Factory Output ===")
    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()
