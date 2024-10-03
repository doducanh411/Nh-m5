import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, firwin
from matplotlib.widgets import Button


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


# Lớp để quản lý các biểu đồ
class PlotManager:
    def __init__(self, fs, duration, freqs):
        self.fs = fs
        self.duration = duration
        self.freqs = freqs
        self.fig, self.ax = plt.subplots(2, 2, figsize=(10, 8))
        plt.subplots_adjust(bottom=0.2)

        # Tạo tín hiệu và FFT
        self.t, self.signal = generate_signal(fs, duration, freqs)
        self.cutoff = 100
        self.filtered_signal_butter = apply_butterworth_filter(self.signal, self.cutoff, fs)
        self.filtered_signal_fir = apply_fir_filter(self.signal, self.cutoff, fs)

        self.buttons = [None] * 3
        self.current_plot = 0

        # Tạo nút điều khiển
        self.create_buttons()
        self.plot_all()

    def create_buttons(self):
        # Tạo nút để chuyển đổi giữa các biểu đồ
        ax_button = plt.axes([0.1, 0.01, 0.2, 0.075])
        self.buttons[0] = Button(ax_button, 'Tín hiệu gốc')
        self.buttons[0].on_clicked(lambda event: self.update_plot(0))

        ax_button = plt.axes([0.35, 0.01, 0.2, 0.075])
        self.buttons[1] = Button(ax_button, 'Tín hiệu sau lọc Butterworth')
        self.buttons[1].on_clicked(lambda event: self.update_plot(1))

        ax_button = plt.axes([0.6, 0.01, 0.2, 0.075])
        self.buttons[2] = Button(ax_button, 'Tín hiệu sau lọc FIR')
        self.buttons[2].on_clicked(lambda event: self.update_plot(2))

    def update_plot(self, index):
        self.current_plot = index
        self.plot_all()

    def plot_all(self):
        for ax in self.ax.flat:
            ax.clear()

        if self.current_plot == 0:
            # Tín hiệu gốc
            self.ax[0, 0].plot(self.t, self.signal)
            self.ax[0, 0].set_title("Tín hiệu gốc")
            self.ax[0, 0].set_xlabel('Thời gian (giây)')
            self.ax[0, 0].set_ylabel('Biên độ')
            self.ax[0, 0].grid()

            # FFT của tín hiệu gốc
            fft_freqs, fft_result = perform_fft(self.signal, self.fs)
            self.ax[0, 1].plot(fft_freqs, fft_result)
            self.ax[0, 1].set_title("Phổ tần số của tín hiệu gốc")
            self.ax[0, 1].set_xlabel('Tần số (Hz)')
            self.ax[0, 1].set_ylabel('Biên độ')
            self.ax[0, 1].grid()

        elif self.current_plot == 1:
            # Tín hiệu sau lọc Butterworth
            self.ax[0, 0].plot(self.t, self.filtered_signal_butter)
            self.ax[0, 0].set_title(f"Tín hiệu sau khi lọc Butterworth (cutoff={self.cutoff} Hz)")
            self.ax[0, 0].set_xlabel('Thời gian (giây)')
            self.ax[0, 0].set_ylabel('Biên độ')
            self.ax[0, 0].grid()

            # FFT của tín hiệu sau lọc Butterworth
            fft_freqs_butter, fft_result_butter = perform_fft(self.filtered_signal_butter, self.fs)
            self.ax[0, 1].plot(fft_freqs_butter, fft_result_butter)
            self.ax[0, 1].set_title("Phổ tần số sau khi lọc Butterworth")
            self.ax[0, 1].set_xlabel('Tần số (Hz)')
            self.ax[0, 1].set_ylabel('Biên độ')
            self.ax[0, 1].grid()

        elif self.current_plot == 2:
            # Tín hiệu sau lọc FIR
            self.ax[0, 0].plot(self.t, self.filtered_signal_fir)
            self.ax[0, 0].set_title(f"Tín hiệu sau khi lọc FIR (cutoff={self.cutoff} Hz)")
            self.ax[0, 0].set_xlabel('Thời gian (giây)')
            self.ax[0, 0].set_ylabel('Biên độ')
            self.ax[0, 0].grid()

            # FFT của tín hiệu sau lọc FIR
            fft_freqs_fir, fft_result_fir = perform_fft(self.filtered_signal_fir, self.fs)
            self.ax[0, 1].plot(fft_freqs_fir, fft_result_fir)
            self.ax[0, 1].set_title("Phổ tần số sau khi lọc FIR")
            self.ax[0, 1].set_xlabel('Tần số (Hz)')
            self.ax[0, 1].set_ylabel('Biên độ')
            self.ax[0, 1].grid()

        plt.draw()


# Chương trình chính
if __name__ == "__main__":
    # Tạo tín hiệu
    fs = 1000  # Tần số lấy mẫu
    duration = 2.0  # Thời gian tín hiệu (giây)
    freqs = [50, 120]  # Tần số của các tín hiệu thành phần

    plot_manager = PlotManager(fs, duration, freqs)
    plt.show()
