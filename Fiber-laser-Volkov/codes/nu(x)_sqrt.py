import numpy as np

from plots_library import *

k_legend_accuracy = 3  # кол-во знаков после зпт в легенде для коэффициента k
c_legend_accuracy = 3  # кол-во знаков после зпт в легенде для коэффициента c
k_info_accuracy = 3  # кол-во знаков после зпт в выводе информации для коэффициента k
c_info_accuracy = 3  # кол-во знаков после зпт в выводе информации для коэффициента c
sigma_k_info_accuracy = 3  # кол-во знаков после зпт в выводе информации для погрешности коэффициента k
sigma_c_info_accuracy = 3  # кол-во знаков после зпт в выводе информации для погрешности коэффициента c


I = np.array([1.19, 1.49, 1.76, 1.89, 2.03, 2.23])
T = np.array([27.18, 20.97, 18.16, 17.2, 15.62, 14.52])  # мкс
sigma_T = np.array([0.85, 0.46, 0.66, 0.25, 0.45, 0.37])
nu = 1 / T

x = I / 0.91
y = nu * 1000                 # кГц
ye = 1000 * nu * sigma_T / T  # кГц


# Модель линейной зависимости: y = k(x-1)^0.5
def linear_model(x, k):
    return k * np.sqrt(x - 1)


# Оценка параметров с учетом весов (1 / ye^2)
popt, pcov = curve_fit(linear_model, x, y, p0=[74], sigma=ye, absolute_sigma=True)
k = popt[0]
sigma_k = np.sqrt(np.diag(pcov))

x_grid = np.linspace(min(x), max(x), 200)

plt.errorbar(x, y, yerr=ye, color='b', fmt='o', label=f'Экспериментальные точки', capsize=3)
plt.plot(x_grid, linear_model(x_grid, k), label=f'y = {k:.2f}$\\sqrt{{x - 1}}$', color='orange')


plt.xlabel(f'Превышение над порогом $x$', size=14)
plt.ylabel(f'Частота релаксационных колебаний $\\nu$, кГц', size=14)
plt.title(f'График зависимости $\\nu(x)$, построенный взвешенным МНК', size=14)
plt.legend(prop={'size': 14})  # создание легенды
plt.grid()  # создание сетки


plt.show()
