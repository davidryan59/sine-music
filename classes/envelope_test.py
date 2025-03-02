from classes.envelope import Envelope


def get_simple_envelope() -> Envelope:
    return Envelope(
        times=[0, 0.1, 0.5, 3],
        amplitudes=[0, 1, 0.25, 0],
        ref_time=0.1,
    )


def test_simple_envelope_ref_time():
    envelope: Envelope = get_simple_envelope()
    assert envelope.ref_time == 0.1
