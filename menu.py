#importation des biblios
import pygame;
from pygame.locals import *;
import sys;

def menuprin(window,width,height):

    button1j = pygame.image.load("data/menu1joueur.png")
    button2j = pygame.image.load("data/menu2joueur.png")
    buttonop = pygame.image.load("data/boutonoption.png")
    buttoncred = pygame.image.load("data/boutoncredit.png")
    buttonquit = pygame.image.load("data/boutonquitter.png")

    window.blit(button1j, (width/16,height/6))
    window.blit(button2j, (width*11/16,height/6))
    window.blit(buttonop, (width/16,(height*3/6)+145))
    window.blit(buttoncred, (width*6/16,(height*3/6)+145))
    window.blit(buttonquit, (width*11/16,(height*3/6)+145))
    pygame.display.flip()
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = 0

            elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
                if event.button == 1: # 1= clique gauche
                    if clickable_area.collidepoint(event.pos):
                        color_index = (color_index + 1) % 3
                        rect_surf.fill(COLORS[color_index])
