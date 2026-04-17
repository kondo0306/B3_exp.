#周波数を変えてみる
import numpy as np
import matplotlib.pyplot as plt

# --- 基本設定 ---
T0 = 0
sfreq = 10000 
slen = 100000 
tau = 0.1     
t = (np.arange(slen) - slen / 2) / sfreq

# 矩形波の作成
def r(t):
    return np.where(np.abs(t - T0) <= tau / 2, 1, 0)

# フーリエ変換
fft_s_raw = np.fft.fft(r(t))
fft_freq = np.fft.fftfreq(slen, 1/sfreq)

# ローパスフィルタの関数
def H(fft_freq, W):
    return np.where(np.abs(fft_freq) <= W / 2, 1 + 0j, 0 + 0j)

# --- 比較する帯域 W のリスト [Hz] ---
W_list = [50, 100, 500]
colors = ['blue', 'green', 'red']
labels = ['W = 50 Hz (Narrow)', 'W = 100 Hz (Standard)', 'W = 500 Hz (Wide)']

plt.figure(figsize=(10, 6))

# ループでそれぞれの W について計算と描画を行う
for W, color, label in zip(W_list, colors, labels):
    # フィルタをかける
    filtered_spectrum_raw = fft_s_raw * H(fft_freq, W)
    
    # 逆フーリエ変換で時間波形に戻す（実数部を取得）
    filtered_time_signal = np.real(np.fft.ifft(filtered_spectrum_raw))
    
    # グラフにプロット
    plt.plot(t * 1e3, filtered_time_signal, '-', color=color, label=label)

# 元の矩形波も参考として薄いグレーの破線で描画
plt.plot(t * 1e3, r(t), '--', color='gray', alpha=0.5, label='Original Rectangular Pulse')

plt.xlim([-150, 150]) # パルス周辺にズーム
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude')
plt.title('Filtered Time Waveforms with Different Bandwidths W')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()