import pygame

class Drawable:
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.surface = None
        self.flipHorizontal = False
        self.flipVertical = False

    def loadFile(self, file):
        if file is not None:
            self.file = file
            image = pygame.image.load(file)
            self.surface = pygame.transform.smoothscale(image, (self.width, self.height))

    def flip(self, horizontal, vertical):
        self.flipHorizontal = horizontal
        self.flipVertical = vertical
        
    def draw(self, surface):
        if self.surface is not None:
            self.surface = pygame.transform.flip(self.surface, self.flipHorizontal, self.flipVertical)
            surface.blit(self.surface,(self.pos_x, self.pos_y))