# Nom du jeu
# Made by Team7

# -*- coding:Utf-8 -*-

#importation des biblios
import pygame;
from pygame.locals import *;
import sys;

#Importation des classes

#init
pygame.init();
#Création de la fenetre à la de l'écran
widowResolution = pygame.display.Info();
heigth =widowResolution.current_h;
width = widowResolution.current_w;
window  = pygame.display.set_mode((widowResolution.current_w,widowResolution.current_h), RESIZABLE);

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
