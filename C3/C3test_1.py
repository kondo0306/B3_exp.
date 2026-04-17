#3.1(1)sin波の出力、プロット
import numpy as np
import matplotlib.pyplot as plt
sfreq = 100000
slen = 100000
f = 2000
A = np.sqrt(2)
t = np.arange(slen) / sfreq
s = A * np.sin(2 * np.pi * f * t)
plt.plot(t * 1e3, s, '--', label = 'Sample(sfreq = 100 kHz)')
plt.legend(loc = 'upper right')
plt.xlim([0, 2])
plt.xlabel('Amplitude')
plt.ylabel('Time [ms]')
plt.show()