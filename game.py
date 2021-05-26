import pygame
import math
from pygame import sprite
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_SPACE,
    K_LSHIFT,
    KMOD_LSHIFT,
    QUIT,
)
from drawable import Drawable
from agent import Agent
from player import Player
from missiles import Missile
from hud import HUD
from sprite import Sprite



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
        self.craters = []
        self.explosions = []
        self.hud = HUD(0, 0, screen_w, 100)
        self.hud.setPower(self.player.power)
        self.hud.setAngle(self.player.angle)
        

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

        for crater in self.craters:
            if isinstance(crater, Drawable):
                crater.draw(screen)

        for explosion in self.explosions:
            if isinstance(explosion, Drawable):
                explosion.draw(screen)

        #for crater in self.craters:
            
        
        self.hud.draw(screen)
        pygame.display.flip()


    def process_events(self):
        """ Process all of the events.Return a "True" if we need to close the window. """
        mods = pygame.key.get_mods()
        shifted = mods and KMOD_LSHIFT

        angleDelta = 1
        powerDelta = 2
        if shifted:
            angleDelta = 10
            powerDelta = 10
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    vel_x = self.player.calc_player_vel_x()
                    vel_y = self.player.calc_player_vel_y()
                    missile = Missile(
                        self.player.pos_x+self.player.width /2 + vel_x*30,
                        self.player.pos_y + 15 + vel_y*30, 
                        4, 
                        4, 
                        self.player.calc_player_vel_x(),
                        self.player.calc_player_vel_y()
                        )
                    self.missiles.append(missile) 
                if event.key == K_UP:
                    self.player.power += powerDelta
                if event.key == K_DOWN:
                    self.player.power -= powerDelta
                if event.key == K_LEFT:
                    self.player.angle += angleDelta
                if event.key == K_RIGHT:
                    self.player.angle -= angleDelta
                


                if self.player.power >= 100:
                    self.player.power = 100
                if self.player.power <= 1:
                    self.player.power = 1
                if self.player.angle >= 180:
                    self.player.angle = 180
                if self.player.angle <= 0:
                    self.player.angle = 0

                self.hud.setAngle(self.player.angle)
                self.hud.setPower(self.player.power)
            
        return False

    def run(self):
        done = False
        clock = pygame.time.Clock()
        count = 0
        while not done:
            done = self.process_events()
            
            self.display_frame(self.screen)

            for player in self.players:
                if isinstance(player, Agent):
                    player.update()

            for missile in self.missiles:
                if isinstance(missile, Agent):
                    missile.update()
                    for player in self.players:
                        if isinstance(player, Agent):
                            if missile.collided(player):
                                print("Collided")
                                self.missiles.remove(missile)
                                self.players.remove(player)
                                crater = Drawable(player.pos_x, player.pos_y + 30, 64, 20)
                                crater.loadFile('assets/crater.png')
                                self.craters.append(crater)


                                explosion = Sprite(player.pos_x - 25, player.pos_y - 50, 100, 100)
                                explosion.loadFile('assets/boom.png', 3, 4)
                                explosion.start()
                                self.explosions.append(explosion)
                                

            clock.tick(60)
            count += 1
        pygame.quit()