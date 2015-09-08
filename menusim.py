# Harry Beadle 2015
# This is a pygame program that simulates the menu
# of the Apple Watch.

from random import randint

import pygame
pygame.init()

X = 500
Y = 500
RADIUS = 25

display = pygame.display.set_mode((X, Y))
pygame.display.set_caption = "Apple Watch Menu Simulator"

BLACK = 000, 000, 000
WHITE = 255, 255, 255


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def random_circle_surface():
    global RADIUS
    surface = pygame.Surface((2 * RADIUS, 2 * RADIUS))
    surface.fill(BLACK)
    pygame.draw.circle(surface, random_color(), (RADIUS, RADIUS), RADIUS)
    return surface


def blit_icon(icon):
    global display
    surface = pygame.transform.scale(icon.surface, icon.size())
    surface_x, surface_y = surface.get_size()
    x = icon.x + (0.5 * ((2 * RADIUS) - surface_x))
    y = icon.y + (0.5 * ((2 * RADIUS) - surface_y))
    display.blit(surface, (x, y))


class icon:

    def __init__(self, position):
        self.x, self.y = position
        self.surface = random_circle_surface()

    def size(self):
        global X, Y
        x_size = abs(
            int((1 - (abs((self.x + RADIUS) - X / 2) / (X / 2.0))) * (2 * RADIUS)))
        y_size = abs(
            int((1 - (abs((self.y + RADIUS) - X / 2) / (X / 2.0))) * (2 * RADIUS)))
        return_value = (x_size + y_size) / 2
        return return_value, return_value

    def shift(self, rel):
        self.x += rel[0]
        self.y += rel[1]
        if self.x > X:
            self.x = self.x - X
        if self.x < 0:
            self.x = X + self.x
        if self.y > Y:
            self.y = self.y - Y
        if self.y < 0:
            self.y = Y + self.y

# Generate Icons
a = []
extra = False
for y in range(0, Y, Y / 10):
    extra = not extra
    for x in range(0, X, X / 10):
        a.append(icon((x + (extra * X / 20), y)))

# Blit icons
for icon in a:
    blit_icon(icon)
pygame.display.flip()

if __name__ == '__main__':
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        pygame.mouse.get_rel()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        if pygame.mouse.get_pressed()[0]:
            rel = pygame.mouse.get_rel()
            display.fill(BLACK)
            for icon in a:
                icon.shift(rel)
                blit_icon(icon)
            pygame.display.flip()
