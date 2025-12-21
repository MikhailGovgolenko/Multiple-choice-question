from plots_library import *


file_path = 'C:/Users/mamki/OneDrive/Рабочий стол/Учеба/5 семестр/Фотоника/Волоконный лазер/данные/beats_2,23.txt'

# Считываем файл, пропуская заголовок и ненужные строки
data = pd.read_csv(file_path, skiprows=9, sep=r'\s+', names=['N', 'CH1', 'CH2'])


time = data['N'].to_numpy() * 50 / 125
amplitude = data['CH1'].to_numpy() * 0.15 / 32


# Вычисляем период колебаний T
peak_times = [587.6, 602.6, 617.2, 632, 646.2, 660.2]
peak_amplitudes = [1.1954, 0.975, 0.8671, 0.8016, 0.7642, 0.7407]
periods = np.diff(peak_times)  # Разница между соседними пиками
T = np.mean(periods)  # Средний период
print(f"Период колебаний T: {T:.2f}+-{np.std(periods):.2f} мкс")

# Вычисляем характерное время затухания tau
log_amplitudes = np.log(peak_amplitudes)
linear_fit = np.polyfit(peak_times, log_amplitudes, 1)  # Линейная регрессия
tau = -1 / linear_fit[0]  # Характерное время затухания
print(f"Характерное время затухания τ: {tau:.3f} мкс")

# Визуализация
plt.plot(time, amplitude, label="Осциллограмма")
plt.plot(peak_times, peak_amplitudes, 'ro', label="Пики")


plt.xlabel(f'$t$, мкс', size=14)
plt.ylabel(f'$U$, В', size=14)
plt.title(f'Осциллограмма при токе накачки $I$ = 2,23 А', size=14)
plt.xlim([560, 860])
plt.legend(prop={'size': 14})
plt.grid()

plt.show()
