import pygame
import sys
import os

pygame.init()

WINSIZE = WW, WH = 800, 600
WINDOW = pygame.display.set_mode(WINSIZE)

class Splash():
    
    def Window():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            Splash.Draw()

    def Draw():
        WINDOW.fill((136,221,255))
        pygame.display.flip()

Splash.Window()