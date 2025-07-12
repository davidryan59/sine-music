import numpy as np
import matplotlib.pyplot as plt
from functions.helpers import (
    # get_kernel,
    # np_squashed_sine,
    fade_in_and_out,
    resample,
    random_integers,
    make_channel_fixed_val,
    integrate_freqs,
    sine_period_1,
    regular_times,
    normalise_amps,
    mix,
    audio_write,
    scale_amps_using_freqs,
    get_output_filename,
)


def script_slowly_changing_music():
    fname = script_slowly_changing_music.__name__
    filename = get_output_filename(fname)
    print(f"{fname}: started with {filename=}")

    fade_time_s = 0.02

    # sequence_rate_hz = 120  # Initial quantisation of sequence variables
    sample_rate_hz = 44100  # Final quantisation of sequence data
    # beats_gap = 0.3  # How long the transitions are, in beats
    # beat_length_s = 0.12  # How long each beat is, in seconds
    # kernel_size = 4  # Smoothing using a binomial distribution of width 17 = 1+2^4

    # # controls squashed_sine waveform
    # p, s = 0.005, 0.001

    # # format [time_in_samples, value]
    # sequence_data = np.array(
    #     [
    #         [8.0, 200],
    #         [4, 300],
    #         [3, 400],
    #         [1, 500],
    #         [8, 450],
    #         [4, 390],
    #         [4, 400],
    #         [2, 275],
    #         [1, 250],
    #         [1, 225],
    #         [4, 325],
    #         [4, 320],
    #         [6, 350],
    #         [8, 400],
    #         [0.2, 200],
    #         [0.2, 800],
    #         [2, 400],
    #     ]
    # )

    # options = "options"  # Anything related to the overall sequencer, not an individual chord or note
    # chords = "chords"  # Main area for all the notes in a piece of music to be sequenced
    # t = "t"  # Time in beats of a particular chord entry
    # a = "a"  # Amplitude from 0 to 100 of the chord (0 = 0.0, 100 = 1.0). Can also be note amplitude.
    # notes = "notes"  # List of individual notes in the chord
    # c = "c"  # Channel of a note: 1, 2, 3, etc
    # f = "f"  # Frequency of a note in Hz

    # sequence_data = {
    #     options: {},
    #     chords: [
    #         {t: 8, a: 10, notes: [{c:1, f:300},{c:2, f:400},{c:3, f:500}]},
    #         {t: 4, a: 10, notes: [{c:1, f:300},{c:2, f:400},{c:3, f:500}]},

    #     ],
    # }

    # Setup freq fading
    # amp_rand_mult = 1.8
    amp_f0 = 110
    # amp_exponent = -1.667

    # Setup timing
    count_beats = 30
    beat_time_s = 0.5
    fade_time_s = 0.5

    # Setup frequencies
    base_freq_hz = 28.264532450
    chan_freqs = np.array([2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 20, 24, 32])
    chan_freqs = np.array([2, 3, 4, 5, 6, 8, 11, 13, 17, 19, 20, 23, 32])

    base_freq_hz = 17.264532450
    chan_freqs = 128 / np.arange(4, 64)
    amp_channel_0 = 0.5
    amp_rand_mult = 2

    amp_f0, base_freq_hz, arr0, arr1 = 110, 31.2634, [2, 3, 4, 6], [8, 9, 10, 12, 15]
    amp_f0, base_freq_hz, arr0, arr1 = 200, 23.618, [3, 6, 9], [12, 14, 16, 18, 21]
    amp_f0, base_freq_hz, arr0, arr1 = 120, 3.618, [12, 16, 18, 24], [27, 30, 32, 36, 40, 45, 48]
    # amp_f0, base_freq_hz, arr0, arr1 = 200, 58.618, [1, 2], [4, 5, 6,7]
    # amp_f0, base_freq_hz, arr0, arr1 = 200, 261.63, [0.25, 0.5], [1]
    chan_freqs = np.array(arr1)
    chan_freqs = np.concat((arr0, chan_freqs, chan_freqs * 2, chan_freqs * 4, chan_freqs * 8))
    print(chan_freqs)

    chan_freqs_hz = chan_freqs * base_freq_hz
    count_channels = len(chan_freqs_hz)

    # Frequency at each beat time
    freqs_hz_beat = np.tile(chan_freqs_hz, count_beats).reshape((count_beats, count_channels))

    # Setup an N x (M+1) array for time vector + channel amplitudes
    max_time_s = count_beats * beat_time_s
    last_beat_start = max_time_s - beat_time_s
    beat_rate_hz = 1 / beat_time_s
    beat_starts_s = regular_times(0, last_beat_start, beat_rate_hz)
    sample_times_s = regular_times(0, max_time_s, sample_rate_hz)

    amp_exp_times = np.array([0, count_beats * beat_time_s])
    amp_exp_values = np.array([-3, -0.5])
    amp_exps = resample(sample_times_s, amp_exp_times, amp_exp_values)

    print("")
    print(amp_exps[:50])
    print("")
    print(amp_exps[-50:])
    print("")

    amp_data = random_integers(rows=count_beats, cols=count_channels, size=amp_rand_mult)

    make_channel_fixed_val(arr=amp_data, channel=0, val=amp_channel_0)

    freq_samp = resample(sample_times_s, beat_starts_s, freqs_hz_beat)

    freq_sum_samp = integrate_freqs(freq_samp, sample_rate_hz)

    sin_samp = sine_period_1(freq_sum_samp)

    sample_amps = resample(sample_times_s, beat_starts_s, amp_data)

    scale_amps_using_freqs(sample_amps, freq_samp, amp_f0, amp_exps)

    sample_amps = normalise_amps(sample_amps)

    waveform = mix(sin_samp, sample_amps)

    fade_in_and_out(waveform=waveform, sample_rate_hz=sample_rate_hz, fade_time_s=fade_time_s)

    audio_write(filename, sample_rate_hz, waveform)

    # Optional - plot the waveform
    # (Comment this out if you don't want to plot, plotting hangs the terminal)
    plt.plot(sample_times_s, waveform)
    plt.show()

    print(f"{fname}: finished")
