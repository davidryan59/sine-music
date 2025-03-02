from classes.envelope import Envelope
from classes.partial import Partial


def get_simple_partial() -> Partial:
    return Partial(
        freq=256,
        envelope=Envelope(
            times=[0, 0.1, 0.5, 3],
            amplitudes=[0, 1, 0.25, 0],
            ref_time=0.1,
        ),
    )


def test_simple_partial_ref_time():
    partial: Partial = get_simple_partial()
    assert partial.envelope.ref_time == 0.1


# TODO
# - Add more tests to * / + - ** // @
# - Want to test that copied object identities are different
