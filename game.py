import pygame
import math
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_SPACE,
    QUIT,
)
from drawable import Drawable
from agent import Agent
from player import Player
from missiles import Missile



class Game:
    def __init__(self, screen_w, screen_h):
        super().__init__()
        pygame.init()
        self.screen_w = screen_w
        self.screen_h = screen_h
        size = [screen_w, screen_h]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Scorched Py")
        self.background = Drawable(0,0,screen_w,screen_h)
        self.background.loadFile('assets/background.jpg')
        self.player = Player(100, 380, 50 ,50)
        self.player.loadFile('assets/tank1.png')
        self.enemy = Player(600,380,50,50)
        self.enemy.loadFile('assets/tank2.png')
        self.enemy.flip(True, False)
        
        self.players = []
        self.players.append(self.player)
        self.players.append(self.enemy)
        self.missiles = []
        

    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill((255, 255, 255))

        self.background.draw(screen)

        for missile in self.missiles:
            if isinstance(missile,Drawable):
                missile.draw(screen)

        for player in self.players:
            if isinstance(player,Drawable):
                player.draw(screen)
        
        pygame.display.flip()


    def process_events(self):
        """ Process all of the events.Return a "True" if we need to close the window. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    missile = Missile(self.player.pos_x+self.player.width / 2, self.player.pos_y + 15, 4, 4, math.cos(math.radians(self.player.angle))*self.player.power/100, math.sin(math.radians(self.player.angle))*-1*self.player.power/100)
                    self.missiles.append(missile) 


        return False
    

    
    def run(self):
        done = False
        clock = pygame.time.Clock()
        while not done:
            done = self.process_events()
            
            self.display_frame(self.screen)

            for player in self.players:
                if isinstance(player, Agent):
                    player.update()

            for missile in self.missiles:
                if isinstance(missile, Agent):
                    missile.update()

            clock.tick(60)

        pygame.quit()


    