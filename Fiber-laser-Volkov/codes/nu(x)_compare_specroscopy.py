import numpy as np

from plots_library import *

k_legend_accuracy = 3  # кол-во знаков после зпт в легенде для коэффициента k
c_legend_accuracy = 3  # кол-во знаков после зпт в легенде для коэффициента c
k_info_accuracy = 3  # кол-во знаков после зпт в выводе информации для коэффициента k
c_info_accuracy = 3  # кол-во знаков после зпт в выводе информации для коэффициента c
sigma_k_info_accuracy = 3  # кол-во знаков после зпт в выводе информации для погрешности коэффициента k
sigma_c_info_accuracy = 3  # кол-во знаков после зпт в выводе информации для погрешности коэффициента c


I = np.array([1.18, 1.28, 1.39, 1.47, 1.56, 1.64, 1.75, 1.84, 1.97, 2.08])  # A
nu = np.array([22.25, 27.86, 31.52, 33.72, 37.14, 38.85, 42.02, 45.7, 49.35, 51.54])  # кГц


x = I / 0.91
y = nu

# ----------------------------------------------------------------------------------------------------------------------


# Модель линейной зависимости: y = kx + b
def linear_model(x, k1, b):
    return k1 * x + b


popt, pcov = curve_fit(linear_model, x, y)
k, b = popt
sigma_k, sigma_b = np.sqrt(np.diag(pcov))

plt.plot(x, linear_model(x, k, b), label=f'$y = {k:.2f}x + {b:.2f}$ - наблюдаемая зависимость', color='orange')

# ----------------------------------------------------------------------------------------------------------------------


# Модель линейной зависимости: y = k(x-1)^0.5
def sqrt_model(x, k0):
    return k0 * np.sqrt(x - 1)


popt_sqrt, pcov_sqrt = curve_fit(sqrt_model, x, y, p0=[57])
k_sqrt = popt_sqrt[0]
sigma_k_sqrt = np.sqrt(np.diag(pcov_sqrt))

x_grid = np.linspace(min(x), max(x), 200)

plt.plot(x_grid, sqrt_model(x_grid, k_sqrt), label=f'y = {k_sqrt:.2f}$\\sqrt{{x - 1}}$ - ожидаемая зависимость',
         color='c', linestyle='dashed')

# ----------------------------------------------------------------------------------------------------------------------

plt.errorbar(x, y, color='b', fmt='o', label=f'Экспериментальные точки', capsize=3)

plt.xlabel(f'Превышение над порогом $x$', size=14)
plt.ylabel(f'Частота релаксационных колебаний $\\nu$, кГц', size=14)
plt.title(f'График зависимости $\\nu(x)$', size=14)
plt.legend(prop={'size': 14})  # создание легенды
plt.grid()  # создание сетки


plt.show()
