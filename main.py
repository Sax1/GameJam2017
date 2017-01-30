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
import sprite;
import character;
import player;

#init pygame
pygame.init();

#Creation de la fenetre a la de l'ecran
widowResolution = pygame.display.Info();
heigth = widowResolution.current_h;
width = widowResolution.current_w;
window  = pygame.display.set_mode((widowResolution.current_w,widowResolution.current_h), FULLSCREEN);

#Variables Globales
nbJoueur = 1;
gravity = 5;
playerDeplacement = 8;
#Creation des joueurs
joueur1 = player.Player(50,50,'./sprite/MageDR-1.png',100,1,1,"");
#if(nbJoueur == 2):
#    joueur2 = player.Player(100,100,'./sprite/MageDR-1.png',100,1,2,"");
#Listes des elements
listHUD = [];
listHUD.append(sprite.Sprite(0,0,'./data/BG.jpg'));
listDecors = [];
listDecors.append(sprite.Sprite(0,heigth-20,'./data/Sol-1.png'));
listPlayers = [];
listPlayers.append(joueur1);

pygame.key.set_repeat(20,20);
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            #print event.key;
            if(event.key == 27):
                sys.exit();
            if(event.key == 122):
                print '1haut';
            if( event.key == 115):
                print '1bas';
            if( event.key == 113):
                print '1gauche';
                joueur1.setDeplacement(-playerDeplacement,0)
            if( event.key == 100):
                print '1droit'
                joueur1.setDeplacement(playerDeplacement,0)
            if(nbJoueur == 2):
                if(event.key == K_UP):
                    print '2haut';
                if(event.key == K_DOWN):
                    print '2bas';
                if(event.key == K_LEFT):
                    print '2gauche';
                if(event.key == K_RIGHT):
                    print '2droite';
    if(joueur1.getAscend() == 0):
        joueur1.setDeplacement(0,gravity);

    #display all the element on screen
    util.displayAllImages(window, listHUD);
    util.displayAllImages(window, listDecors);
    util.displayAllImages(window, listPlayers)
    pygame.display.flip();
