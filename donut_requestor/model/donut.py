from enum import StrEnum
from pydantic import BaseModel

from donut_requestor.helper.exceptions import BoxIsFullException


class Flavour(StrEnum):
    CHOCOLATE = "choco"
    VANILLA = "vanilla"
    STRAWBERRY = "strawberry"


class Donut(BaseModel):
    flavour: Flavour
    _price_by_flavour: dict[str, float] = {
        Flavour.STRAWBERRY: 1.70,
        Flavour.CHOCOLATE: 2.10,
        Flavour.VANILLA: 1.90,
    }

    def price(self) -> float:
        return self._price_by_flavour[self.flavour]


class DonutBox:
    amount: int
    _donuts: list[Donut] = []

    def __init__(self, amount: int):
        self.amount = amount

    @property
    def donuts(self) -> list[Donut]:
        return self._donuts

    def add_donut(self, donut: Donut):
        if self.amount - 1 <= 0:
            raise BoxIsFullException(message="You can't add more donuts on the box")
        self._donuts.append(donut)

    def any_donut_of_flavour(self, flavour: Flavour) -> bool:
        result = False
        index = 0
        while index < len(self._donuts):
            if self._donuts[index].flavour == flavour:
                result = True
                index += 1
        return result

    def box_price(self) -> float:
        # base cost plus cost of each donut
        return 0.20 + sum([donut.price() for donut in self._donuts])
