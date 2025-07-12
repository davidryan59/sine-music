import numpy as np
from classes.envelope import Envelope
from classes.partial import Partial
from classes.music import Music
from functions.helpers import get_output_filename


def script_test_envelope():
    fname = script_test_envelope.__name__
    filename = get_output_filename(fname)
    print(f"{fname}: started with {filename=}")

    e1: Envelope = Envelope([0, 0.01, 0.03, 0.06, 0.20], [0, 1, 0.5, 0.25, 0])
    p1: Partial = Partial(freq=240, envelope=e1)

    n = 2.688
    print("")
    print(p1)
    print(p1 + n)
    print(p1 - n)
    print(p1 * n)
    print(p1 / n)
    print(p1**n)
    print(p1 // n)
    print(p1 @ n)

    m1: Music = Music(partials=[p1])
    print(m1)
    print(m1())

    print("")
    print(e1)
    print(e1.times)
    print(e1.amplitudes)
    print(tuple(e1.times))
    print(tuple(e1.amplitudes))
    print(tuple(e1.times)[0])
    print(tuple(e1.times)[0] == 0)
    print(np.array((0, 0.01, 0.3)))
    print("end")

    # print(id(e1), id(e1.times), id(e1.amplitudes), e1)

    # e2 = copy(e1)
    # print(id(e2), id(e2.times), id(e2.amplitudes), e2)

    # e1.times[2] = -0.4
    # print(id(e1), id(e1.times), id(e1.amplitudes), e1)
    # print(id(e2), id(e2.times), id(e2.amplitudes), e2)

    # print(id(p1), id(p1.envelope), id(p1.envelope.times), p1)

    # p2: Partial = copy(p1)
    # print(id(p2), id(p2.envelope), id(p2.envelope.times), p2)

    # p2.envelope.amplitudes[1] = 0.8
    # print(id(p1), id(p1.envelope), id(p1.envelope.times), p1)
    # print(id(p2), id(p2.envelope), id(p2.envelope.times), p2)

    # p3 = p1 * 2.5
    # print(p3)

    # p4 = p1 / 2.5
    # print(p4)

    # e3 = e1 * 3.33
    # print(e1)
    # print(e3)
    # e1.amplitudes[3] = 5.555
    # e3.amplitudes[1] = 4.444
    # print(e1)
    # print(e3)

    # e0 = Envelope([0, 0.01, 0.03, 0.06, 0.20], [0, 1, 0.5, 0.25, 0])

    # n = 7
    # print("")
    # print(e0)
    # print(e0 + n)
    # print(e0 - n)
    # print(e0 * n)
    # print(e0 / n)
    # print(e0 ** n)
    # print(e0 // n)

    # print((e0 + 7) ** 13)
    # print((e0 ** 13) + 7)

    # print("")
    # print(e0)
    # print(e0 + 2)
    # print((e0 + 2) ** 3)
    # print("")
    # print(e0)
    # print(e0 ** 3)
    # print((e0 ** 3) + 2)

    print(f"{fname}: finished")
