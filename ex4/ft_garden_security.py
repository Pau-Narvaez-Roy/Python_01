#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        if height >= 0:
            self._height = height
        else:
            print(
                f"{self.name.capitalize()}:",
                "Error, height can't be negative",
                "setting height at default value of 0"
            )
            self._height = 0
        if age >= 0:
            self._age = age
        else:
            print(
                f"{self.name.capitalize()}:",
                "Error, age can't be negative",
                "setting age at default value of 0"
            )
            self._age = 0

    def print_plant(self) -> None:
        print(
            f"{self.name.capitalize()}:",
            f"{round(self._height, 1)}cm,",
            f"{self._age} days old"
        )

    def set_grown(self, grown: float) -> None:
        self._height += grown

    def set_aged(self, aged: int) -> None:
        self._age += aged

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            print(
                f"{self.name.capitalize()}:",
                "Error, height can't be negative"
            )
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
        else:
            print(
                f"{self.name.capitalize()}:",
                "Error, age can't be negative"
            )
            print("Age update rejected")     

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    rose.print_plant()
    print()
    rose.set_height(25)
    print(f"Height updated: {rose.get_height()}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")
    print()
    rose.set_height(-1)
    rose.set_age(-1)
    print()
    print("Current state:", end=" ")
    rose.print_plant()
