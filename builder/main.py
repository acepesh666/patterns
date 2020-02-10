from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class Builder(ABC):

    @abstractproperty
    def product(self) -> None:
        pass

    @abstractproperty
    def produce_part_frame(self) -> None:
        pass

    @abstractproperty
    def produce_part_wheels(self) -> None:
        pass

    @abstractproperty
    def produce_part_engine(self) -> None:
        pass

    @abstractproperty
    def produce_part_light(self) -> None:
        pass

class RacingBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product

    def produce_part_frame(self) -> None:
        self._product.add("Frame weight: Light")

    def produce_part_wheels(self) -> None:
        self._product.add("Number of wheels: Two")

    def produce_part_engine(self) -> None:
        self._product.add("Power engine: 1000hp")

    def produce_part_light(self) -> None:
        self._product.add("Light: None")

class Product():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")

class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return  self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal(self) -> None:
        self.builder.produce_part_frame()
        self.builder.produce_part_engine()
        self.builder.produce_part_wheels()

    def build_full(self) -> None:
        self.builder.produce_part_frame()
        self.builder.produce_part_engine()
        self.builder.produce_part_wheels()
        self.builder.produce_part_light()

if __name__ == "__main__":

    director = Director()
    builder = RacingBuilder()
    director.builder = builder

    print("Minimal: ")
    director.build_minimal()
    builder.product.list_parts()

    print("\n")

    print("Full: ")
    director.build_full()
    builder.product.list_parts()

    print("\n")

    print("Custom: ")
    builder.produce_part_frame()
    builder.produce_part_engine()
    builder.product.list_parts()