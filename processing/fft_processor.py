import numpy as np

def compute_fft(signal, sample_rate):
    """
    Computes FFT and returns frequencies and power spectrum.
    """

    n = len(signal)
    fft_values = np.fft.fft(signal)
    fft_freqs = np.fft.fftfreq(n, d=1/sample_rate)

    power = np.abs(fft_values) ** 2

    # Only positive frequencies
    half = n // 2
    return fft_freqs[:half], power[:half]
