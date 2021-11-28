# Mental notes for the maintainer:
# - Learn function parameters instead of relying on global variables
# - Learn error handling

# Importing modules
import pygame
import sys
import os
import datetime
import time

# Initializing pygame and its modules
pygame.init()
pygame.mixer.init()
pygame.font.init()

if pygame.get_init() and pygame.mixer.get_init() and pygame.font.get_init() == True:
    print("All pygame modules loaded")

# Setting up the window
WINSIZE = WW, WH = 800, 600
WINDOW = pygame.display.set_mode(WINSIZE)
pygame.display.set_caption('DroneFish')

GAMEICON = pygame.image.load(os.path.join('Resources', 'Icon', 'Icon.png'))
pygame.display.set_icon(GAMEICON)


# FPS Cap
FPS = 60

# Array with all the assets (see Resources folder)
images = [pygame.image.load(os.path.join('Resources', 'Splash Screen', 'Images', 'Background.png')), pygame.image.load(os.path.join('Resources', 'Splash Screen', 'Images', 'Logo.png')), pygame.image.load(os.path.join('Resources', 'Splash Screen', 'Images', 'Logo2.png'))]
sounds = [os.path.join('Resources', 'Splash Screen', 'Sounds', 'Beep.wav'), os.path.join('Resources', 'Splash Screen', 'Sounds', 'Exitting.wav')]
fonts = [os.path.join('Resources', 'Fonts', 'FredokaOne.ttf')]

global FredokaOne # Mental note for maintainer: Learn function parameters instead of relying on global variables
FredokaOne = pygame.font.Font(fonts[0], 54)
FredokaOnesmol = pygame.font.Font(fonts[0], 36)

# Class for the splash screen
class SplashPart1():
    
    def Window():
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=1)
        SplashPart1.Sound()
        while True:
            clock = pygame.time.Clock()
            clock.tick(FPS) # Setting the FPS cap

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            SplashPart1.Draw()

            if datetime.datetime.now() >= endTime:
                break
        
    # Function for handling sound
    def Sound():
        pygame.mixer.music.load(sounds[0])
        pygame.mixer.music.play()
    # Drawing things on the screen
    def Draw():
        background = (255, 255, 255)

        LOGO_WIDTH, LOGO_HEIGHT = 800, 300
        LOGO_IMG = images[1]
        LOGO_SCALE = pygame.transform.rotate(pygame.transform.scale(LOGO_IMG, (LOGO_WIDTH, LOGO_HEIGHT)), 0)
        logo = pygame.Rect(0, 100, LOGO_WIDTH, LOGO_HEIGHT)

        WINDOW.fill(background)
        WINDOW.blit(LOGO_SCALE, (logo.x, logo.y))

        pygame.display.flip()

class SplashPart2():

    def Window():
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=1)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            SplashPart2.Draw()
            
            if datetime.datetime.now() >= endTime:
                break

    def Draw():
        background = (255, 255, 255)
        
        LOGO2_WIDTH, LOGO2_HEIGHT = 316, 74
        LOGO2_IMG = images[2]
        LOGO2_SCALE = pygame.transform.rotate(pygame.transform.scale(LOGO2_IMG, (LOGO2_WIDTH, LOGO2_HEIGHT)), 0)
        logo2 = pygame.Rect(240, 250, LOGO2_WIDTH, LOGO2_HEIGHT)

        WINDOW.fill(background)
        WINDOW.blit(LOGO2_SCALE, (logo2.x, logo2.y))
        pygame.display.flip()

# Class for the Main Menu
class MainMenu():
    
    def Window():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
            # Keyboard inputs
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_e]:
                WINDOW.fill((0, 0, 0))
                pygame.display.update()

                pygame.mixer.music.load(sounds[1])
                pygame.mixer.music.play(fade_ms=1)
                time.sleep(0.5)
                sys.exit()

            if keys_pressed[pygame.K_c]:
                Credits.Window()

            # Calling a function for drawing
            MainMenu.Draw()
    
    def Draw():
        # Background
        background = images[0]
        
        # Logo
        LOGO2_WIDTH, LOGO2_HEIGHT = 316, 74
        LOGO2_IMG = images[2]
        LOGO2_SCALE = pygame.transform.rotate(pygame.transform.scale(LOGO2_IMG, (LOGO2_WIDTH, LOGO2_HEIGHT)), 0)
        logo2 = pygame.Rect(240, 72, LOGO2_WIDTH, LOGO2_HEIGHT)

        # Buttons
        START_GAME_TEXT = FredokaOne.render("Start game (Enter)", True, (255, 255, 255))
        CREDITS_TEXT = FredokaOne.render("Credits (C)", True, (255, 255, 255))
        EXIT_GAME_TEXT = FredokaOne.render("Exit game (E)", True, (255, 255, 255))

        # Blitting things on the screen
        WINDOW.blit(background, (0, 0))
        WINDOW.blit(LOGO2_SCALE, (logo2.x, logo2.y))

        WINDOW.blit(START_GAME_TEXT, (39, 272))
        WINDOW.blit(CREDITS_TEXT, (39, 372))
        WINDOW.blit(EXIT_GAME_TEXT, (39, 472))
        pygame.display.flip()

class Credits():

    def Window():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            Credits.Draw()

            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_ESCAPE]:
                MainMenu.Window()

    def Draw():
        # Background
        background = images[0]
        
        # Credits text
        PROGRAMMER = FredokaOnesmol.render("Maintainer - Markix", True, (255, 255, 255)) # Markix was taken on Github ;-;
        FONT_AUTHOR = FredokaOnesmol.render("Main Game Font - Available on Google Fonts", True, (255, 255, 255))

        # Blitting stuff
        WINDOW.blit(background, (0, 0))
        WINDOW.blit(PROGRAMMER, (10, 200))
        WINDOW.blit(FONT_AUTHOR, (10, 300))
        pygame.display.flip()

# SplashPart1 runs for about a second, the loop then ends, 
# meaning the function is not running anymore and the 2nd part can run. 
SplashPart1.Window()
SplashPart2.Window()

# Calling the Main Menu
MainMenu.Window()