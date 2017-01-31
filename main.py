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
ascendDecrement = 0.5;

#Creation des joueurs
joueur1 = player.Player(50,50,'./sprite/MageDR-1.png',100,1,1,"");
#if(nbJoueur == 2):
joueur2 = player.Player(100,100,'./sprite/MageDR-1.png',100,1,2,"");

#Listes des elements
listHUD = [];
listHUD.append(sprite.Sprite(0,0,'./data/BG.jpg'));
listDecors = [];
listDecors.append(sprite.Sprite(0,heigth-20,'./data/Sol-1.png'));
listDecors.append(sprite.Sprite(0,500,'./sprite/SolR1-1.png'));
listPlayers = [];
listPlayers.append(joueur1);

################################################################################
################################ MAIN BOUCLE ###################################
################################################################################
if(gameState == 1):
    boutonRes = menu.menuprin(window,width,heigth)
    if(boutonRes==1):
        game.launch(window, listHUD, listDecors, listPlayers, gravity, playerDeplacement, nbJoueur, ascendDecrement);
    elif(boutonRes==2):
        #appel boucle principale avec j2
        listPlayers.append(joueur2);
        nbJoueur= 2;
        game.launch(window, listHUD, listDecors, listPlayers, gravity, playerDeplacement, nbJoueur, ascendDecrement);
        print "2";
    elif(boutonRes==3):
        menu.menuop(window,width,heigth)
        print "3";
    elif(boutonRes==4):
        #menu.menucred
        print "4";
    elif(boutonRes==5):
        print "5";
        sys.exit()
