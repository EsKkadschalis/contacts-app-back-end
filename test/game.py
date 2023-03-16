import pygame

pygame.init()

window = pygame.display.set_mode([500, 500])

FONT = pygame.font.sys_font ('couriernew', 24)

while True:

    events = pygame.event.get()

    for event in events:
       
        if event.type == pygame.QUIT:
            pygame.quit()

    text = text.render('text', True, [255, 255, 255])
    window.blit(FONT , [10, 10])
   
    pygame.display.update()