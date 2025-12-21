from plots_library import *


# Определяем интерполяционную функцию
def func(x, k, x_0):
    return k * (x - x_0)


# Функция аппроксимации методом наименьших квадратов для func()
def MLS_func(x, y, ye):
    # Начальные приближения для coefs
    initial_guess = [24, 0.9]  # Эти значения можно корректировать

    try:
        x_fit = x[:5]
        y_fit = y[:5]
        # Используем curve_fit для подбора параметров k и x_0
        params, covariance = curve_fit(func, x_fit, y_fit, p0=initial_guess, maxfev=5000, sigma=ye[:5],
                                       absolute_sigma=True)
        k, x_0 = params
        perr = np.sqrt(np.diag(covariance))  # ср.кв.отклонения для параметров

        print(f'Найденные параметры: k = {k}, x_0 = {x_0}')

        plt.errorbar(x, y, yerr=ye, color='b', fmt='o', label='Экспериментальные точки', capsize=3)

        # Создаем последовательность значений для аппроксимирующей кривой
        x_grid = np.linspace(min(x_fit), max(x_fit), 1000)
        y_grid = func(x_grid, k, x_0)

        plt.plot(x_grid, y_grid, label=f'$y$ = {round(k, 2)}($x$ - {round(x_0, 2)}$)$,', color='orange')
        plt.scatter([], [], color='None', label=f'где $x_0$ = {round(x_0, 3)}$\\pm${round(perr[1], 3)}')
        plt.xlabel(f'Мощность накачки $P_{{накач}}$, Вт', size=14)
        plt.ylabel(f'Мощность лазера $P_{{излуч}}$, мВт', size=14)
        plt.title(f'Интерполяция функцией вида $y = k(x - x_0)$', size=14)
        plt.legend(prop={'size': 14})
        plt.grid()
        plt.show()

    except RuntimeError as e:
        print(f"Ошибка: {e}")
        print("Попробуйте изменить начальные приближения для параметров или увеличить maxfev ещё больше.")


P = np.array([1.8, 4.5, 7.2, 9.6, 12.3, 17.0, 20.0, 23.0, 27.0, 30.0, 34.0, 36.0, 39.0, 42.0])  # Дж
I = np.array([0.98, 1.11, 1.22, 1.31, 1.42, 1.53, 1.6, 1.72, 1.82, 1.92, 2.05, 2.13, 2.21, 2.36])  # А

x = I * 6
y = P * 27
y_e = P * 0.18

MLS_func(x, y, y_e)
