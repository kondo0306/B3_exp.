import numpy as np
import matplotlib.pyplot as plt

# --- 1. パラメータの設定 ---
sfreq = 10000       # サンプリング周波数 10 kHz
slen = 100000       # サンプル数 10^5 (10万個)

# --- 2. 白色ガウス雑音 (AWGN) の生成 ---
# 平均(loc)0、標準偏差(scale)1（分散1の標準偏差は1）の乱数を生成
noise = np.random.normal(loc=0.0, scale=1.0, size=slen)

# --- 3. パワーと分散の計算と確認 ---
# 分散 (Variance) の計算
noise_var = np.var(noise)

# パワー (Power) の計算：各サンプルの2乗の平均
noise_power = np.mean(noise**2)

print(f"計算された分散: {noise_var}")
print(f"計算されたパワー: {noise_power}")
print("→ パワーと分散がほぼ等しいことが確認できます！")

# --- 4. グラフの描画準備 ---
plt.figure(figsize=(10, 6))

# --- 5. ヒストグラムの描画 ---
# density=True を指定することで、縦軸が「度数(回数)」ではなく「確率密度(面積の合計が1)」になります
# これをしないと、理論値の曲線と高さが合いません
plt.hist(noise, bins=100, density=True, alpha=0.6, color='blue', label='AWGN Histogram')

# --- 6. ガウス分布（理論値）の曲線の描画 ---
# -4 から 4 くらいまでの滑らかな横軸データを作る
x = np.linspace(-4, 4, 1000)

# ヒントの式を使って確率密度関数の理論値を計算
p = np.exp(-1 * (x - 0)**2 / (2 * 1)) / np.sqrt(2 * np.pi)

# 理論値を赤い線で重ねて描画
plt.plot(x, p, 'r-', linewidth=2, label='Theoretical Gaussian N(0, 1)')

# --- グラフの仕上げ ---
plt.title('Histogram of AWGN and Theoretical Gaussian Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()