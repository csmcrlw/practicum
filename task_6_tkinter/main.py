import tkinter as tk
import math

SPEED_INCREASE = 0.001
WIDTH = 600
HEIGHT = 600


class Canvas:
    def __init__(self, root):
        self.root = root
        self.root.title("Task 6 (tkinter)")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()

        self.radius = 200
        self.center_x = 300
        self.center_y = 300
        self.angle = 0
        self.speed = 0.03    # начальная скорость
        self.direction = 1  # при 1 движение против часовой стрелки, -1 - по часовой

        self.canvas.bind("<B1-Motion>", self.draw_on_canvas)    # добавляем холсту возможность вызова метода рисования при нажатии левой кнопки мыши
        self.draw_circle()
        self.draw_moving_point()

        self.add_buttons()
        self.draw_circle()
        self.draw_moving_point()

    def add_buttons(self):
        # кнопки для увеличения/уменьшения скорости и изменения направления движения точки
        buttons = [
            ("Change direction", self.change_direction),
            ("Increase speed", self.increase_speed),
            ("Decrease speed", self.decrease_speed),
        ]

        self.buttons = {}
        for text, command in buttons:
            btn = tk.Button(self.root, text=text, command=command)
            btn.pack()
            self.buttons[text] = btn

    def change_speed(self, change):
        if self.speed > 0:
            self.speed += change
        else:
            self.speed -= change

        self.update_button_state()

    def decrease_speed(self):
        self.change_speed(-SPEED_INCREASE)

    def increase_speed(self):
        self.change_speed(SPEED_INCREASE)

    def change_direction(self):
        self.direction *= -1

    def update_button_state(self):
        if self.speed == 0:
            self.buttons["Decrease speed"]["state"] = "disabled"
            self.buttons["Change direction"]["state"] = "disabled"
            self.show_message("Speed is zero")
        else:
            self.buttons["Decrease speed"]["state"] = "normal"
            self.buttons["Change direction"]["state"] = "normal"
            self.show_message("")

    def show_message(self, message):
        self.canvas.delete("message")
        self.canvas.create_text(WIDTH // 2, HEIGHT - 20, text=message, tags="message")

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

        self.angle -= self.direction * self.speed
        self.root.after(10, self.draw_moving_point)

    def draw_on_canvas(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = Canvas(root)
    root.mainloop()
