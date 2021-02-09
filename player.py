from agent import Agent

class Player(Agent):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__(pos_x, pos_y, width, height, 0, 0)
        self.angle = 45
        self.power = 50