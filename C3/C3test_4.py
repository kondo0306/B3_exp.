#3.2(1)矩形信号を出す
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

plt.plot(t * 1e3, r(t), '-', label = '')
#plt.legend(loc = 'upper right')
plt.xlim([-5000, 5000])
#plt.xlabel('Amplitude')
#plt.ylabel('Time [ms]')
plt.show()