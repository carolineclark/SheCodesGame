#!/usr/bin/env python

import os
import sys
import pygame
import game
from pygame.locals import *

if not pygame.font:
    print 'Warning, fonts disabled'
if not pygame.mixer:
    print 'Warning, sound disabled'


class PyManMain:
    """
    The Main PyMan Class - This class handles the main
    initialization and creating of the Game.
    """

    def __init__(self, width=640, height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('She++ game')
        self.game = game.Game(self.screen)

    def mainloop(self):
        """This is the Main Loop of the Game"""
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.game.update()
            self.game.render(self.screen)

if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.mainloop()
