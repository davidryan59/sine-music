from typing import List
from copy import copy
from classes.partial import Partial

# import numpy as np


# A Music is a collection of Partials
class Music:
    def __init__(self, partials: List[Partial]):
        self.partials: List[Partial] = partials

    def __call__(self):
        return "self.call was called"

    # To copy a Music, copy all its partials
    def __copy__(self):
        return Music(partials=[copy(x) for x in self.partials])

    def __repr__(self) -> str:
        return f"Music(partials={self.partials})"

    # # NOT YET IMPLEMENTED remaining functions
    # # See the Partial implementations (commented out) for the types of operations to build

    # def __mul__(self, other):
    #     return Partial(
    #         freq = self.freq,
    #         envelope = self.envelope * other
    #     )

    # def __truediv__(self, other):
    #     return Partial(
    #         freq = self.freq,
    #         envelope = self.envelope / other
    #     )

    # def __add__(self, other):
    #     return Partial(
    #         freq = self.freq,
    #         envelope = self.envelope + other
    #     )

    # def __sub__(self, other):
    #     return Partial(
    #         freq = self.freq,
    #         envelope = self.envelope - other
    #     )

    # def __pow__(self, other):
    #     return Partial(
    #         freq = self.freq,
    #         envelope = self.envelope ** other
    #     )

    # def __floordiv__(self, other):
    #     return Partial(
    #         freq = self.freq,
    #         envelope = self.envelope // other
    #     )

    # def __matmul__(self, other):
    #     if type(other) in (int, float):
    #         return Partial(
    #             freq = self.freq * other,
    #             envelope = copy(self.envelope)
    #         )
    #     else:
    #         raise("Could not multiply frequency of Partial by non-numeric argument")

    # # All operations above are commutative, allow them to be called either way round
    # __rmul__ = __mul__
    # __rtruediv__ = __truediv__
    # __radd__ = __add__
    # __rsub__ = __sub__
    # __rpow__ = __pow__
    # __rfloordiv__ = __floordiv__
    # __rmatmul__ = __matmul__
