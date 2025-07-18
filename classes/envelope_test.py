import pytest
from classes.envelope import Envelope
from copy import copy


def get_simple_envelope() -> Envelope:
    return Envelope(
        times=[0, 0.1, 0.5, 3],
        amplitudes=[0, 1, 0.25, 0],
        ref_time=0.1,
    )


def test_simple_envelope_ref_time():
    e1: Envelope = get_simple_envelope()
    assert e1.ref_time == 0.1


def test_simple_envelope_mult_times():
    e2: Envelope = get_simple_envelope() * 2.4
    assert tuple(e2.times) == (0, 0.1, 0.5, 3)


def test_simple_envelope_mult_amps():
    e2: Envelope = get_simple_envelope() * 2.4
    assert tuple(e2.amplitudes) == (0, 2.4, 0.6, 0)


def test_simple_envelope_add_times():
    e2: Envelope = get_simple_envelope() + 2.4
    assert tuple(e2.times) == (2.4, 2.5, 2.9, 5.4)


def test_simple_envelope_add_amps():
    e2: Envelope = get_simple_envelope() + 2.4
    assert tuple(e2.amplitudes) == (0, 1, 0.25, 0)


def test_simple_envelope_pow_times():
    e2: Envelope = get_simple_envelope() ** 2.4
    assert tuple(e2.times) == pytest.approx((-0.14, 0.1, 1.06, 7.06))


def test_simple_envelope_pow_amps():
    e2: Envelope = get_simple_envelope() ** 2.4
    assert tuple(e2.amplitudes) == (0, 1, 0.25, 0)


def test_simple_envelope_mult_ids():
    e1: Envelope = get_simple_envelope()
    e2: Envelope = e1 * 2.4
    assert id(e1) != id(e2)


def test_simple_envelope_rmul():
    e1: Envelope = get_simple_envelope() * 2.64
    e2: Envelope = 2.64 * get_simple_envelope()
    assert tuple(e1.amplitudes) == tuple(e2.amplitudes)


def test_simple_envelope_rtruediv():
    e1: Envelope = get_simple_envelope() / 2.64
    e2: Envelope = 2.64 / get_simple_envelope()
    assert tuple(e1.amplitudes) == tuple(e2.amplitudes)


def test_simple_envelope_radd():
    e1: Envelope = get_simple_envelope() + 2.64
    e2: Envelope = 2.64 + get_simple_envelope()
    assert tuple(e1.times) == tuple(e2.times)


def test_simple_envelope_rsub():
    e1: Envelope = get_simple_envelope() - 2.64
    e2: Envelope = 2.64 - get_simple_envelope()
    assert tuple(e1.times) == tuple(e2.times)


def test_simple_envelope_rpow():
    e1: Envelope = get_simple_envelope() ** 2.64
    e2: Envelope = 2.64 ** get_simple_envelope()
    assert tuple(e1.times) == tuple(e2.times)


def test_simple_envelope_rfloordiv():
    e1: Envelope = get_simple_envelope() // 2.64
    e2: Envelope = 2.64 // get_simple_envelope()
    assert tuple(e1.times) == tuple(e2.times)


def test_simple_envelope_mul_div():
    e1: Envelope = get_simple_envelope() * 2.64
    e2: Envelope = get_simple_envelope() / (1 / 2.64)
    assert tuple(e1.amplitudes) == tuple(e2.amplitudes)


def test_simple_envelope_add_sub():
    e1: Envelope = get_simple_envelope() + 2.64
    e2: Envelope = get_simple_envelope() - (0 - 2.64)
    assert tuple(e1.times) == tuple(e2.times)


def test_simple_envelope_pow_floordiv():
    e1: Envelope = get_simple_envelope() ** 2.64
    e2: Envelope = get_simple_envelope() // (1 / 2.64)
    assert tuple(e1.times) == tuple(e2.times)


def test_simple_envelope_copy_times_same():
    e1: Envelope = get_simple_envelope()
    e2: Envelope = copy(e1)
    assert tuple(e1.times) == tuple(e2.times)


def test_simple_envelope_copy_amplitudes_same():
    e1: Envelope = get_simple_envelope()
    e2: Envelope = copy(e1)
    assert tuple(e1.amplitudes) == tuple(e2.amplitudes)


def test_simple_envelope_copy_ref_time_same():
    e1: Envelope = get_simple_envelope()
    e2: Envelope = copy(e1)
    assert e1.ref_time == e2.ref_time


def test_simple_envelope_copy_id_different():
    e1: Envelope = get_simple_envelope()
    e2: Envelope = copy(e1)
    assert id(e1) != id(e2)
