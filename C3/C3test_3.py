'''
import numpy as np
import matplotlib.pyplot as plt

sfreq = 100000
slen = 100000
f = 2000
A = np.sqrt(2)
t = np.arange(slen) / sfreq
cos = A * np.cos(2 * np.pi * f * t)
#フーリエ変換してから強度（絶対値）出す
fft_cos = np.fft.fft(cos, norm = 'forward')
fft_freq = np.fft.fftfreq(fft_s.size, 1/sfreq)
#ピークを検出
np.abs(fft_cos).max()
'''
import numpy as np
import matplotlib.pyplot as plt

f = 2000          # 余弦波の周波数: 2 kHz
A = np.sqrt(2)    # 振幅
duration = 1.0    # 1秒分のデータを作成

# グラフにプロットするための結果を保存する空リスト
sfreq_list = []
peak_freq_list = []

# サンプリング周波数を1000Hzから10000Hzまで500Hz刻みでループ
for sfreq in np.arange(1000, 10500, 500):
    
    # 時間軸と余弦波データの生成
    # duration（1秒）分のデータ点数を用意する
    t = np.arange(int(sfreq * duration)) / sfreq
    cos = A * np.cos(2 * np.pi * f * t)
    
    # フーリエ変換
    fft_cos = np.fft.fft(cos, norm='forward')
    fft_freq = np.fft.fftfreq(fft_cos.size, 1/sfreq)
    
    # ヒントを使ったピーク周波数の検出
    # 1. argmax()で強度が最大となるインデックス（配列の何番目か）を取得
    peak_index = np.abs(fft_cos).argmax()
    # 2. そのインデックスを使って、対応する周波数を取得（念のため絶対値にする）
    peak_freq = np.abs(fft_freq[peak_index])
    
    # 取得した値をリストに追加
    sfreq_list.append(sfreq)
    peak_freq_list.append(peak_freq)

# --- ここからグラフ描画 ---
# 見やすくするため、HzをkHzに変換してプロット
plt.plot(np.array(sfreq_list) / 1000, np.array(peak_freq_list) / 1000, marker='o')
plt.xlabel('Sampling Frequency [kHz]')
plt.ylabel('Peak Frequency [kHz]')
plt.title('Relationship between Sampling Frequency and Peak Frequency')
plt.grid(True)
plt.show()