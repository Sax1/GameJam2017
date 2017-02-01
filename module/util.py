import sys
import pygame
from pygame.locals import *;
import physic;
import magic;

#To load an image with a given path
def load_image(name):
    image = pygame.image.load(name)
    return image

#Display all images from a given list
def displayAllImages(window, listElements):
    for elem in listElements:
        window.blit(elem.get_img(),elem.get_pos());

def actionForKeyInput(keys, listPlayers, playerDeplacement, nbJoueur, listDecors, listSorts):
    touchJ1(keys,listPlayers[0],listDecors, playerDeplacement, listSorts)
    if(nbJoueur == 2):
        touchJ2(keys,listPlayers[1],listDecors, playerDeplacement, listSorts)

def touchJ1(keys, player, listDecors, playerDeplacement, listSorts):
    if(keys[122]):
        if(player.getJump() == 0 and player.getLanded() == 1):
            player.setJump(1);
            player.setAscend(1);
            player.setAscendValue(10);
            player.setDeplacement(0,-player.getAscendValue());
    if(keys[115]):
        print '1bas';
        #sys.exit();
    if( keys[113]):
        if(physic.isTouching('left',player,listDecors) == 0):
            player.setDeplacement(-playerDeplacement,0)
            player.set_image("./sprite/Joueur1/MageGA-1.png")
    if( keys[100]):
        if(physic.isTouching('right',player,listDecors) == 0):
            player.setDeplacement(playerDeplacement,0)
            player.set_image("./sprite/Joueur1/MageDR-1.png")
    if(keys[106] and keys[121]):
        print("haut droit")
        magic.launchBoule((1,-1),listSorts, player)
    elif(keys[106] and keys[104]):
        print("bas droit")
        magic.launchBoule((1,1),listSorts, player)
    elif(keys[106]):#droite
        magic.launchBoule((1,0),listSorts, player)
    elif(keys[103] and keys[104]):
        print("bas gauche")
        magic.launchBoule((-1,1),listSorts, player)
    elif(keys[103] and keys[121]):
        print("haut gauche")
        magic.launchBoule((-1,-1),listSorts, player)
    elif(keys[103]):#gauche
        print("gauche")
        magic.launchBoule((-1,0),listSorts, player)
    elif(keys[104]):#bas
        print("bas")
        magic.launchBoule((0,1),listSorts, player)
    elif(keys[121]):#haut
        print("haut")
        magic.launchBoule((0,-1),listSorts, player)

def touchJ2(keys, player, listDecors, playerDeplacement, listSorts):
    if(keys[K_UP]):
        if(player.getJump() == 0 and player.getLanded() == 1):
            player.setJump(1);
            player.setAscend(1);
            player.setAscendValue(10);
            player.setDeplacement(0,-player.getAscendValue());
    if(keys[K_DOWN]):
        print '2bas';
    if(keys[K_LEFT]):
        if(physic.isTouching('left',player,listDecors) == 0):
            player.setDeplacement(-playerDeplacement,0)
            player.set_image("./sprite/Joueur2/Mage2GA-1.png")
    if(keys[K_RIGHT]):
        if(physic.isTouching('right',player,listDecors) == 0):
            player.setDeplacement(playerDeplacement,0)
            player.set_image("./sprite/Joueur2/Mage2DR-1.png")
    if(keys[51] and keys[53]):
        print("haut droit")
        magic.launchBoule((1,-1),listSorts, player)
    elif(keys[50] and keys[51]):
        print("bas droit")
        magic.launchBoule((1,1),listSorts, player)
    elif(keys[51]):#droite
        magic.launchBoule((1,0),listSorts, player)
    elif(keys[49] and keys[50]):
        print("bas gauche")
        magic.launchBoule((-1,1),listSorts, player)
    elif(keys[49] and keys[53]):
        print("haut gauche")
        magic.launchBoule((-1,-1),listSorts, player)
    elif(keys[49]):#gauche
        print("gauche")
        magic.launchBoule((-1,0),listSorts, player)
    elif(keys[50]):#bas
        print("bas")
        magic.launchBoule((0,1),listSorts, player)
    elif(keys[53]):#haut
        print("haut")
        magic.launchBoule((0,-1),listSorts, player)
