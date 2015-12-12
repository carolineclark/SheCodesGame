import pygame
from pygame.locals import *


class UnknownDirectionException(Exception):
    pass


class Player:

    def __init__(self, surface):
        self._surface = surface
        self._width = 100
        self._height = 100
        self._x = 150
        self._y = 150
        self._speed = 10
        self._running = True
        self._key_pressed = None

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def move(self):
        '''
        :params direction: the direction you want the ship to go
        :type direction: string "up", "down" "left" "right"
        '''
        if self._key_pressed:
            if self._key_pressed == "up":
                self._y = self._y - self._speed
            if self._key_pressed == "down":
                self._y = self._y + self._speed
            if self._key_pressed == "left":
                self._x = self._x - self._speed
            if self._key_pressed == "right":
                self._x = self._x + self._speed

    def set_key_pressed(self, direction):
        if direction and direction not in ["left", "right", "up", "down"]:
            raise UnknownDirectionException

        self._key_pressed = direction

    def draw(self):
        pygame.draw.rect(
            self._surface,
            (255, 255, 255),
            (self.x, self.y, self._width, self._height)
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
                        self.set_key_pressed("up")
                    elif event.key == K_DOWN:
                        self.set_key_pressed("down")
                    if event.key == K_LEFT:
                        self.set_key_pressed("left")
                    if event.key == K_RIGHT:
                        self.set_key_pressed("right")

                elif event.type == KEYUP:
                    self.set_key_pressed(None)

            self._surface.fill((0, 0, 0))
            self.move()
            self.draw()
            pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    player = Player(screen)
    player.test_game()
