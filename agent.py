import pygame
from drawable import Drawable


class Agent(Drawable):
    def __init__(self, pos_x, pos_y, width, height, vel_x=0, vel_y=0):
        super().__init__(pos_x, pos_y, width, height)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.accel_x = 0
        self.accel_y = 0
        self.collidable = True
        self.collideCountdown = 0

    def update(self):
        self.vel_x += self.accel_x
        self.vel_y += self.accel_y
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        if self.collideCountdown != 0:
            self.collideCountdown -= 1
        if self.collideCountdown == 0:
            self.collidable = True

    def setNotCollidable(self, timeSteps=10):
        self.collidable = False
        self.collideCountdown = timeSteps

    def collided(self, other):
        if not isinstance(other, Agent):
            return False

        if not other.collidable:
            return False

        if (
            self.pos_x + self.width > other.pos_x
            and self.pos_x < other.pos_x + other.width
        ):
            if (
                self.pos_y + self.height > other.pos_y
                and self.pos_y < other.pos_y + other.height
            ):
                return True
        return False