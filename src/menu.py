#! /usr/bin/env python

import pygame, resources, utils, button, os

class Menu:
        """Menu Screen"""

        def __init__(self, screen):
            self.screen = screen
            self.background = pygame.image.load(resources.BACKGROUND)
            self.background_rect = self.background.get_rect()

            self.play = button.Button(self.screen, resources.BUTTONS, resources.CUT_PLAY, 320, 410)
            self.credits = button.Button(self.screen, resources.BUTTONS, resources.CUT_CREDITS, 120, 218)
            self.back = button.Button(self.screen, resources.BUTTONS, resources.CUT_BACK, 505, 670)
            self.exit = button.Button(self.screen, resources.BUTTONS, resources.CUT_EXIT, 538, 605)

            self.creditsTextLine0 = 'Jogo Da Velha desenvolvido para'
            self.creditsTextLine1 = 'disciplina de Nivelamento em'
            self.creditsTextLine2 = 'Linux/GIT.'
            self.creditsTextLine3 = 'Desenvolvido por:'
            self.creditsTextLine4 = '   - Cicera Rodrigues'
            self.creditsTextLine5 = '   - Ketille Kalyane'
            self.creditsTextLine6 = '   - Lucas dos Santos'
            self.creditsTextLine7 = 'PEM - Projeto para Excelencia em Microeletonica.'
            self.font_26 = pygame.font.Font(resources.FONT, 30)
            self.font_20 = pygame.font.Font(resources.FONT, 20)
            self.creditsTextLine0Render = self.font_26.render(self.creditsTextLine0, 1, (0,0,0))
            self.creditsTextLine1Render = self.font_26.render(self.creditsTextLine1, 1, (0,0,0))
            self.creditsTextLine2Render = self.font_26.render(self.creditsTextLine2, 1, (0,0,0))
            self.creditsTextLine3Render = self.font_26.render(self.creditsTextLine3, 1, (0,0,0))
            self.creditsTextLine4Render = self.font_26.render(self.creditsTextLine4, 1, (0,0,0))
            self.creditsTextLine5Render = self.font_26.render(self.creditsTextLine5, 1, (0,0,0))
            self.creditsTextLine6Render = self.font_26.render(self.creditsTextLine6, 1, (0,0,0))
            self.creditsTextLine7Render = self.font_20.render(self.creditsTextLine7, 1, (0,0,0))


        def update(self):
            self.screen.blit(self.background, self.background_rect)

        def display(self, flip):

            self.update()

            if flip.equals(resources.PLAYING):
                self.set_background(resources.BACKGROUND)

            elif flip.equals(resources.CREDITS):
                self.set_background(resources.BACKGROUND)
                self.screen.blit(pygame.image.load(resources.LOGO), (26, 26))
                self.screen.blit(pygame.image.load(resources.TABLE), (94, 136))
                self.screen.blit(pygame.image.load(resources.BACKGROUND_CREDITS), (94, 136))
                self.screen.blit(self.creditsTextLine0Render, (109,146))
                self.screen.blit(self.creditsTextLine1Render, (109,186))
                self.screen.blit(self.creditsTextLine2Render, (109,226))
                self.screen.blit(self.creditsTextLine3Render, (109,341))
                self.screen.blit(self.creditsTextLine4Render, (109,391))
                self.screen.blit(self.creditsTextLine5Render, (109,421))
                self.screen.blit(self.creditsTextLine6Render, (109,451))
                self.screen.blit(self.creditsTextLine7Render, (109,541))

                self.back.show()

            else:
                self.set_background(resources.BACKGROUND)
                self.screen.blit(pygame.image.load(resources.LOGO), (26, 26))
                self.screen.blit(pygame.image.load(resources.TABLE), (94, 136))
                self.play.show()
                self.credits.show()
                self.exit.show()


        def set_background(self, background):
            self.background = pygame.image.load(background)