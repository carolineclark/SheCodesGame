import pygame
from pygame.locals import *

class Player:

    def __init__(self, surface):
        self._surface = surface
        self._width = 100
        self._height = 100
        self._x = 150
        self._y = 150
        self._speed = 10
        self._running = True

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def move(self, direction):
        '''
        :params direction: the direction you want the ship to go
        :type direction: string "up", "down" "left" "right"
        '''
        if direction == "up":
            self._y = self._y - self._speed
        if direction == "down":
            self._y = self._y + self._speed
        if direction == "left":
            self._x = self._x - self._speed
        if direction == "right":
            self._x = self._x + self._speed

    def draw(self):
        pygame.draw.rect(
            self._surface,
            (255, 255, 255),
            (self.x, self.y, self.x + self._width, self.y + self._height)
        )
        pygame.display.flip()

    def test_game(self):
        self.draw()
        while self._running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.move("up")
                    elif event.key == K_DOWN:
                        self.move("down")
                    if event.key == K_LEFT:
                        self.move("left")
                    if event.key == K_RIGHT:
                        self.move("right")
                self._surface.fill((0, 0, 0))
                self.draw()
                pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    player = Player(screen)
    player.test_game()
