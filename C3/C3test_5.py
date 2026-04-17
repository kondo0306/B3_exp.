import numpy as np
import matplotlib.pyplot as plt

T0 = 0
sfreq = 10000 #サンプリング周波数
slen = 100000 #サンプリング数
tau = 0.1 #時間幅100ms
t = (np.arange(slen) - slen / 2) / sfreq
def r(t):
    # t-T0の絶対値が tau/2 以下なら 1、そうでないなら 0 を返す
    return np.where(np.abs(t - T0) <= tau / 2, 1, 0)
#フーリエ変換してから絶対値
fft_s = np.fft.fft(r(t)) * (1 / sfreq)
fft_s_abs = np.abs(fft_s)

# 周波数軸の作成
fft_freq = np.fft.fftfreq(slen, 1/sfreq)

# グラフ描画のために、周波数とFFT結果をマイナスからプラスへ順番通りに並べ替える
freq_shifted = np.fft.fftshift(fft_freq)
fft_s_abs_shifted = np.fft.fftshift(fft_s_abs)
# --- 2. 数学的な解析解の計算 ---
# R(f) = tau * sinc(f * tau)
# ※np.sinc(x) は sin(pi*x)/(pi*x) を計算してくれる関数です
analytical_R = tau * np.sinc(freq_shifted * tau)
analytical_R_abs = np.abs(analytical_R)


# --- グラフの描画 ---
# FFTの結果（青い実線）
plt.plot(freq_shifted, fft_s_abs_shifted, '-', label='FFT (Numerical)')

# 解析解の結果（赤い破線）
plt.plot(freq_shifted, analytical_R_abs, '--', color='red', label='Analytical R(f)')

plt.legend(loc='upper right')
# Sinc関数の波打ちがよく見えるように -100Hz から 100Hz にズーム
plt.xlim([-100, 100])
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.title('Fourier Transform of Rectangular Pulse')
plt.grid(True)
plt.show()