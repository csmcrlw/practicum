""" Основной модуль, использующий паттерн 'Мост' """

from camera_functions import DSLRCamera, MirrorlessCamera
from camera_control import ButtonControl, TouchScreenControl


def main():
    dslr_camera = DSLRCamera(ButtonControl())
    dslr_camera.take_photo()
    dslr_camera.record_video()
    print()
    mirrorless_camera = MirrorlessCamera(TouchScreenControl())
    mirrorless_camera.take_photo()
    mirrorless_camera.record_video()


if __name__ == "__main__":
    main()
