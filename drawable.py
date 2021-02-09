import pygame

class Drawable:
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.surface = None

    def loadFile(self, file):
        if file is not None:
            self.file = file
            image = pygame.image.load(file)
            self.surfave = pygame.transform.smoothscale(image, (self.width, self.height))

    def flip(self, horizontal, vertical):
        self.surface = pygame.transform.flip(self.surface, horizontal, vertical)

    def draw(self, surface):
        if self.surface is not None:
            surface.blit(self.surface,(self.pos_x, self.pos_y))