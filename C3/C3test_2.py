#3.1(3)フーリエ変換して強度出した
import numpy as np
import matplotlib.pyplot as plt

sfreq = 100000
slen = 100000
f = 2000
A = np.sqrt(2)
t = np.arange(slen) / sfreq
s = A * np.sin(2 * np.pi * f * t)
#
intensity = s ** 2
energy = (intensity * 1 / sfreq).sum()
power = (energy) / (slen / sfreq)
power_theory = A ** 2 / 2 #パーセバルの定理
energy_theory = power_theory * slen / sfreq
ave_intensity = intensity.mean()
#フーリエ変換してから強度（絶対値）出す
fft_s = np.abs(np.fft.fft(s, norm = 'forward'))
fft_freq = np.fft.fftfreq(fft_s.size, 1/sfreq)
#強度の平均
print(np.sum(fft_s**2))

#プロット・表示
plt.xlim([-3000, 3000])
plt.plot(fft_freq, fft_s)
plt.show()