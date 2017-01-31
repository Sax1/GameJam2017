import sys
import pygame

#To load an image with a given path
def load_image(name):
    image = pygame.image.load(name)
    return image

#Display all images from a given list
def displayAllImages(window, listElements):
    for elem in listElements:
        window.blit(elem.get_img(),elem.get_pos());

def actionForKeyInput(keyValue, listPlayers, playerDeplacement, nbJoueur):
    #print keyValue;
    if(keyValue == 27):
        sys.exit();
    if(keyValue == 122):
        print '1haut';
        if(player.getJump() == 0):
            player.setJump(1);
            player.setAscend(1);
            player.setAscendValue(10);
    if( keyValue == 115):
        print '1bas';
    if( keyValue == 113):
        listPlayers[0].setDeplacement(-playerDeplacement,0)
    if( keyValue == 100):
        listPlayers[0].setDeplacement(playerDeplacement,0)
    if(nbJoueur == 2):
        if(keyValue == K_UP):
            print '2haut';
        if(keyValue == K_DOWN):
            print '2bas';
        if(keyValue == K_LEFT):
            listPlayers[1].setDeplacement(-playerDeplacement,0)
        if(keyValue == K_RIGHT):
            listPlayers[1].setDeplacement(playerDeplacement,0)
