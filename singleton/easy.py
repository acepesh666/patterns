from __future__ import annotations
from typing import Optional

class SingletonMeta(type):
    _instance: Optional[Singleton] = None

    def __call__(self) -> Singleton:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance

class Singleton(metaclass=SingletonMeta):
    name: str = ""
    counter: int = 0

    # def __init__(self, name: str):
    #     self.name = name

    def change_name(self, name):
        self.name = name

    def print_singleton(self):
        print(self.name + ":" + str(self.counter))

    def plus_counter(self):
        self.counter += 1

    def minus_counter(self):
        self.counter -= 1

if __name__ == "__main__":

    singleton1 = Singleton()
    singleton1.change_name("First")
    singleton1.plus_counter()

    print("First singleton:")
    singleton1.print_singleton()

    singleton2 = Singleton()
    singleton2.change_name("Second")
    singleton2.plus_counter()

    print("\nSecond singleton:")
    singleton2.print_singleton()
    print("\nFirst singleton:")
    singleton1.print_singleton()