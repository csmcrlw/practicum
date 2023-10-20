""" Модуль, содержащий базовые классы и интерфейсы """


class Camera:
    def __init__(self, control):
        self._control = control

    def take_photo(self):
        pass

    def record_video(self):
        pass


class Control:
    def operate(self):
        pass
