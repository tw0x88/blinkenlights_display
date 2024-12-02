'''
Blinkenlights Display.

'''
import pygame
import os
import ref as r

def zeichneFensterAN(hoehe, weite, offset = 0):
    screen.blit(image_fenster_AN, (weite + offset, hoehe))

def play_animation(animation):
    for frame in animation:
        for zeileIndex, fensterZeile in enumerate(frame):
            for spalteIndex, fensterStatus in enumerate(fensterZeile):
                if fensterStatus == 1:
                    if zeileIndex == 0:
                        hoehe = 50
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 0)

                    elif zeileIndex == 1:
                        hoehe = 80
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 0)

                    elif zeileIndex == 2:
                        hoehe = 113
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 0)

                    elif zeileIndex == 3:
                        hoehe = 144
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 0)

                    elif zeileIndex == 4:
                        hoehe = 176
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 0)

                    elif zeileIndex == 5:
                        hoehe = 208
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 0)

                    elif zeileIndex == 6:
                        hoehe = 240
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 1)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 2)

                    elif zeileIndex == 7:
                        hoehe = 274
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 1)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 2)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 3)

        pygame.display.flip()    
        pygame.time.delay(pause)
        screen.blit(background, (0, 0))
        pygame.display.flip()



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

        play_animation(r.buchstabenAnimation)
        
    # Beenden
    pygame.quit()