import ref as r

def zeichneFensterAN(hoehe, weite, offset, screen, image_fenster_AN):
    screen.blit(image_fenster_AN, (weite + offset, hoehe))

def play_animation(animation, pygame, screen, image_fenster_AN, background, pause):
    for frame in animation:
        for zeileIndex, fensterZeile in enumerate(frame):
            for spalteIndex, fensterStatus in enumerate(fensterZeile):
                if fensterStatus == 1:
                    if zeileIndex == 0:
                        hoehe = 50
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                    elif zeileIndex == 1:
                        hoehe = 80
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                    elif zeileIndex == 2:
                        hoehe = 113
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                    elif zeileIndex == 3:
                        hoehe = 144
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                    elif zeileIndex == 4:
                        hoehe = 176
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                    elif zeileIndex == 5:
                        hoehe = 208
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                    elif zeileIndex == 6:
                        hoehe = 240
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 1, screen, image_fenster_AN)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 2, screen, image_fenster_AN)

                    elif zeileIndex == 7:
                        hoehe = 274
                        if spalteIndex == 0:
                            weite = 244
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 1:
                            weite = 263
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 2:
                            weite = 281
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 3:
                            weite = 299
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 4:
                            weite = 317
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 5:
                            weite = 336
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 6:
                            weite = 355
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 7:
                            weite = 373
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 8:
                            weite = 391
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 9:
                            weite = 410
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 10:
                            weite = 428
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 11:
                            weite = 446
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 12:
                            weite = 464
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 13:
                            weite = 482
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 14:
                            weite = 501
                            zeichneFensterAN(hoehe, weite, 0, screen, image_fenster_AN)

                        elif spalteIndex == 15:
                            weite = 520
                            zeichneFensterAN(hoehe, weite, 1, screen, image_fenster_AN)

                        elif spalteIndex == 16:
                            weite = 538
                            zeichneFensterAN(hoehe, weite, 2, screen, image_fenster_AN)

                        elif spalteIndex == 17:
                            weite = 556
                            zeichneFensterAN(hoehe, weite, 3, screen, image_fenster_AN)

        # Zeige aktuellen Frame an
        pygame.display.flip()    
        pygame.time.delay(pause)

        # Kurz alles löschen zwischen den Frames
        screen.blit(background, (0, 0))
        pygame.display.flip()
        pygame.time.delay(44)

def textAnimation(text):
    text = text.upper()
    print(text)
    ani = []
    for letter in text:
        if letter == "0":
          ani.append(r.zahl_0)

        elif letter == "1":
            ani.append(r.zahl_1)

        elif letter == "2":
            ani.append(r.zahl_2)

        elif letter == "3":
            ani.append(r.zahl_3)

        elif letter == "4":
            ani.append(r.zahl_4)

        elif letter == "5":
            ani.append(r.zahl_5)

        elif letter == "6":
            ani.append(r.zahl_6)

        elif letter == "7":
            ani.append(r.zahl_7)

        elif letter == "8":
            ani.append(r.zahl_8)

        elif letter == "9":
            ani.append(r.zahl_9)

        elif letter == "A":
            ani.append(r.letter_A)

        elif letter == "B":
            ani.append(r.letter_B)

        elif letter == "C":
            ani.append(r.letter_C)

        elif letter == "D":
            ani.append(r.letter_D)

        elif letter == "E":
            ani.append(r.letter_E)

        elif letter == "F":
            ani.append(r.letter_F)

        elif letter == "G":
            ani.append(r.letter_G)

        elif letter == "H":
            ani.append(r.letter_H)

        elif letter == "I":
            ani.append(r.letter_I)

        elif letter == "J":
            ani.append(r.letter_J)

        elif letter == "K":
            ani.append(r.letter_K)

        elif letter == "L":
            ani.append(r.letter_L)

        elif letter == "M":
            ani.append(r.letter_M)

        elif letter == "N":
            ani.append(r.letter_N)

        elif letter == "O":
            ani.append(r.letter_O)

        elif letter == "P":
            ani.append(r.letter_P)

        elif letter == "Q":
            ani.append(r.letter_Q)

        elif letter == "R":
            ani.append(r.letter_R)

        elif letter == "S":
            ani.append(r.letter_S)

        elif letter == "T":
            ani.append(r.letter_T)

        elif letter == "U":
            ani.append(r.letter_U)

        elif letter == "V":
            ani.append(r.letter_V)

        elif letter == "W":
            ani.append(r.letter_W)

        elif letter == "X":
            ani.append(r.letter_X)

        elif letter == "Y":
            ani.append(r.letter_Y)

        elif letter == "Z":
            ani.append(r.letter_Z)

        elif letter == "#":
            ani.append(r.letter_hash)

        elif letter == ".":
            ani.append(r.letter_dot)

        elif letter == " ":
            ani.append(r.space)
    
    return ani
