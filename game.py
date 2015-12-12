#!/usr/bin/env python
import pygame
import background


class Game:
    """
    Game Class - controls all game elements
    """

    def __init__(self, screen):
        self.background = background.Background(screen)
        self.clock = pygame.time.Clock()
        screen.fill((0, 0, 0))
        pygame.display.flip()

    def update(self):
        self.background.update()
        pygame.display.update()

    def render(self, screen):
        self.background.render(screen)
        pygame.display.flip()
        msElapsed = self.clock.tick(100)
