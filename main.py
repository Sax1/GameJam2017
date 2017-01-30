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

#init pygame
pygame.init();

#Creation de la fenetre a la de l'ecran
widowResolution = pygame.display.Info();
heigth = widowResolution.current_h;
width = widowResolution.current_w;
window  = pygame.display.set_mode((widowResolution.current_w,widowResolution.current_h), FULLSCREEN);

#Variables Globales
nbJoueur = 2;
#Listes des elements
listElements = [];
listElements.append(objet.Objet(0,0,'./data/BG.jpg'));
listElements.append(objet.Objet(0,heigth-20,'./data/Sol-1.png'));


while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            print event.key;
            if(event.key == 27):
                sys.exit();
            if(event.key == 122):
                print '1haut';
            if( event.key == 115):
                print '1bas';
            if( event.key == 113):
                print '1gauche';
            if( event.key == 100):
                print '1droite';
            if(nbJoueur == 2):
                if(event.key == K_UP):
                    print '2haut';
                if(event.key == K_DOWN):
                    print '2bas';
                if(event.key == K_LEFT):
                    print '2gauche';
                if(event.key == K_RIGHT):
                    print '2droite';

    #display all the element on screen
    util.displayAllImages(window, listElements);
