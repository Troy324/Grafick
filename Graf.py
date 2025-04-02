import tkinter as tk

def draw_parabola():
    canvas.delete("all")  # Очищаем холст

    width = 600
    height = 400
    scale = 40  # Масштаб (пикселей на единицу)
    offset_x, offset_y = width // 2, height // 2  # Центр координат

    # Рисуем оси X и Y
    canvas.create_line(0, offset_y, width, offset_y, fill="black", width=2)  # Ось X
    canvas.create_line(offset_x, 0, offset_x, height, fill="black", width=2)  # Ось Y

    # Рисуем параболу y = x²/2 - 2
    points = []
    for x_px in range(width):
        x = (x_px - offset_x) / scale  # Переводим в математические координаты
        y = (x ** 2) / 2 - 2  # Формула параболы y = x²/2 - 2
        y_px = offset_y - y * scale  # Переводим обратно в пиксели
        points.append((x_px, y_px))

    canvas.create_line(points, fill="blue", width=4)  # Рисуем линию

    # Подписываем график
    canvas.create_text(50, 20, text="y = x²/2 - 2", font=("Times New Roman", 16), fill="blue")

# Создаем окно
root = tk.Tk()
root.title("График")

# Холст для рисования
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Рисуем сразу при запуске
draw_parabola()

root.mainloop()