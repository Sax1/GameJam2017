import sys
import pygame
from pygame.locals import *;
import physic;

#To load an image with a given path
def load_image(name):
    image = pygame.image.load(name)
    return image

#Display all images from a given list
def displayAllImages(window, listElements):
    for elem in listElements:
        window.blit(elem.get_img(),elem.get_pos());

def actionForKeyInput(keys, listPlayers, playerDeplacement, nbJoueur, listDecors):
    if(keys[122]):
        if(listPlayers[0].getJump() == 0 and listPlayers[0].getLanded() == 1):
            listPlayers[0].setJump(1);
            listPlayers[0].setAscend(1);
            listPlayers[0].setAscendValue(10);
            listPlayers[0].setDeplacement(0,-listPlayers[0].getAscendValue());
    if(keys[115]):
        print '1bas';
        sys.exit();
    if( keys[113]):
        if(physic.isTouching('left',listPlayers[0],listDecors) == 0):
            listPlayers[0].setDeplacement(-playerDeplacement,0)
            listPlayers[0].set_image("./sprite/Joueur1/MageGA-1.png")
    if( keys[100]):
        if(physic.isTouching('rigth',listPlayers[0],listDecors) == 0):
            listPlayers[0].setDeplacement(playerDeplacement,0)
            listPlayers[0].set_image("./sprite/Joueur1/MageDR-1.png")
    if(keys[32]):
        if(keys[106] and keys[121]):
            print("haut droit")
        elif(keys[106] and keys[104]):
            print("bas droit")
        elif(keys[106]):#droite
            print("droite")
        elif(keys[103] and keys[104]):
            print("bas gauche")
        elif(keys[103] and keys[121]):
            print("haut gauche")
        elif(keys[103]):#gauche
            print("gauche")
        elif(keys[104]):#bas
            print("bas")
        elif(keys[121]):#haut
            print("haut")
    if(nbJoueur == 2):
        if(keys[K_UP]):
            if(listPlayers[1].getJump() == 0 and listPlayers[1].getLanded() == 1):
                listPlayers[1].setJump(1);
                listPlayers[1].setAscend(1);
                listPlayers[1].setAscendValue(10);
                listPlayers[1].setDeplacement(0,-listPlayers[1].getAscendValue());
        if(keys[K_DOWN]):
            print '2bas';
        if(keys[K_LEFT]):
            listPlayers[1].setDeplacement(-playerDeplacement,0)
            listPlayers[1].set_image("./sprite/Joueur2/Mage2GA-1.png")
        if(keys[K_RIGHT]):
            listPlayers[1].setDeplacement(playerDeplacement,0)
            listPlayers[1].set_image("./sprite/Joueur2/Mage2DR-1.png")
