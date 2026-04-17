#3.2(2)(1)にLPFを通す
'''
方針
r(t)をフーリエ変換
H(f)を通す(フーリエ(r(t))*H(f)を出す)

'''
'''
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

W = 100 #フィルタ帯域[Hz]
#ローパスフィルター
def H(fft_freq, W):
    return np.where(np.abs(fft_freq) <= W / 2, 1 + 0j, 0 + 0j)

#スペクトル通す
filtered_spectrum = fft_s * H(fft_freq, W)

# --- グラフの描画 ---
# FFTの結果（青い実線）
plt.plot(freq_shifted, filtered_spectrum, '-', label='FFT (Numerical)')

plt.legend(loc='upper right')
plt.xlim([-100, 100])
plt.grid(True)
plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt

T0 = 0
sfreq = 10000 # サンプリング周波数
slen = 100000 # サンプリング数
tau = 0.1     # 時間幅100ms

t = (np.arange(slen) - slen / 2) / sfreq

def r(t):
    return np.where(np.abs(t - T0) <= tau / 2, 1, 0)

# フーリエ変換
# ※逆変換でスケールを戻しやすくするため、(1/sfreq)の係数は後で掛けます
fft_s_raw = np.fft.fft(r(t))
fft_freq = np.fft.fftfreq(slen, 1/sfreq)

W = 100 # フィルタ帯域[Hz]

def H(fft_freq, W):
    return np.where(np.abs(fft_freq) <= W / 2, 1 + 0j, 0 + 0j)

# スペクトルを通す (ここでローパスフィルタを掛ける)
filtered_spectrum_raw = fft_s_raw * H(fft_freq, W)


# --- 1. スペクトル波形用のデータ準備 ---
# ここで振幅スケールを合わせ、絶対値を取り、グラフ用に並べ替える
filtered_spectrum_scaled = filtered_spectrum_raw * (1 / sfreq)
filtered_spectrum_abs_shifted = np.fft.fftshift(np.abs(filtered_spectrum_scaled))
freq_shifted = np.fft.fftshift(fft_freq)


# --- 2. 時間波形用のデータ準備（逆フーリエ変換） ---
# np.fft.ifft() で時間領域に戻します。
# 課題文の「実数となることに注意せよ」に従い、np.real() で実数部分だけを取り出します。
filtered_time_signal = np.real(np.fft.ifft(filtered_spectrum_raw))


# --- グラフの描画 ---
plt.figure(figsize=(10, 8))

# 上段：絶対値振幅スペクトル波形
plt.subplot(2, 1, 1)
plt.plot(freq_shifted, filtered_spectrum_abs_shifted, '-')
plt.xlim([-150, 150]) # W=100 なので ±150 くらいが見やすいです
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.title('Filtered Spectrum')
plt.grid(True)

# 下段：フィルタ出力時間波形
plt.subplot(2, 1, 2)
plt.plot(t * 1e3, filtered_time_signal, '-')
plt.xlim([-200, 200]) # パルス周辺の ±200ms にズーム
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude')
plt.title('Filtered Time Waveform (Inverse FFT)')
plt.grid(True)

plt.tight_layout()
plt.show()