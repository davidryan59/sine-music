from copy import copy
from classes.envelope import Envelope


# A Partial is an Envelope applied to a specific frequency of sine wave
class Partial:
    def __init__(self, freq: float, envelope: Envelope):
        self.freq: float = freq
        self.envelope: Envelope = envelope
        if self.freq <= 0:
            raise Exception("frequency must be positive")

    # To copy a Partial, return a new Partial with the same freq and a copy of the Envelope
    def __copy__(self):
        return Partial(freq=self.freq, envelope=copy(self.envelope))

    def __repr__(self) -> str:
        return f"Partial(freq={self.freq}, envelope={self.envelope})"

    # Use * and / to multiply envelope amplitudes by a number
    def __mul__(self, other):
        return Partial(freq=self.freq, envelope=self.envelope * other)

    def __truediv__(self, other):
        return Partial(freq=self.freq, envelope=self.envelope / other)

    # Use + and - to add or subtract envelope time by a number
    def __add__(self, other):
        return Partial(freq=self.freq, envelope=self.envelope + other)

    def __sub__(self, other):
        return Partial(freq=self.freq, envelope=self.envelope - other)

    # Use ** and // to make envelope time faster or slower
    def __pow__(self, other):
        return Partial(freq=self.freq, envelope=self.envelope**other)

    def __floordiv__(self, other):
        return Partial(freq=self.freq, envelope=self.envelope // other)

    # Use @ to multiply the frequency of a Partial
    def __matmul__(self, other):
        if type(other) in (int, float):
            return Partial(freq=self.freq * other, envelope=copy(self.envelope))
        else:
            raise Exception("Could not multiply frequency of Partial by non-numeric argument")
