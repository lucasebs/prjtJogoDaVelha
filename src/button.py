#! /usr/bin/env python

import pygame, tile, resources, utils


class Button:
    """Class Button - Represents an abstract button"""

    def __init__(self, screen, tileset, cut, *position):
        self.screen = screen
        self.pos = position
        self.state = False
        self.hover = tile.Tile(self.screen, tileset, cut[1])
        self.hover.set_pos(utils.move(self.hover.get_rect(), self.pos))
        self.leave = tile.Tile(self.screen, tileset, cut[0])
        self.leave.set_pos(utils.move(self.leave.get_rect(), self.pos))

    def show(self):

        if self.onhover():
            self.image = self.leave
            self.set_click()
        else:
            self.image = self.hover
            self.set_click(False)

        self.screen.blit(self.image.get_surface(), self.pos)

    def onhover(self):
        mx, my = pygame.mouse.get_pos()
        focus = self.leave.get_rect()
        padding_bottom = (focus.height / 20) - 10

        if mx > focus.right or mx < focus.left:
            return False

        if my > (focus.bottom - padding_bottom) or my < focus.top:
            return False

        return True

    def set_pos(self, *coord):
        self.pos = (coord)

    def set_click(self, state=True):
        self.state = state

    def onclick(self):
        return self.state

    def is_hover(self):
        return

    def focus(self):
        # to do
        pass

    def release(self):
        self.set_click(False)
