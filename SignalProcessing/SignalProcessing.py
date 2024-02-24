import numpy
import scipy
from matplotlib import pyplot as plt

n = 500
Fs = 1000

rand = numpy.random.normal(0, 10, n)

x = numpy.arange(n) / Fs

F_max = 35
w = F_max / (Fs / 2)

parameters_filter = scipy.signal.butter(3, w, 'low', output='sos')

y = scipy.signal.sosfiltfilt(parameters_filter, rand)

fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
# ax.plot(x, y, linewidth=1)
ax.set_xlabel("Час (секунди)", fontsize=14)
ax.set_ylabel("Амплітуда спектру", fontsize=14)
plt.title("Сигнал з максимальною частотою F_max = 15 Гц", fontsize=14)

spectrum = scipy.fft.fft(y)

y1 = numpy.abs(scipy.fft.fftshift(spectrum))

fm = scipy.fft.fftfreq(n, 1 / n)  # частотні відліки

x1 = scipy.fft.fftshift(fm)

plt.plot(x1, y1)

ax.set_xlabel("Частота (Гц)", fontsize=14)

fig.savefig('./figures/' + 'title2' + '.png')
plt.show()
