import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, firwin


# Tạo tín hiệu mẫu với nhiều tần số
def generate_signal(fs, duration, freqs):
    t = np.arange(0, duration, 1/fs)
    signal = np.zeros_like(t)
    for f in freqs:
        signal += np.sin(2 * np.pi * f * t)
    return t, signal


# Biến đổi Fourier nhanh (FFT)
def perform_fft(signal, fs):
    N = len(signal)
    fft_result = np.fft.fft(signal)
    fft_freqs = np.fft.fftfreq(N, 1/fs)
    return fft_freqs[:N//2], np.abs(fft_result[:N//2])


# Thiết kế bộ lọc Butterworth thông thấp
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


# Áp dụng bộ lọc Butterworth
def apply_butterworth_filter(signal, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order)
    return lfilter(b, a, signal)


# Thiết kế bộ lọc FIR
def apply_fir_filter(signal, cutoff, fs, numtaps=101):
    nyq = 0.5 * fs
    fir_coeff = firwin(numtaps, cutoff/nyq)
    return lfilter(fir_coeff, 1.0, signal)


# Hiển thị tín hiệu và kết quả FFT
def plot_signal(t, signal, title):
    plt.figure(figsize=(10, 4))
    plt.plot(t, signal)
    plt.title(title)
    plt.xlabel('Thời gian (giây)')
    plt.ylabel('Biên độ')
    plt.grid()
    plt.show()


# Hiển thị kết quả FFT
def plot_fft(fft_freqs, fft_result, title):
    plt.figure(figsize=(10, 4))
    plt.plot(fft_freqs, fft_result)
    plt.title(title)
    plt.xlabel('Tần số (Hz)')
    plt.ylabel('Biên độ')
    plt.grid()
    plt.show()


# Chương trình chính
if __name__ == "__main__":
    # Tạo tín hiệu
    fs = 1000  # Tần số lấy mẫu
    duration = 2.0  # Thời lượng tín hiệu (giây)
    freqs = [50, 120]  # Tần số của các tín hiệu thành phần

    t, signal = generate_signal(fs, duration, freqs)
    
    # Hiển thị tín hiệu gốc
    plot_signal(t, signal, "Tín hiệu gốc")

    # Thực hiện FFT trên tín hiệu gốc
    fft_freqs, fft_result = perform_fft(signal, fs)
    plot_fft(fft_freqs, fft_result, "Phổ tần số của tín hiệu gốc")

    # Áp dụng bộ lọc Butterworth thông thấp
    cutoff = 100  # Tần số cắt của bộ lọc
    filtered_signal_butter = apply_butterworth_filter(signal, cutoff, fs)

    # Hiển thị tín hiệu sau khi lọc Butterworth
    plot_signal(t, filtered_signal_butter, f"Tín hiệu sau khi lọc Butterworth (cutoff={cutoff} Hz)")

    # Thực hiện FFT sau khi lọc Butterworth
    fft_freqs_butter, fft_result_butter = perform_fft(filtered_signal_butter, fs)
    plot_fft(fft_freqs_butter, fft_result_butter, "Phổ tần số sau khi lọc Butterworth")

    # Áp dụng bộ lọc FIR
    filtered_signal_fir = apply_fir_filter(signal, cutoff, fs)

    # Hiển thị tín hiệu sau khi lọc FIR
    plot_signal(t, filtered_signal_fir, f"Tín hiệu sau khi lọc FIR (cutoff={cutoff} Hz)")

    # Thực hiện FFT sau khi lọc FIR
    fft_freqs_fir, fft_result_fir = perform_fft(filtered_signal_fir, fs)
    plot_fft(fft_freqs_fir, fft_result_fir, "Phổ tần số sau khi lọc FIR")
