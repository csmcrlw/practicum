import tkinter as tk
import math


class Canvas:
    def __init__(self, root):
        self.root = root
        self.root.title("Задание 6 (tkinter)")
        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack()

        self.radius = 200
        self.center_x = 300
        self.center_y = 300
        self.angle = 0       # направление движения
        self.speed = 0.03    # скорость

        self.canvas.bind("<B1-Motion>", self.draw_on_canvas)    # добавляем холсту возможность вызова метода рисования при нажатии левой кнопки мыши
        self.draw_circle()
        self.draw_moving_point()

    def draw_circle(self):
        x0 = self.center_x - self.radius
        y0 = self.center_y - self.radius
        x1 = self.center_x + self.radius
        y1 = self.center_y + self.radius
        self.canvas.create_oval(x0, y0, x1, y1, outline="black")

    def draw_moving_point(self):
        x = self.center_x + self.radius * math.cos(self.angle)
        y = self.center_y + self.radius * math.sin(self.angle)
        self.canvas.delete("point")
        self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="orange", tags="point")

        self.angle += self.speed
        self.root.after(10, self.draw_moving_point)

    def draw_on_canvas(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = Canvas(root)
    root.mainloop()
