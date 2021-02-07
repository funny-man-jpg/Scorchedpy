import pygame





class Game:

    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill((255, 255, 255))

        
        width = 800
        height = 600
        background_image = pygame.image.load('assets/background.jpg')
        scaled_background = pygame.transform.smoothscale(background_image, (width, height))
        pos_x = 0
        pos_y = 0
        screen.blit(scaled_background, (pos_x, pos_y))


        width = 50
        height = 50
        tank1_image = pygame.image.load('assets/tank1.png')
        scaled_tank1 = pygame.transform.smoothscale(tank1_image, (width, height))
        pos_x = 100
        pos_y = 300
        screen.blit(scaled_tank1, (pos_x, pos_y))

        width = 50
        height = 50
        tank2_image = pygame.image.load('assets/tank2.png')
        scaled_tank2 = pygame.transform.smoothscale(tank2_image, (width, height))
        scaled_tank2 = pygame.transform.flip(tank2_image, True, False)
        pos_x = 650
        pos_y = 300
        screen.blit(scaled_tank2, (pos_x, pos_y))
        
        pygame.display.flip()


    def process_events(self):
        """ Process all of the events.Return a "True" if we need to close the window. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

        return False
    def __init__(self, screen_w, screen_h):
        super().__init__()
        pygame.init()
        self.screen_w = screen_w
        self.screen_h = screen_h
        size = [screen_w, screen_h]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("My Game")
    
    def run(self):
        print("Game:run()")
        done = False
        clock = pygame.time.Clock()
        while not done:
            done = self.process_events()
            
            self.display_frame(self.screen)

            clock.tick(60)

        pygame.quit()


    