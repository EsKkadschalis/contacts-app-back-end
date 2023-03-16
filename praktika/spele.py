import pygame

pygame.init()

window = pygame.display.set_mode([200, 200])

while True:

    for event in pygame.event.get():

        rectangle = pygame.Rect(100, 100, 25, 25)
        pygame.draw.rect(window , [ 256 , 0, 0], rectangle )

        pygame.display.update()