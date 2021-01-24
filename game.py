import pygame





class Game:

    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill((0, 204, 255))
        color = (191, 255, 0)
        pygame.draw.rect(screen, color, (0,500,800,200))
        color = (255, 255, 255)
        radius = 25
        pygame.draw.circle(screen, color, (50, 50), radius)
        pygame.draw.circle(screen, color, (60, 60), radius)
        pygame.draw.circle(screen, color, (80, 30), radius)
        pygame.draw.circle(screen, color, (100, 40), radius)
        radius = 40
        pygame.draw.circle(screen, color, (250, 50), radius)
        pygame.draw.circle(screen, color, (260, 60), radius)
        pygame.draw.circle(screen, color, (280, 30), radius)
        pygame.draw.circle(screen, color, (300, 40), radius)
        radius = 20
        pygame.draw.circle(screen, color, (550, 50), radius)
        pygame.draw.circle(screen, color, (560, 60), radius)
        pygame.draw.circle(screen, color, (580, 30), radius)
        pygame.draw.circle(screen, color, (600, 40), radius)
        radius = 25
        pygame.draw.circle(screen, color, (750, 50), radius)
        pygame.draw.circle(screen, color, (760, 60), radius)
        pygame.draw.circle(screen, color, (780, 30), radius)
        pygame.draw.circle(screen, color, (800, 40), radius)
        color = (255, 215, 0)
        pygame.draw.rect(screen, color, (200,200,300,400))
        color = (139,69,19)
        pygame.draw.polygon(screen, color, [[350, 100], [200, 200], [500, 200]], 0)
        color = (195, 155, 119)
        radius = 15
        pygame.draw.circle(screen, color, (350, 150), radius)
        color = (0, 204, 255)
        pygame.draw.rect(screen, color, (250,250,50,50))
        pygame.draw.rect(screen, color, (400,250,50,50))
        color = (255, 0, 0)
        pygame.draw.rect(screen, color, (310,460,80,200))
        color = (195, 155, 119)
        pygame.draw.rect(screen, color, (610,560,10,60))
        color = (34,139,34)
        radius = 30
        pygame.draw.circle(screen, color, (600, 560), radius)
        pygame.draw.circle(screen, color, (630, 560), radius)
        pygame.draw.circle(screen, color, (615, 520), radius)
        color = (195, 155, 119)
        pygame.draw.rect(screen, color, (710,560,10,60))
        color = (34,139,34)
        pygame.draw.circle(screen, color, (700, 560), radius)
        pygame.draw.circle(screen, color, (730, 560), radius)
        pygame.draw.circle(screen, color, (715, 520), radius)
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


    