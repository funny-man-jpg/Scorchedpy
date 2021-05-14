from drawable import Drawable
import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)


class HUD(Drawable):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__(pos_x, pos_y, width, height)
        self.myfont = pygame.font.SysFont(None, 30)
        self.surface = pygame.Surface((width, height))

    def setPower(self, text):
        print(f"HUD: {text}")
        self.powerSurface = self.myfont.render(f"Power: {text}", True, BLUE)
        self.powerSurface.fill(BLACK, pygame.Rect(20, 20, 200, 100))
        self.surface.blit(self.powerSurface, (20, 20))

    def setAngle(self, text):
        print(f"HUD: {text}")
        self.angleSurface = self.myfont.render(f"Angle: {text}", True, BLUE)
        self.powerSurface.fill(BLACK, pygame.Rect(20, 60, 200, 100))
        self.surface.blit(self.angleSurface, (20, 60))

    def draw(self, surface):
        if self.surface is not None:
            surface.blit(self.surface, (self.pos_x, self.pos_y))