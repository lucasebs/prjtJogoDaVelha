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

# Font
FONT = "resouces" + os.sep + "fronts" + os.sep + "Quicksand-Light.otf"

# display settings
CAPTION = "prjtJogoDaVelha"
RESOLUTION = (768, 768)
MOUSE_VISIBILITY = True
FPS = 45

# Menu
MAIN_MENU = 0
PLAYING = 1
CREDITS = 2