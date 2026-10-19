import numpy as np

def cross_correlate(signal1, signal2):
    return np.correlate(signal1, signal2, mode='full')


def correlate_array(signals):
    """
    Cross-correlate all antenna pairs
    """
    correlations = []
    n = len(signals)

    for i in range(n):
        for j in range(i+1, n):
            corr = cross_correlate(signals[i], signals[j])
            correlations.append(corr)

    return correlations
