import numpy as np

def reconstruct_sky(correlations):
    """
    Combine correlations and reconstruct sky intensity
    """
    combined = np.mean(correlations, axis=0)
    sky = np.abs(np.fft.ifft(combined))
    return sky
