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

# ----------------------------------------------------------------------------------------------------------------------


# Модель линейной зависимости: y = kx + b
def linear_model(x, k1, b):
    return k1 * x + b


# Оценка параметров с учетом весов (1 / ye^2)
popt, pcov = curve_fit(linear_model, x, y, sigma=ye, absolute_sigma=True)
k, b = popt
sigma_k, sigma_b = np.sqrt(np.diag(pcov))

plt.plot(x, linear_model(x, k, b), label=f'$y = {k:.2f}x + {b:.2f}$ - наблюдаемая зависимость', color='orange')

# ----------------------------------------------------------------------------------------------------------------------


# Модель линейной зависимости: y = k(x-1)^0.5
def sqrt_model(x, k0):
    return k0 * np.sqrt(x - 1)


# Оценка параметров с учетом весов (1 / ye^2)
popt_sqrt, pcov_sqrt = curve_fit(sqrt_model, x, y, p0=[74], sigma=ye, absolute_sigma=True)
k_sqrt = popt_sqrt[0]
sigma_k_sqrt = np.sqrt(np.diag(pcov_sqrt))

x_grid = np.linspace(min(x), max(x), 200)

plt.plot(x_grid, sqrt_model(x_grid, k_sqrt), label=f'y = {k_sqrt:.2f}$\\sqrt{{x - 1}}$ - ожидаемая зависимость',
         color='c', linestyle='dashed')

# ----------------------------------------------------------------------------------------------------------------------

plt.errorbar(x, y, yerr=ye, color='b', fmt='o', label=f'Экспериментальные точки', capsize=3)

plt.xlabel(f'Превышение над порогом $x$', size=14)
plt.ylabel(f'Частота релаксационных колебаний $\\nu$, кГц', size=14)
plt.title(f'График зависимости $\\nu(x)$, построенный взвешенным МНК', size=14)
plt.legend(prop={'size': 14})  # создание легенды
plt.grid()  # создание сетки


plt.show()
