import numpy as np


# An Envelope is a list of amplitudes at a list of times,
# with linear interpolation between adjacent times,
# and zero values outside of the times.
#
# This is a piecewise linear function, see: https://en.wikipedia.org/wiki/Piecewise_linear_function
# It can be applied to a waveform (such as a sine wave) to shape the waveform.
# The ref_time gives the temporal centre when scaling (multiplying) the times.
#
# NOTE: these extra conditions should hold:
# - times should be numeric and strictly ascending
# - amplitudes should be numeric and non-negative, normally between 0 and 1 if applied to a sine wave (>1 gives distortion)
# - amplitudes should normally start and end with 0, to give smooth waveform when applied to a sine wave
# Currently these conditions are not checked.


# Operations
# Let e be an envelope, and n be a number:
# e * n = n * e scales the amplitudes by n
# e + n = n + e shifts the times and ref_time by n
# e ** n = n ** e scales the times by n, centered on ref_time
# e1 + e2 combines the two amplitudes in a linear way, ref_time taken from e1
class Envelope:
    def __init__(self, times: np.array, amplitudes: np.array, ref_time: float = 0):
        self.times: np.array = np.array(times)
        self.amplitudes: np.array = np.array(amplitudes)
        self.ref_time: float = ref_time
        if len(self.times) != len(self.amplitudes):
            raise Exception("lengths of times and amplitudes should match")

    # To copy an Envelope, return a new Envelope with a separate copy of the times and the amplitudes
    def __copy__(self):
        return Envelope(
            times=np.array(self.times),
            amplitudes=np.array(self.amplitudes),
            ref_time=self.ref_time,
        )

    def __repr__(self) -> str:
        return f"Envelope(ref_time={self.ref_time}, times={self.times}, amplitudes={self.amplitudes})"

    # Override many dunder methods to make Envelopes easy to use
    # See: https://www.pythonmorsels.com/every-dunder-method/

    # Envelope * number gives a new Envelope with amplitudes multiplied by that number
    def __mul__(self, other):
        if type(other) in (int, float):
            return Envelope(times=np.array(self.times), amplitudes=self.amplitudes * other, ref_time=self.ref_time)
        else:
            raise Exception("Could not multiply Envelope amplitudes")

    # Envelope * number gives a new Envelope with amplitudes divided by that number
    def __truediv__(self, other):
        if type(other) in (int, float):
            return self * (1 / other)
        else:
            raise Exception("Could not divide Envelope amplitudes")

    # Envelope + number gives a new Envelope with times (and ref_time) added by that number
    def __add__(self, other):
        if type(other) in (int, float):
            return Envelope(times=self.times + other, amplitudes=np.array(self.amplitudes), ref_time=self.ref_time + other)
        else:
            raise Exception("Could not add Envelope times")

    # Envelope - number gives a new Envelope with times (and ref_time) subtracted by that number
    def __sub__(self, other):
        if type(other) in (int, float):
            return self + (-other)
        else:
            raise Exception("Could not subtract Envelope times")

    # Envelope ** number gives a new Envelope with times multiplied by that number, centred on ref_time
    def __pow__(self, other):
        if type(other) in (int, float):
            return Envelope(
                times=(self.times - self.ref_time) * other + self.ref_time,
                amplitudes=np.array(self.amplitudes),
                ref_time=self.ref_time,
            )
        else:
            raise Exception("Could not multiply Envelope times")

    # Envelope // number gives a new Envelope with times divided by that number, centred on ref_time
    def __floordiv__(self, other):
        if type(other) in (int, float):
            return self ** (1 / other)
        else:
            raise Exception("Could not divide Envelope times")

    # All operations above are commutative, allow them to be called either way round
    __rmul__ = __mul__
    __rtruediv__ = __truediv__
    __radd__ = __add__
    __rsub__ = __sub__
    __rpow__ = __pow__
    __rfloordiv__ = __floordiv__
