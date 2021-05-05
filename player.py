from agent import Agent
import math

class Player(Agent):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__(pos_x, pos_y, width, height, 0, 0)
        self.angle = 45
        self.power = 50

    def calc_player_vel_x(self):
        return math.cos(math.radians(self.angle)) * self.power * (.025)
    def calc_player_vel_y(self):
        return -math.sin(math.radians(self.angle)) * self.power * (.025)