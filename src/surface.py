#! /user/bin/env python

import sys, pygame, resources, time, utils, menu
from time import strftime

class Surface:
    """Class Surface - Represents the main surface of the game"""

    def __init__(self):

        # game state
        self.running = False

        # flag to change screens
        self.flip = utils.switch()

        self.actual_level = 1
        self.actual_score = 0

        # screen dimensions
        self.width, self.height = resources.RESOLUTION
        self.screen = pygame.display.get_surface()

        # main menu
        self.menu = menu.Menu(self.screen)

    def cycle(self):
        """Initialize the main loop."""

        self.screen.convert()
        self.screen.fill(resources.WHITE)
        self.screen.blit(pygame.image.load(resources.BACKGROUND), (0, 0))

        # game loop
        while True:
            self.catch_events()
            font_60 = pygame.font.Font(resources.FONT, 60)

            if self.is_running():
                self.screen.blit(pygame.image.load(resources.BACKGROUND), (0, 0))
                self.screen.blit(pygame.image.load(resources.TABLE), (94, 136))



            else:
                self.menu.display(self.flip)

            # update state
            pygame.display.flip()

    def catch_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    if (resources.MAIN_MENU):
                        self.quit()
                    else:
                        self.flip.to(resources.MAIN_MENU)


            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse()
                                

    def handle_mouse(self):

        if self.menu.play.onclick():
            self.flip.to(resources.PLAYING)
            self.menu.play.release()

        elif self.menu.credits.onclick():
            self.flip.to(resources.CREDITS)
            self.menu.credits.release()

        elif self.menu.back.onclick():
            self.flip.to(resources.MAIN_MENU)

        elif self.menu.exit.onclick():
            self.quit()
        
        /* 
            Escolher modo de jogo
            Criar Cliente
            Criar Servidor
            Verificar Jogadas - IA
        */

    def update_menu(self):
        self.menu = menu.Menu(self.screen)

    def set_running(self, state=True):
        self.running = state

    def is_running(self):
        return self.running

    def is_parent(self, node, *childrens):
        return (self.node.equals(node) and self.flip.get() in childrens)

    def quit(self):
        sys.exit()
        pygame.quit()

def init():
    return Surface().cycle()
