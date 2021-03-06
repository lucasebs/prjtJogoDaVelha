#! /usr/bin/env python
# coding: utf-8

import pygame, resources, surface, os


class Game:
    """Class Game - Initialize the game"""

    def __init__(self):

        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # initialize pygame modules
        pygame.init()
        pygame.mixer.init()

        # set the name of the game
        pygame.display.set_caption(resources.CAPTION)

        # set visibility of the mouse
        pygame.mouse.set_visible(resources.MOUSE_VISIBILITY)

        # set a window or screen for display
        pygame.display.set_mode(resources.RESOLUTION, 0, 32)

        # sets the game surface
        surface.init()

        pygame.mixer.quit()
        pygame.quit()

if __name__ == "__main__":
    Game()
