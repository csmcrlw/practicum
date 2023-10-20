""" Реализация функций контроля камеры с помощью кнопок """

from base import Control


class ButtonControl(Control):
    def operate(self):
        print("Using Button Control")


class TouchScreenControl(Control):
    def operate(self):
        print("Using Touch Screen Control")
