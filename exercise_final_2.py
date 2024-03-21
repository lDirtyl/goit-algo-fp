import matplotlib.pyplot as plt
import numpy as np

def draw_branch(x, y, angle, depth):
    if depth == 0:
        return
    
    # Визначаємо довжину гілки в залежності від глибини
    branch_length = depth * 10
    
    # Кінцеві координати гілки
    x_end = x + branch_length * np.cos(np.radians(angle))
    y_end = y + branch_length * np.sin(np.radians(angle))
    
    # Малюємо гілку
    plt.plot([x, x_end], [y, y_end], 'brown')
    
    # Викликаємо функцію рекурсивно для створення наступних гілок
    # Відхилення кута для нових гілок
    angle_diff = 45
    
    draw_branch(x_end, y_end, angle - angle_diff, depth - 1)
    draw_branch(x_end, y_end, angle + angle_diff, depth - 1)

# Запитуємо у користувача глибину рекурсії
depth = int(input("Будь ласка, введіть глибину рекурсії для дерева Піфагора: "))

# Налаштування вікна для малювання
plt.figure(figsize=(8, 8))
plt.axis('off')

# Викликаємо функцію для малювання дерева з початковою точкою внизу по центру
draw_branch(x=0, y=0, angle=90, depth=depth)

plt.show()
