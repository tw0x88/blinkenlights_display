'''
Blinkenlights Display.

'''

import pygame
import os

beispielMatrix_AN = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

beispielMatrix_AUS = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

db = [
[0, 0, 1, 1, 1, 1, 0, 0],
[0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 1, 1, 0, 1, 0],
[0, 1, 1, 0, 0, 1, 1, 0],
[0, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 1, 1, 0, 0, 1, 0],
[0, 0, 0, 1, 1, 1, 0, 0]
]


ccc_logo = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]
]

ccc = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

herz = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


zeile_00_an = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

zeile_01_an = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

zeile_02_an = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

zeile_03_an = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

zeile_04_an = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

zeile_05_an = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

zeile_06_an = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

zeile_07_an = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

zahl_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

zahl_1 = [
    [0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0]
]

zahl_2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

zahl_3 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0]
]

zahl_4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]

zahl_5 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0]
]

zahl_6 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0]
]

zahl_7 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
]

zahl_8 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0]
]

zahl_9 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0]
]

beispielAnimation = [ccc,
                    ccc_logo,
                    herz
                    ]

def zeicheFensterAN(hoehe, weite, offset = 0):
    screen.blit(image_fenster_AN, (weite + offset, hoehe))

pause = 1050
FULLSCREEN = False

if __name__ == "main":

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

        #hintergrund = screen.blit(background, (0, 0))
        pygame.time.delay(800)    

        for frame in beispielAnimation:
            for zeileIndex, fensterZeile in enumerate(frame):
                for spalteIndex, fensterStatus in enumerate(fensterZeile):
                    if fensterStatus == 1:
                        if zeileIndex == 0:
                            hoehe = 50
                            if spalteIndex == 0:
                                weite = 244
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 1:
                                weite = 263
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 2:
                                weite = 281
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 3:
                                weite = 299
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 4:
                                weite = 317
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 5:
                                weite = 336
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 6:
                                weite = 355
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 7:
                                weite = 373
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 8:
                                weite = 391
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 9:
                                weite = 410
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 10:
                                weite = 428
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 11:
                                weite = 446
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 12:
                                weite = 464
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 13:
                                weite = 482
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 14:
                                weite = 501
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 15:
                                weite = 520
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 16:
                                weite = 538
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 17:
                                weite = 556
                                zeicheFensterAN(hoehe, weite, 0)

                        elif zeileIndex == 1:
                            hoehe = 80
                            if spalteIndex == 0:
                                weite = 244
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 1:
                                weite = 263
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 2:
                                weite = 281
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 3:
                                weite = 299
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 4:
                                weite = 317
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 5:
                                weite = 336
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 6:
                                weite = 355
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 7:
                                weite = 373
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 8:
                                weite = 391
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 9:
                                weite = 410
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 10:
                                weite = 428
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 11:
                                weite = 446
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 12:
                                weite = 464
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 13:
                                weite = 482
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 14:
                                weite = 501
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 15:
                                weite = 520
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 16:
                                weite = 538
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 17:
                                weite = 556
                                zeicheFensterAN(hoehe, weite, 0)

                        elif zeileIndex == 2:
                            hoehe = 113
                            if spalteIndex == 0:
                                weite = 244
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 1:
                                weite = 263
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 2:
                                weite = 281
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 3:
                                weite = 299
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 4:
                                weite = 317
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 5:
                                weite = 336
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 6:
                                weite = 355
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 7:
                                weite = 373
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 8:
                                weite = 391
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 9:
                                weite = 410
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 10:
                                weite = 428
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 11:
                                weite = 446
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 12:
                                weite = 464
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 13:
                                weite = 482
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 14:
                                weite = 501
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 15:
                                weite = 520
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 16:
                                weite = 538
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 17:
                                weite = 556
                                zeicheFensterAN(hoehe, weite, 0)

                        elif zeileIndex == 3:
                            hoehe = 144
                            if spalteIndex == 0:
                                weite = 244
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 1:
                                weite = 263
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 2:
                                weite = 281
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 3:
                                weite = 299
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 4:
                                weite = 317
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 5:
                                weite = 336
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 6:
                                weite = 355
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 7:
                                weite = 373
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 8:
                                weite = 391
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 9:
                                weite = 410
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 10:
                                weite = 428
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 11:
                                weite = 446
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 12:
                                weite = 464
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 13:
                                weite = 482
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 14:
                                weite = 501
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 15:
                                weite = 520
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 16:
                                weite = 538
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 17:
                                weite = 556
                                zeicheFensterAN(hoehe, weite, 0)

                        elif zeileIndex == 4:
                            hoehe = 176
                            if spalteIndex == 0:
                                weite = 244
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 1:
                                weite = 263
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 2:
                                weite = 281
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 3:
                                weite = 299
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 4:
                                weite = 317
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 5:
                                weite = 336
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 6:
                                weite = 355
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 7:
                                weite = 373
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 8:
                                weite = 391
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 9:
                                weite = 410
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 10:
                                weite = 428
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 11:
                                weite = 446
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 12:
                                weite = 464
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 13:
                                weite = 482
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 14:
                                weite = 501
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 15:
                                weite = 520
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 16:
                                weite = 538
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 17:
                                weite = 556
                                zeicheFensterAN(hoehe, weite, 0)

                        elif zeileIndex == 5:
                            hoehe = 208
                            if spalteIndex == 0:
                                weite = 244
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 1:
                                weite = 263
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 2:
                                weite = 281
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 3:
                                weite = 299
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 4:
                                weite = 317
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 5:
                                weite = 336
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 6:
                                weite = 355
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 7:
                                weite = 373
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 8:
                                weite = 391
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 9:
                                weite = 410
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 10:
                                weite = 428
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 11:
                                weite = 446
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 12:
                                weite = 464
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 13:
                                weite = 482
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 14:
                                weite = 501
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 15:
                                weite = 520
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 16:
                                weite = 538
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 17:
                                weite = 556
                                zeicheFensterAN(hoehe, weite, 0)

                        elif zeileIndex == 6:
                            hoehe = 240
                            if spalteIndex == 0:
                                weite = 244
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 1:
                                weite = 263
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 2:
                                weite = 281
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 3:
                                weite = 299
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 4:
                                weite = 317
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 5:
                                weite = 336
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 6:
                                weite = 355
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 7:
                                weite = 373
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 8:
                                weite = 391
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 9:
                                weite = 410
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 10:
                                weite = 428
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 11:
                                weite = 446
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 12:
                                weite = 464
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 13:
                                weite = 482
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 14:
                                weite = 501
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 15:
                                weite = 520
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 16:
                                weite = 538
                                zeicheFensterAN(hoehe, weite, 1)

                            elif spalteIndex == 17:
                                weite = 556
                                zeicheFensterAN(hoehe, weite, 2)

                        elif zeileIndex == 7:
                            hoehe = 274
                            if spalteIndex == 0:
                                weite = 244
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 1:
                                weite = 263
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 2:
                                weite = 281
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 3:
                                weite = 299
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 4:
                                weite = 317
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 5:
                                weite = 336
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 6:
                                weite = 355
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 7:
                                weite = 373
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 8:
                                weite = 391
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 9:
                                weite = 410
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 10:
                                weite = 428
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 11:
                                weite = 446
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 12:
                                weite = 464
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 13:
                                weite = 482
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 14:
                                weite = 501
                                zeicheFensterAN(hoehe, weite, 0)

                            elif spalteIndex == 15:
                                weite = 520
                                zeicheFensterAN(hoehe, weite, 1)

                            elif spalteIndex == 16:
                                weite = 538
                                zeicheFensterAN(hoehe, weite, 2)

                            elif spalteIndex == 17:
                                weite = 556
                                zeicheFensterAN(hoehe, weite, 3)

            pygame.display.flip()    
            pygame.time.delay(pause)
            screen.blit(background, (0, 0))
            pygame.display.flip()
        
    # Beenden
    pygame.quit()