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
import physic;
import menu;
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
gameState = 2;
nbJoueur = 1;
gravity = 5;
playerDeplacement = 8;
ascendDecrement = 0.5;

#Creation des joueurs
joueur1 = player.Player(50,50,'./sprite/MageDR-1.png',100,1,1,"");
#if(nbJoueur == 2):
#    joueur2 = player.Player(100,100,'./sprite/MageDR-1.png',100,1,2,"");

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
    print("bouton : ",boutonRes)

#Pour avoir des inputs successifs
pygame.key.set_repeat(20,20);

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            util.actionForKeyInput(event.key,listPlayers, playerDeplacement, nbJoueur);
    for player in listPlayers:
        physic.applyGravity(player, gravity);
        physic.applyCollisionWithFloor(player, listDecors);
        physic.applyJump(player, ascendDecrement);

    #display all the element on screen
    util.displayAllImages(window, listHUD);
    util.displayAllImages(window, listDecors);
    util.displayAllImages(window, listPlayers)
    pygame.display.flip();
