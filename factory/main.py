from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: {product.operation()}"
        return result

class ConcreteCreator1(Creator):

    def factory_method(self) -> ConcreteProduct1:
        return ConcreteProduct1()

class ConcreteCreator2(Creator):

    def factory_method(self) -> ConcreteProduct2:
        return ConcreteProduct2()

class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProduct1(Product):

    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"

class ConcreteProduct2(Product):

    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"

def client_code(creator: Creator) -> None:
    print(creator.some_operation())

if __name__ == "__main__":
    print("Launch ConcreteProduct1")
    client_code(ConcreteCreator1())
    print("\n")

    print("Launch ConcreteProduct2")
    client_code(ConcreteCreator2())