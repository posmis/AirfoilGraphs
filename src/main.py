import numpy as np
import matplotlib.pyplot as plt
import os

# Исходные данные
m = 8
V = 39
L_k = 0.45
b_k = 0.11
S_k = L_k * b_k
S_go = S_k * 2
S_kr = S_k * 2
L_go = 0.298
b_a = b_k
# Константы
g = 9.81
ro = 1.225

# Задание относительного пути к файлу
relative_file_path = 'graphs_data/NASA_2210_Cy_alpha.csv'
# Получение абсолютного пути к файлу
file_path = os.path.join(os.getcwd(), relative_file_path)


# Чтение файла и замена запятых на точки
with open(file_path, 'r') as file:
    data = file.read().replace(',', '.')
# Сохранение изменённого файла
with open(file_path, 'w') as file:
    file.write(data)
# Загрузка данных из изменённого файла
data = np.loadtxt(file_path, delimiter=';', skiprows=1)

# Извлечение углов атаки и коэффициентов подъёмной силы
alpha = data[:, 0]
cl = data[:, 1]

# Расчет
Y_mg = m * g
Y_cy = cl * (ro * pow(V, 2) / 2)
S = Y_mg / Y_cy
S_pot = S / 4
A_go = (S_go * L_go) / (S_kr * b_a)
mask = S >= 0

# Апроксимация
coefficient = np.polyfit(alpha[mask], S_pot[mask], len(S_pot[mask]) - 1)
p = np.poly1d(coefficient)
x_1 = np.linspace(alpha.min(), alpha.max(), 100)
y_1 = p(x_1)

# Построение графика
plt.scatter(alpha[mask], S_pot[mask], label='Data points')
plt.plot(x_1, y_1, color='orange',label=f'Polynomial fit')
plt.xlabel('Angle of Attack (degrees)')
plt.ylabel('Required wing area (S)')
plt.title('S_pot vs. Angle of Attack for NACA 23009')

for i in range(len(alpha)):
    plt.text(alpha[i], S_pot[i], f'{S_pot[i]:.3f}', fontsize=8, ha='right')

plt.legend()
plt.grid(True)
plt.show()
