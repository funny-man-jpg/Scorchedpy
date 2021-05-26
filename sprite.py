import pygame
from agent import Agent
from spritesheet import SpriteSheet


class Sprite(Agent):
    def __init__(self, pos_x, pos_y, height, width, vel_x=0, vel_y=0):
        super().__init__(pos_x, pos_y, height, width, vel_x, vel_y)
        self.image_index = -1
        self.num_images = 0

    def loadFile(self, file, num_rows, num_cols):
        if file is not None:
            self.file = file
            self.spriteSheet = SpriteSheet(file)
            self.images = self.spriteSheet.load_grid_images(num_rows, num_cols)
            self.num_images = num_rows * num_cols

    def draw(self, surface):
        print(f"Sprite draw index: {self.image_index}")
        if self.image_index < 0:
            return
    
        image = pygame.transform.smoothscale(
            self.images[self.image_index], (self.width, self.height)
        )
        if image is not None:
            surface.blit(image, (self.pos_x, self.pos_y))

    def start(self):
        print(f"Sprite start")
        self.image_index = 0

    def update(self):
        if self.image_index >= 0 and self.image_index < self.num_images -1:
            self.image_index += 1