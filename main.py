# Nom du jeu
# Made by Team7

 #-*- coding:Utf-8 -*-

#importation des biblios
import pygame;
from pygame.locals import *;
import sys;

#On definit le path

sys.path.append('./module');

#Importation des classes
import util;
import objet;

#init
pygame.init();
#Creation de la fenetre a la de l'ecran
widowResolution = pygame.display.Info();
heigth =widowResolution.current_h;
width = widowResolution.current_w;
window  = pygame.display.set_mode((widowResolution.current_w,widowResolution.current_h), RESIZABLE);

BG = util.load_image('./data/BG.jpg');
window.blit(BG,(0,0));
pygame.display.flip();

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
