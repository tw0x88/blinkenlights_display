'''
Blinkenlights Display.

'''
import pygame
import os
import func as f
import ref as r

pause = 1050
FULLSCREEN = False

if __name__ == "__main__":
    pygame.init()

    if FULLSCREEN == True:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((800, 480))

    pygame.display.set_caption("Blinkenlights Display")
    background = pygame.image.load("images/background.png").convert()
    image_fenster_AN = pygame.image.load("images/an.png").convert_alpha()
    hintergrund = screen.blit(background, (0, 0))
    os.system("cls")

    running = True
    while running:
        # Ereignisse überprüfen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Escape-Taste
                    running = False

        pygame.time.delay(800)
        f.play_animation(f.textAnimation("0123456789 abcdefghijklmnOpqrstuvwxyz.#"), pygame, screen, image_fenster_AN, background, pause)
        
    # Beenden
    pygame.quit()