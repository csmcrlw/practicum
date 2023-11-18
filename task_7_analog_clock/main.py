import tkinter as tk
import math
from time import strftime
import ephem
from datetime import date


class DateWindow(tk.Label):
    def __init__(self, parent=None, **kwargs):
        tk.Label.__init__(self, parent, **kwargs)
        self.date_label = tk.Label(self, text="Дата: ")
        self.date_label.pack()
        self.update_date()

    def update_date(self):
        current_date = date.today().strftime('%d.%m.%Y')
        self.date_label.config(text=f"Дата: {current_date}")
        self.after(1000, self.update_date)


class AnalogClock(tk.Canvas):
    def __init__(self, parent=None, **kwargs):
        tk.Canvas.__init__(self, parent, width=300, height=300, bg='black', **kwargs)
        self.hour_hand = self.create_line(150, 150, 150, 100, width=6, fill='pale green')
        self.minute_hand = self.create_line(150, 150, 150, 90, width=6, fill='blue violet')
        self.second_hand = self.create_line(150, 150, 150, 60, width=6, fill='pink')
        self.center_circle = self.create_oval(147, 147, 153, 153, fill='white')
        self.moon_phase_label = tk.Label(parent, bd=1, relief='groove')
        self.moon_phase_label.pack()
        self.display_time()

    def display_time(self):
        current_time = strftime('%H:%M:%S')
        hours, minutes, seconds = map(int, current_time.split(':'))

        hour_angle = 90 - hours * 30 - minutes / 2
        minute_angle = 90 - minutes * 6
        second_angle = 90 - seconds * 6

        self.coords(self.hour_hand, 150, 150, 150 + 50 * math.cos(math.radians(hour_angle)), 150 - 50 * math.sin(math.radians(hour_angle)))
        self.coords(self.minute_hand, 150, 150, 150 + 60 * math.cos(math.radians(minute_angle)), 150 - 60 * math.sin(math.radians(minute_angle)))
        self.coords(self.second_hand, 150, 150, 150 + 70 * math.cos(math.radians(second_angle)), 150 - 70 * math.sin(math.radians(second_angle)))

        moon_phase = self.calculate_moon_phase()
        self.moon_phase_label.config(text=f"Фаза Луны: {moon_phase}")

        self.after(1000, self.display_time)

    def calculate_moon_phase(self):
        observer = ephem.Observer()
        observer.date = ephem.now()
        moon = ephem.Moon(observer)
        phase = moon.phase

        if 0 <= phase < 7.4:
            return "Новолуние"
        elif 7.4 <= phase < 14.8:
            return "Убывающая (первая четверть)"
        elif 14.8 <= phase < 22.1:
            return "Растущая (первая четверть)"
        elif 22.1 <= phase < 29.5:
            return "Полнолуние"
        elif 29.5 <= phase < 36.8:
            return "Растущая (последняя четверть)"
        elif 36.8 <= phase < 44.1:
            return "Убывающая (последняя четверть)"
        else:
            return "Новолуние"


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Задание 7 (анимация часов)")

    date_window = DateWindow(root, bd=1, relief='groove')
    date_window.pack()

    analog_clock = AnalogClock(root)
    analog_clock.pack()

    root.mainloop()
