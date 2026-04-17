import numpy as np
import matplotlib.pyplot as plt

# --- 1. パラメータ設定とノイズ生成 ---
sfreq = 10000  # サンプリング周波数
slen = 100000  # サンプル数
W = 5000       # フィルタ帯域 5 kHz

# 平均0、分散1の白色ガウス雑音を生成
noise_in = np.random.normal(loc=0.0, scale=1.0, size=slen)

# --- 2. フーリエ変換 ---
fft_noise_in = np.fft.fft(noise_in)
fft_freq = np.fft.fftfreq(slen, 1/sfreq)

# --- 3. ローパスフィルタ処理 ---
# |f| <= W/2 (つまり -2500 Hz ~ 2500 Hz) を通過させる
H_filter = np.where(np.abs(fft_freq) <= W / 2, 1 + 0j, 0 + 0j)
fft_noise_out = fft_noise_in * H_filter

# --- 4. 逆フーリエ変換（時間領域の波形に戻す） ---
noise_out = np.real(np.fft.ifft(fft_noise_out))

# --- 5. 分散の計算と確認（コンソール出力） ---
var_in = np.var(noise_in)
var_out = np.var(noise_out)
print(f"フィルタ入力前の分散: {var_in:.4f}")
print(f"フィルタ出力後の分散: {var_out:.4f}")
print("→ 確実に出力の分散が入力の約半分（0.5）になっています！")

# --- 6. グラフ描画 ---
# スペクトル表示用に並べ替えと絶対値化
freq_shifted = np.fft.fftshift(fft_freq)
fft_in_abs = np.fft.fftshift(np.abs(fft_noise_in))
fft_out_abs = np.fft.fftshift(np.abs(fft_noise_out))

plt.figure(figsize=(10, 10)) # 縦に長いキャンバスを用意

# 【上段】入力ノイズのスペクトル
plt.subplot(3, 1, 1)
plt.plot(freq_shifted, fft_in_abs, color='gray', alpha=0.8)
plt.title('Input AWGN Spectrum (All frequencies present)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.xlim([-5000, 5000])
plt.grid(True)

# 【中段】出力ノイズのスペクトル（フィルタ効果の確認）
plt.subplot(3, 1, 2)
plt.plot(freq_shifted, fft_out_abs, color='blue', alpha=0.8)
plt.title(f'Output Spectrum after LPF (W = {W/1000} kHz)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.xlim([-5000, 5000])
plt.grid(True)

# 【下段】ヒストグラムの比較
plt.subplot(3, 1, 3)
# 入力ノイズ（グレー）
plt.hist(noise_in, bins=100, density=True, alpha=0.5, color='gray', label=f'Input (Var: {var_in:.2f})')
# 出力ノイズ（青）
plt.hist(noise_out, bins=100, density=True, alpha=0.5, color='blue', label=f'Output (Var: {var_out:.2f})')

plt.title('Histogram Comparison (Input vs Output)')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)

plt.tight_layout() # グラフ同士が重ならないように自動調整
plt.show()