import pygame
from drawable import Drawable


class Agent(Drawable):
    def __init__(self, pos_x, pos_y, width, height, vel_x=0, vel_y=0):
        super().__init__(pos_x, pos_y, width, height)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.accel_x = 0
        self.accel_y = 0

    def collided(self, player):
        if (self.pos_x < player.pos_x + player.width and self.pos_x + self.width > player.pos_x and self.pos_y < player.pos_y + player.height and self.pos_y + self.height > player.pos_y):
            return True

    def update(self):
        self.vel_x += self.accel_x
        self.vel_y += self.accel_y
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y