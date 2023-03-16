import pygame

pygame.init()

window = pygame.display.set_mode([500, 500])

font = pygame.font.SysFont('couriernew', 40)
text = font.render('TEKSTS', True, [255, 255, 255])


while True:
    for event in pygame.event.get():
       window.blit(text, [50, 50])
        
    pygame.display.update()