import pygame, sys

pygame.init()
WIDTH, HEIGHT = 400, 400
pygame.display.set_caption("CTRL+EN Fullscreenn Toggle")
fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(
                    
                    (800 , 600),
                    pygame.FULLSCREEN |
                    pygame.SCALED)
                else:
                    screen = pygame.display.set_mode(
                            (WIDTH , HEIGHT), pygame.RESIZABLE)
    screen.fill((30,30,30))
    pygame.draw.rect(screen, (255, 0, 0), (1, 5, 100, 100))
    pygame.quit()
                    

