#importation des biblios
import pygame;
from pygame.locals import *;
import sys;

def menuprin(window,width,height):
    #fond du menu
    posf = window.get_rect()
    fond_e = pygame.image.load("data/menubackgroundCastle.png").convert()
    fond = pygame.transform.scale(fond_e, (posf.right, posf.bottom))
    window.blit(fond,(0,0))

    #creation des boutons
    button1j = pygame.image.load("data/menu1joueur.png")
    button2j = pygame.image.load("data/menu2joueur.png")
    buttonop = pygame.image.load("data/boutonoption.png")
    buttoncred = pygame.image.load("data/boutoncredit.png")
    buttonquit = pygame.image.load("data/boutonquitter.png")

    #redimension des boutons
    #button1j = pygame.transform.scale(button1j, (width*4/16, height*5/16))
    #button2j = pygame.transform.scale(button2j, (width*4/16, height*5/16))
    #buttonop = pygame.transform.scale(buttonop, (width*4/16, height*5/32))
    #buttoncred = pygame.transform.scale(buttoncred, (width*4/16, height*5/32))
    #buttonquit = pygame.transform.scale(buttonquit, (width*4/16, height*5/32))

    #ajout des boutons
    window.blit(button1j, (width/16,height/6))
    window.blit(button2j, (width*11/16,height/6))
    window.blit(buttonop, (width/16,(height*3/6)+145))
    window.blit(buttoncred, (width*6/16,(height*3/6)+145))
    window.blit(buttonquit, (width*11/16,(height*3/6)+145))

    # Affichage deun Nomjeu au centre de la fenetre
    basicfont = pygame.font.SysFont("Winks", 48)
    text = basicfont.render('Nomjeu', True, (0,0,0))
    textrect = text.get_rect()
    textrect.x = width*6/16
    textrect.y = height/6
    window.blit(text, textrect)
    pygame.display.flip()

    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = 0
            elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
                if event.button == 1: # 1= clique gauche
                    if button1j.get_rect(left=width/16,top=height/6).collidepoint(event.pos):
                        return 1 #bouton 1joueur
                    elif button2j.get_rect(left=width*11/16,top=height/6).collidepoint(event.pos):
                        return 2 #bouton 2joueur
                    elif buttonop.get_rect(left=width/16,top=(height*3/6)+145).collidepoint(event.pos):
                        return 3 #bouton options
                    elif buttoncred.get_rect(left=width*6/16,top=(height*3/6)+145).collidepoint(event.pos):
                        return 4 #bouton credits
                    elif buttonquit.get_rect(left=width*11/16,top=(height*3/6)+145).collidepoint(event.pos):
                        return 5 #bouton quitter

def menuop(window,width,height):
    #fond du menu
    posf = window.get_rect()
    fond_e = pygame.image.load("data/menubackgroundCastle.png").convert()
    fond = pygame.transform.scale(fond_e, (posf.right, posf.bottom))
    window.blit(fond,(0,0))

    #creation des boutons
    button1j = pygame.image.load("data/menu1joueur.png")
    button2j = pygame.image.load("data/menu2joueur.png")
    buttonop = pygame.image.load("data/boutonoption.png")
    buttoncred = pygame.image.load("data/boutoncredit.png")
    buttonquit = pygame.image.load("data/boutonquitter.png")
