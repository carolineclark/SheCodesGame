#!/usr/bin/env python
import pygame
import sys
import pygame.sprite as sprite


class Background:
    """
    BAckground Class - scrolling background
    """

    def __init__(self, screen):
        # self.texture = pygame.image.load('./assets/background.jpg')
        self.width = screen.get_size()[0]
        self.height = screen.get_size()[1]
        self.pos_y = 0
        self.pos_newY = -self.height
        # Fill background
        self.texture = pygame.Surface(screen.get_size())
        self.texture = self.texture.convert()
        self.texture.fill((150, 0, 0))

    def update(self):
        self.pos_newY += 5
        self.pos_y += 5
        if self.pos_y > self.height:
            self.pos_y = -self.height
        if self.pos_newY > self.height:
            self.pos_newY = -self.height

    def render(self, screen):
        screen.blit(self.texture, (0, 0))
