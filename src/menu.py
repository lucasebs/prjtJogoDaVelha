#! /usr/bin/env python

import pygame, resources, utils


class Menu:
        """Menu Screen"""

        def __init__(self, screen):
            self.screen = screen
            self.background = pygame.image.load(resources.BACKGROUND)
            self.background_rect = self.background.get_rect()

        def update(self):
            self.screen.blit(self.background, self.background_rect)

        def display(self, flip):

            self.update()

            if flip.equals(resources.PLAYING):
                self.set_background(resources.BACKGROUND)
                self.back.show()

            elif flip.equals(resources.CREDITS):
                self.set_background(resources.BACKGROUND)
                self.back.show()

            else:
                self.set_background(resources.BACKGROUND)
                self.exit.show()

        def set_background(self, background):
            self.background = pygame.image.load(background)