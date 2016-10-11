#! /usr/bin/env python[

import pygame


class Tile:
    """Class Tile - Represents every inanimate object over the screen."""

    def __init__(self, screen, tileset, cut):
        self.screen = screen
        self.tileset = tileset
        self.image = pygame.image.load(tileset).subsurface(cut)
        self.rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def set_tile(self, tileset):
        self.tileset = tileset

    def get_tileset(self):
        return self.tileset

    def get_rect(self):
        return self.rect

    def set_pos(self, rect):
        self.rect = pygame.Rect(rect)

    def get_surface(self):
        return self.image]