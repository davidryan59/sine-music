from datetime import datetime
import math
import numpy as np
from scipy.io.wavfile import write
from typing import List


PI = np.pi
PI2 = 2 * np.pi

DEFAULT_START_KERNEL = [0.5, 0.5]  # Creates a binomial distribution


# Return a binomial distribution of width 1+2^n for smoothing time series
def get_kernel(n: int, start_kernel: List[int] = DEFAULT_START_KERNEL):
    kernel = [*start_kernel]
    for _ in range(n):
        kernel = np.convolve(kernel, kernel)

    return kernel


# Simple parameterised waveform that can go smoothly between sine, square, sawtooth-like
# t is np.array of time values
# p, s in range [0, 1]
# p is ratio of peak width to 2*pi
# s is how squashed one half of the sine wave is compared to the other
# p, s = 0, 0: sine
# p, s = 0, 1: sawtooth-like
# p, s = 1, 0: square
# p, s = 1, 1: square (also)
# Both p and s can be supplied as numpy vectors
def squashed_sine(t, p, s):
    a = PI2 * (1 - s) * (1 - p) / (2 - s)
    b = a + p * PI
    c = PI2 - b + a
    val = t % PI2
    if val < a:
        return math.cos(val * np.pi / a)
    elif val <= b:
        return -1
    elif val < c:
        return -math.cos((val - b) * np.pi / (c - b))
    else:
        return 1


# Numpy function of squashed_sine above
np_squashed_sine = np.frompyfunc(squashed_sine, 3, 1)


# Apply this to a finished waveform to prevent clipping at start and end
def fade_in_and_out(waveform, sample_rate_hz, fade_time_s):
    fade_samples = int(fade_time_s * sample_rate_hz)
    k = fade_samples  # shorter variable name
    waveform[:k] = waveform[:k] * np.linspace(0, 1, k)
    waveform[-k:] = waveform[-k:] * np.linspace(1, 0, k)


# Use linear interpolation on a vector or array of values to get a new vector or array of values
def resample(new_t, old_t, old_v):
    if len(old_v.shape) < 2:
        # old_v is a vector
        return np.interp(x=new_t, xp=old_t, fp=old_v)
    else:
        # old_v is an array
        count_channels = old_v.shape[1]
        new_v = np.zeros((len(new_t), count_channels))
        for chan in range(count_channels):
            new_v[:, chan] = np.interp(x=new_t, xp=old_t, fp=old_v[:, chan])

        return new_v


def integrate_freqs(freqs, divisor):
    return np.cumsum(freqs, axis=0) / divisor


def sine_period_1(t):
    return np.sin(t * PI2)


def regular_times(min_s, max_s, rate_hz):
    return np.linspace(min_s, max_s, int(max_s * rate_hz + 1))


# Scale amps so that their sum at each time is 1
def normalise_amps(amps):
    amp_sum = np.sum(amps, axis=1)
    return amps / amp_sum.reshape((amps.shape[0], 1))


def mix(raw_waveforms, amplitudes):
    wav_samp = raw_waveforms * amplitudes
    return np.sum(wav_samp, axis=1)


def audio_write(filename, sample_rate_hz, waveform):
    write(filename, sample_rate_hz, waveform.astype(np.float32))
    print(f"Wrote {waveform.shape=} to {filename=}")


def random_integers(rows, cols, size):
    return np.trunc(np.random.rand(rows, cols) * size)


def make_channel_fixed_val(arr, channel, val):
    arr[:, channel] = np.ones(arr.shape[0]) * val


def scale_amps_using_freqs(amps, freqs, f0, f_exp):
    # Make sure f_exp is either scalar or array, but not vector
    if type(f_exp) == int:
        f_exp0 = f_exp
    elif len(f_exp.shape) == 1:
        f_exp0 = f_exp.reshape(f_exp.shape[0], 1)
    else:
        f_exp0 = f_exp
    amps = amps * (np.maximum(freqs, f0) ** f_exp0)


def get_output_filename(fname: str) -> str:
    dt = datetime.now()
    return f"output/{fname}_{int(dt.timestamp())}.wav"
