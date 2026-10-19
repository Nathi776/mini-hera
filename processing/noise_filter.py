import numpy as np
from scipy.signal import butter, filtfilt

def bandpass_filter(signal, lowcut, highcut, fs, order=4):
    """
    Applies a Butterworth bandpass filter.
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist

    b, a = butter(order, [low, high], btype="band")
    filtered_signal = filtfilt(b, a, signal)

    return filtered_signal


def moving_average(signal, window_size=10):
    """
    Smooths signal using moving average.
    """
    return np.convolve(signal, np.ones(window_size)/window_size, mode='same')
