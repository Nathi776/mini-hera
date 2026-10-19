import numpy as np

def generate_cosmic_signal(
    duration=5.0,
    sample_rate=1000,
    signal_freq=1420,
    noise_level=0.5,
    interference_strength=2.0
):
    """
    Simulates a radio telescope signal.
    
    Parameters:
    - duration: seconds
    - sample_rate: samples per second
    - signal_freq: hydrogen line (MHz scaled)
    - noise_level: random noise strength
    - interference_strength: artificial interference
    
    Returns:
    - time array
    - signal array
    """

    t = np.linspace(0, duration, int(sample_rate * duration))

    # Simulated cosmic hydrogen signal
    cosmic_signal = np.sin(2 * np.pi * signal_freq * t * 1e-6)

    # Thermal noise
    noise = noise_level * np.random.normal(size=len(t))

    # Interference (e.g. satellite burst)
    interference = interference_strength * np.sin(2 * np.pi * 50 * t)

    # Combined signal
    raw_signal = cosmic_signal + noise + interference

    return t, raw_signal
