import pygame
from agent import Agent
from spritesheet import SpriteSheet


class Sprite(Agent):
    def __init__(self, pos_x, pos_y, height, width, vel_x=0, vel_y=0):
        super().__init__(pos_x, pos_y, height, width, vel_x, vel_y)
        self.image_index = -1
        self.num_images = 0
        self.animated = True

    def loadFile(self, file, num_rows, num_cols, num_images=0):
        if file is not None:
            self.file = file
            self.spriteSheet = SpriteSheet(file)
            self.images = self.spriteSheet.load_grid_images(num_rows, num_cols)
            if num_images == 0:
                self.num_images = num_rows * num_cols
            else:
                self.num_images = num_images

    def draw(self, surface):
        print(f"Sprite draw index: {self.image_index}")
        if self.image_index < 0 or self.image_index > self.num_images :
            return
    
        image = pygame.transform.smoothscale(
            self.images[self.image_index], (self.width, self.height)
        )
        if image is not None:
            surface.blit(image, (self.pos_x, self.pos_y))

    def setAnimated(self, animated):
        self.animated = animated

    def setIndex(self, index):
        self.image_index = index


    def start(self):
        print(f"Sprite start")
        self.image_index = 0
        self.animated = True

    def update(self):
        if (self.animated and self.image_index >= 0 and self.image_index < self.num_images - 1):
            self.image_index += 1