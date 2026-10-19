import matplotlib.pyplot as plt
from processing.signal_generator import generate_cosmic_signal
from processing.noise_filter import bandpass_filter, moving_average
from processing.fft_processor import compute_fft

def plot_raw_signal():
    t, signal = generate_cosmic_signal()

    plt.figure(figsize=(12, 5))
    plt.plot(t, signal, color="blue", linewidth=0.7)
    plt.title("Simulated Radio Telescope Signal")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_raw_signal()


def plot_filtered_signal():
    # Generate signal
    t, raw_signal = generate_cosmic_signal()

    # Apply filters
    filtered = bandpass_filter(
        raw_signal,
        lowcut=5,
        highcut=200,
        fs=1000
    )

    smoothed = moving_average(filtered, window_size=20)

    # Plot
    plt.figure(figsize=(14, 7))

    plt.subplot(3, 1, 1)
    plt.plot(t, raw_signal)
    plt.title("Raw Signal")
    plt.ylabel("Amplitude")

    plt.subplot(3, 1, 2)
    plt.plot(t, filtered, color="orange")
    plt.title("Band-pass Filtered Signal")
    plt.ylabel("Amplitude")

    plt.subplot(3, 1, 3)
    plt.plot(t, smoothed, color="green")
    plt.title("Smoothed Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_filtered_signal()


def plot_fft_analysis():
    # Generate raw signal
    t, raw_signal = generate_cosmic_signal()

    # Filter signal
    filtered = bandpass_filter(
        raw_signal,
        lowcut=5,
        highcut=200,
        fs=1000
    )
    smoothed = moving_average(filtered, window_size=20)

    # FFT
    freqs, power = compute_fft(smoothed, sample_rate=1000)

    # Plot
    plt.figure(figsize=(14, 9))

    plt.subplot(3, 1, 1)
    plt.plot(t, raw_signal)
    plt.title("Raw Signal")
    plt.ylabel("Amplitude")

    plt.subplot(3, 1, 2)
    plt.plot(t, smoothed, color="green")
    plt.title("Filtered Signal")
    plt.ylabel("Amplitude")

    plt.subplot(3, 1, 3)
    plt.plot(freqs, power, color="purple")
    plt.title("Frequency Spectrum (FFT)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_fft_analysis()