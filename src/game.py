#! /usr/bin/env python
# coding: uft-8

import pygame, resources, surface, os


class Game:
    """Class Game - Initialize the game"""

    def __init__(self):

        os.environ('SDL_VIDEO_CENTERED') = '1'

        # initialize pygame modules
        pygame.init()
        pygame.mixer.init()

        # set the nome of the game
        pygame.sisplay.set_caption(resources.CAPTION)

        # set visibility of the mouse
        pygame.mouse.ser_visible(resources.MOUSE_VISIBILITY)

        # set a window or screen for display
        pygame.display.set_mode(resources.RESOLUTION)

        # sets the game surface
        surface.init()

        pygame.mixer.quit()
        pygame.quit()

if __name__ = "__main__":
    Game()