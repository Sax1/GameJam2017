import sys
import pygame
from pygame.locals import *;

#To load an image with a given path
def load_image(name):
    image = pygame.image.load(name)
    return image

#Display all images from a given list
def displayAllImages(window, listElements):
    for elem in listElements:
        window.blit(elem.get_img(),elem.get_pos());

def actionForKeyInput(keys, listPlayers, playerDeplacement, nbJoueur):
    if(keys[122]):
        print '1haut';
        if(listPlayers[0].getJump() == 0 and listPlayers[0].getLanded() == 1):
            listPlayers[0].setJump(1);
            listPlayers[0].setAscend(1);
            listPlayers[0].setAscendValue(10);
    if(keys[115]):
        print '1bas';
        sys.exit();
    if( keys[113]):
        listPlayers[0].setDeplacement(-playerDeplacement,0)
    if( keys[100]):
        listPlayers[0].setDeplacement(playerDeplacement,0)
    if(nbJoueur == 2):
        if(keys[K_UP]):
            print '2haut';
        if(keys[K_DOWN]):
            print '2bas';
        if(keys[K_LEFT]):
            listPlayers[1].setDeplacement(-playerDeplacement,0)
        if(keys[K_RIGHT]):
            listPlayers[1].setDeplacement(playerDeplacement,0)
