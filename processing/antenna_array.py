import numpy as np

class Antenna:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def simulate_antenna_signals(base_signal, antennas, sample_rate):
    """
    Simulate time delays for multiple antennas.
    """
    c = 3e8  # speed of light
    signals = []

    for ant in antennas:
        delay = (ant.x + ant.y) / c
        delay_samples = int(delay * sample_rate)

        shifted = np.roll(base_signal, delay_samples)
        signals.append(shifted)

    return np.array(signals)
