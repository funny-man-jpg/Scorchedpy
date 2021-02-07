import pygame





class Game:

    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill((255, 255, 255))
        
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


    