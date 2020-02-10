from __future__ import annotations
from threading import Lock, Thread
from typing import Optional

class SingletonMeta(type):
    _instance: Optional[Singleton] = None
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        while cls._lock:
            if not cls._instance:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Singleton(metaclass=SingletonMeta):
    name: str = None
    # counter: int = 0

    def __init__(self, name: str) -> None:
        self.name = name

    def print_singleton(self):
        print(self.name)

    # def plus_counter(self):
    #     self.counter += 1
    #
    # def minus_counter(self):
    #     self.counter -= 1

def test_singleton(name: str) -> None:
    singleton = Singleton(name)
    singleton.print_singleton()

if __name__ == "__main__":

    print("test")
    test1 = Thread(target=test_singleton, args=("Health",))
    test2 = Thread(target=test_singleton, args=("Death",))

    test1.start()
    test2.start()

    # singleton = Singleton("Health")
    # print(singleton.name)
    # print(singleton.counter)