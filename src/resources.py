#! /usr/bin/env python

import pygame, os

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DEFAULT_BG_COLOR = WHITE

# Image paths
GRAPHICS_PATH = "resources" + os.sep + "images" + os.sep
BACKGROUND = GRAPHICS_PATH + "background.jpg"
BACKGROUND_CREDITS = GRAPHICS_PATH + "background_credits.png"
BUTTONS = GRAPHICS_PATH + "buttons.png"
LOGO = GRAPHICS_PATH + "logo.png"
TABLE = GRAPHICS_PATH + "tabuleiro.png"



# buttons
CUT_PLAY = ((240, 0, 130, 38), (0, 0, 130, 38))
CUT_CREDITS = ((240, 40, 131, 30), (0, 40, 131, 30))
CUT_BACK = ((240, 72, 178, 30), (0, 72, 178, 30))
CUT_EXIT = ((240, 104, 148, 30), (0, 104, 148, 30))

# Font
FONT = "resources" + os.sep + "fonts" + os.sep + "Quicksand-Regular.otf"

# display settings
CAPTION = "prjtJogoDaVelha"
RESOLUTION = (768, 768)
MOUSE_VISIBILITY = True
FPS = 45

# Menu
MAIN_MENU = 0
PLAYING = 1
CREDITS = 2