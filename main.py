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
import mobs;
import factory;
import levels;


#init pygame
pygame.init();
pygame.key.set_repeat(200,20);


#Creation de la fenetre a la de l'ecran
widowResolution = pygame.display.Info();
height = widowResolution.current_h;
width = widowResolution.current_w;
window  = pygame.display.set_mode((widowResolution.current_w,widowResolution.current_h), FULLSCREEN);

#Variables Globales
gameState = 1;
nbJoueur = 1;
gravity = 12;
playerDeplacement = 8;
ascendDecrement = 0.2;

#Creation des joueurs
listPlayers = [];
listPlayers.append(player.Player(850,900,'./sprite/Joueur1/MageAV-1.png', 100, 1," ",1,""));

#Creation des ennemis
listEnnemis = [];
ListSquelette1 = factory.listeskelet(100,50);
ListSquelette2 = factory.listeskelet(950,50);
ListSquelette3 = factory.listeskelet(1600,50);
listEnnemis.append(ListSquelette1);
listEnnemis.append(ListSquelette2);
listEnnemis.append(ListSquelette3);

#Listes des elements
tabPathBDF = ['./sprite/attaques+mobs/BouledeFeu/bouledefeuD.png','./sprite/attaques+mobs/BouledeFeu/bouledefeuBD.png','./sprite/attaques+mobs/BouledeFeu/bouledefeuB.png','./sprite/attaques+mobs/BouledeFeu/bouledefeuBG.png','./sprite/attaques+mobs/BouledeFeu/bouledefeuG.png','./sprite/attaques+mobs/BouledeFeu/bouledefeuHG.png','./sprite/attaques+mobs/BouledeFeu/bouledefeuH.png','./sprite/attaques+mobs/BouledeFeu/bouledefeuHD.png']
tabPathPDG = ['./sprite/attaques+mobs/PicDeGlace/picGlaceD.png','./sprite/attaques+mobs/PicDeGlace/picGlaceBD.png','./sprite/attaques+mobs/PicDeGlace/picGlaceB.png','./sprite/attaques+mobs/PicDeGlace/picGlaceBG.png','./sprite/attaques+mobs/PicDeGlace/picGlaceG.png','./sprite/attaques+mobs/PicDeGlace/picGlaceHG.png','./sprite/attaques+mobs/PicDeGlace/picGlaceH.png','./sprite/attaques+mobs/PicDeGlace/picGlaceHD.png']
tabPathV = ['./sprite/attaques+mobs/Tornade/Tornade-1.png','./sprite/attaques+mobs/Tornade/Tornade-1.png','./sprite/attaques+mobs/Tornade/Tornade-1.png','./sprite/attaques+mobs/Tornade/Tornade-1.png','./sprite/attaques+mobs/Tornade/Tornade-1.png','./sprite/attaques+mobs/Tornade/Tornade-1.png','./sprite/attaques+mobs/Tornade/Tornade-1.png','./sprite/attaques+mobs/Tornade/Tornade-1.png']

listeSort = [factory.listeboulefeu(tabPathBDF),factory.listePicGlace(tabPathPDG),factory.listeVent(tabPathV)]

posf = window.get_rect()
BG = sprite.Sprite(0,0,'./data/menubackgroundCastle.png')
img = BG.get_img()
img = pygame.transform.scale(img, (posf.right, posf.bottom))
BG.set_image2(img)



listBG = [];
listBG.append(BG);
listHUD = [];
listHUD.append(util.setHUD(window, './data/HUD/HUD1Joueur.png'));
listDecors = [];
listDecors.append(sprite.Sprite(0,-20,'./data/Sol-1.png'));
listDecors.append(sprite.Sprite(0,height-20,'./data/Sol-1.png'));
listDecors.append(sprite.Sprite(0,0,'./data/Mur1-1.png'));
listDecors.append(sprite.Sprite(width-20,0,'./data/Mur1-1.png'));

################################################################################
################################ MAIN BOUCLE ###################################
################################################################################
while 1:
    if(gameState == 1):
        boutonRes = menu.menuprin(window,width,height)
        if(boutonRes==1):
            nbJoueur = 1;
            listHUD.append(util.setHUD(window, './data/HUD/HUD1Joueur.png'));
            game.launch(window,listBG, listHUD, listDecors, listPlayers,listEnnemis, gravity, playerDeplacement, nbJoueur, ascendDecrement,listeSort,height,width);
        elif(boutonRes==2):
            nbJoueur = 2;
            listHUD.append(util.setHUD(window, './data/HUD/HUD2Joueur.png'));
            if(len(listPlayers) == 1):
                listPlayers.append(player.Player(900,900,'./sprite/Joueur2/Mage2AV-1.png',100,1," ",2,""));
            game.launch(window,listBG, listHUD, listDecors, listPlayers, listEnnemis, gravity, playerDeplacement, nbJoueur, ascendDecrement,listeSort,height,width);
        elif(boutonRes==3):
            menu.menuop(window,width,height)
        elif(boutonRes==4):
            #menu.menucred
            print "4";
            factory.listeboulefeu()
        elif(boutonRes==5):
            sys.exit()
    else:
        listHUD.append(util.setHUD(window, './data/HUD/HUD1Joueur.png'));
        game.launch(window,listBG, listHUD, listDecors, listPlayers, listEnnemis, gravity, playerDeplacement, nbJoueur, ascendDecrement,listeSort,height,width);
