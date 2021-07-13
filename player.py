from sprite import Sprite
import math

class Player(Sprite):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__(pos_x, pos_y, width, height, 0, 0)
        self.angle = 45
        self.power = 50

    def calc_player_vel_x(self):
        return math.cos(math.radians(self.angle)) * self.power * (.025)
    def calc_player_vel_y(self):
        return -math.sin(math.radians(self.angle)) * self.power * (.025)

    def update(self):
        if self.num_images > 0:
            index = math.floor(self.angle/180*12)
            self.setIndex(index)
        else:
            self.setIndex(0)