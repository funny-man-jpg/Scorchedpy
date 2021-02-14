import pygame
from agent import Agent

class Missile(Agent):
    def __init__(self, pos_x, pos_y, width, height, vel_x, vel_y):
        super().__init__(pos_x, pos_y, width, height, vel_x, vel_y)
        surface = pygame.Surface((width, height))
        pygame.draw.circle(surface, (0,0,0), (width/2, height/2), width/2)
        self.surface = surface
        self.accel_y = 0.005