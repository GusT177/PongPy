import pygame
import sys


class Game:

    def __init__(self):
        WIDTH = 1280
        HEIGHT = 720
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()
                    pygame.quit()
        self.clock.tick(60)
        self.window.fill(0, 0, 0)
        print(self.clock.tick())
        pygame.display.update()


Game().run()
