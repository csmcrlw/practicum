""" Реализация основного функционала камер """

from base import Camera


class DSLRCamera(Camera):
    def take_photo(self):
        print("Taking photo with DSLR Camera")

    def record_video(self):
        print("Recording video with DSLR Camera")


class MirrorlessCamera(Camera):
    def take_photo(self):
        print("Taking photo with Mirrorless Camera")

    def record_video(self):
        print("Recording video with Mirrorless Camera")
