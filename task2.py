import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції


def f(x):
    return x ** 2


# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло для обчислення інтегралу


def monte_carlo_integration(f, a, b, num_points=10000):
    x_random = np.random.uniform(a, b, num_points)
    y_random = np.random.uniform(
        0, max(f(np.linspace(a, b, num_points))), num_points)

    under_curve = y_random < f(x_random)
    integral = (b - a) * max(f(np.linspace(a, b, num_points))) * \
        np.mean(under_curve)

    return integral


# Обчислення інтегралу методом Монте-Карло
mc_result = monte_carlo_integration(f, a, b)
print(f"Інтеграл методом Монте-Карло: {mc_result}")

# Обчислення інтегралу за допомогою quad
result_quad, error = spi.quad(f, a, b)
print(f"Інтеграл за допомогою quad: {result_quad}, з похибкою: {error}")

# Візуалізація результату
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
