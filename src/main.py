import numpy as np
import matplotlib.pyplot as plt

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

# Считывание пути к файлу из консоли
file_path = input("Введите путь к файлу: ")
#C:\Users\posmis\PycharmProjects\Airfoills Graphs\graphs_data\NASA_2210_Cy_alpha.csv
#file_path='C:\Users\posmis\PycharmProjects\Airfoills Graphs\graphs_data\NASA_2210_Cy_alpha.csv'

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
coefficient = np.polyfit(alpha[mask], S_pot[mask], len(alpha[mask]))
p = np.poly1d(coefficient)
x = np.linspace(alpha.min(), alpha.max(), 100)
y = p(x)
print(p)

# Построение графика
plt.plot(alpha[mask], S_pot[mask], x, y)
plt.xlabel('Angle of Attack (degrees)')
plt.ylabel('Required wing area (S)')
plt.title('S_pot vs. Angle of Attack for NACA 23009')

for i in range(len(alpha)):
    plt.text(alpha[i], S_pot[i], f'{S_pot[i]:.2f}', fontsize=8, ha='right')

plt.legend()
plt.grid(True)
plt.show()
