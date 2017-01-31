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
import game;
import physic;
import menu;
import sprite;
import character;
import player;
import factory;
import levels;


#init pygame
pygame.init();
pygame.key.set_repeat(20,20);


#Creation de la fenetre a la de l'ecran
widowResolution = pygame.display.Info();
heigth = widowResolution.current_h;
width = widowResolution.current_w;
window  = pygame.display.set_mode((widowResolution.current_w,widowResolution.current_h), FULLSCREEN);

#Variables Globales
gameState = 1;
nbJoueur = 1;
gravity = 5;
playerDeplacement = 8;
ascendDecrement = 0.2;

#Creation des joueurs
listPlayers = [];
listPlayers.append(player.Player(50,50,'./sprite/Joueur1/MageAV-1.png',100,1,1,""));

#Listes des elements
posf = window.get_rect()
sparte = sprite.Sprite(0,0,'./data/menubackgroundCastle.png')
img = sparte.get_img().convert()
img = pygame.transform.scale(img, (posf.right, posf.bottom))
sparte.set_image2(img)
listHUD = [];
listHUD.append(sparte);
listDecors = [];
listDecors.append(sprite.Sprite(0,0,'./data/Sol-1.png'));
listDecors.append(sprite.Sprite(0,heigth-20,'./data/Sol-1.png'));
listDecors.append(sprite.Sprite(0,500,'./data/SolR1-1.png'));
listDecors.append(sprite.Sprite(0,0,'./data/Mur1-1.png'));
listDecors.append(sprite.Sprite(width-20,0,'./data/Mur1-1.png'));

################################################################################
################################ MAIN BOUCLE ###################################
################################################################################
while 1:
    if(gameState == 1):
        boutonRes = menu.menuprin(window,width,heigth)
        if(boutonRes==1):
            nbJoueur = 1;
            game.launch(window, listHUD, listDecors, listPlayers, gravity, playerDeplacement, nbJoueur, ascendDecrement);
        elif(boutonRes==2):
            nbJoueur = 2;
            if(len(listPlayers) == 1):
                listPlayers.append(player.Player(100,100,'./sprite/Joueur1/Mage2AV-1.png',100,1,2,""));
            game.launch(window, listHUD, listDecors, listPlayers, gravity, playerDeplacement, nbJoueur, ascendDecrement);
        elif(boutonRes==3):
            menu.menuop(window,width,heigth)
        elif(boutonRes==4):
            #menu.menucred
            print "4";
            factory.listeboulefeu()
        elif(boutonRes==5):
            sys.exit()
    else:
        game.launch(window, listHUD, listDecors, listPlayers, gravity, playerDeplacement, nbJoueur, ascendDecrement);
