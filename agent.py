import pygame
from drawable import Drawable


class Agent(Drawable):
    def __init__(self, pos_x, pos_y, width, height, vel_x=0, vel_y=0):
        super().__init__(pos_x, pos_y, width, height)
        self.vel_x = vel_x
        self.vel_y = vel_y

    def update(self):
        pass
        