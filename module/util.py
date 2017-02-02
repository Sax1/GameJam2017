import sys
import pygame
from pygame.locals import *;
import physic;
import magic;
import sprite

#To load an image with a given path
def load_image(name):
    image = pygame.image.load(name)
    return image

#Display all images from a given list
def displayAllImages(window, listElements):
    for elem in listElements:
        window.blit(elem.get_img(),elem.get_pos());

def displayAllPv(window,listElements):
    for elem in listElements:
        window.blit(elem[0],elem[1]);

def actionForKeyInput(keys, listPlayers, playerDeplacement, nbJoueur, listDecors, listSorts,keysPressed):
    touchJ1(keys,listPlayers[0],listDecors, playerDeplacement, listSorts,keysPressed)
    if(nbJoueur == 2):
        touchJ2(keys,listPlayers[1],listDecors, playerDeplacement, listSorts,keysPressed)

def lauchboulecourant(player, playerDeplacement, listSorts,direction):
    if (player.sortCourant == 0):
        magic.launchBoule(playerDeplacement,listSorts[0], player,direction)
    elif(player.sortCourant == 1):
        magic.launchBoule(playerDeplacement,listSorts[1], player,direction)
    elif(player.sortCourant == 2):
        magic.launchBoule(playerDeplacement,listSorts[2], player,direction)


def touchJ1(keys, player, listDecors, playerDeplacement, listSorts):
    x = 0;
    y = 0;
    if(keys[122]):
        if(player.getJump() == 0 and player.getLanded() == 1):
            player.setJump(1);
            player.setAscend(1);
            player.setAscendValue(10);
            y = -player.getAscendValue();
    if( keys[113]):
        if(physic.isTouching('left',player,listDecors) == 0):
            x = -playerDeplacement;
            player.set_image("./sprite/Joueur1/MageGA-1.png")
    elif( keys[100]):
        if(physic.isTouching('right',player,listDecors) == 0):
            x = playerDeplacement;
            player.set_image("./sprite/Joueur1/MageDR-1.png")
    if(keys[101]):
        player.changeSort(1)
    elif(keys[97]):
        player.changeSort(-1)
    elif(keys[106] and keys[121]):
        lauchboulecourant(player,(1,-1),listSorts,7)
    elif(keys[106] and keys[104]):
        lauchboulecourant(player,(1,1),listSorts,1)
    elif(keys[106]):#droite
        lauchboulecourant(player,(1,0),listSorts,0)
        pygame.mixer.music.load("./data/Musiques/boulefeu.wav");
        pygame.mixer.music.play();
    elif(keys[103] and keys[104]):
        lauchboulecourant(player,(-1,1),listSorts,3)
    elif(keys[103] and keys[121]):
        lauchboulecourant(player,(-1,-1),listSorts,5)
    elif(keys[103]):#gauche
        lauchboulecourant(player,(-1,0),listSorts,4)
    elif(keys[104]):#bas
        lauchboulecourant(player,(0,1),listSorts,2)
    elif(keys[121]):#haut
        player.setDeplacement(x,y);

def touchJ2(keys, player, listDecors, playerDeplacement, listSorts):
    if(keys[K_UP]):
        if(player.getJump() == 0 and player.getLanded() == 1):
            player.setJump(1);
            player.setAscend(1);
            player.setAscendValue(10);
            player.setDeplacement(0,-player.getAscendValue());
    if(keys[K_LEFT]):
        if(physic.isTouching('left',player,listDecors) == 0):
            player.setDeplacement(-playerDeplacement,0)
            player.set_image("./sprite/Joueur2/Mage2GA-1.png")
    elif(keys[K_RIGHT]):
        if(physic.isTouching('right',player,listDecors) == 0):
            player.setDeplacement(playerDeplacement,0)
            player.set_image("./sprite/Joueur2/Mage2DR-1.png")
    if(keys[54]):
        player.changeSort(1)
    elif(keys[52]):
        player.changeSort(-1)
    elif(keys[51] and keys[53]):
        lauchboulecourant(player,(1,-1),listSorts,7)
    elif(keys[50] and keys[51]):
        lauchboulecourant(player,(1,1),listSorts,1)
    elif(keys[51]):#droite
        lauchboulecourant(player,(1,0),listSorts,0)
    elif((keys[49] or keys[257]) and (keys[50] or keys[258])):
        lauchboulecourant(player,(-1,1),listSorts,3)
    elif((keys[49] or keys[257]) and (keys[53] or keys[261])):
        lauchboulecourant(player,(-1,-1),listSorts,5)
    elif(keys[49] or keys[257]):#gauche
        lauchboulecourant(player,(-1,0),listSorts,4)
    elif(keys[50] or keys[258]):#bas
        lauchboulecourant(player,(0,1),listSorts,2)
    elif(keys[53] or keys[261]):#haut
        lauchboulecourant(player,(0,-1),listSorts,6)

def setHUD(window, pathhud):
    posf = window.get_rect();
    HUD = sprite.Sprite(0,0,pathhud);
    img = HUD.get_img()
    img = pygame.transform.scale(img, (posf.right, HUD.get_img().get_height()));
    HUD.set_image2(img);
    return HUD;

def setHUDPV(window, player,numPlayer):
    basicfont = pygame.font.SysFont("Arial", 48)
    PV = basicfont.render(str(player.get_hp()), True, (255,255,255))
    textrect = PV.get_rect()
    if (numPlayer==1):
        textrect.x = window.get_width()*3/16
        textrect.y = window.get_height()/10
    else:
        textrect.x = window.get_width()*13/16
        textrect.y = window.get_height()/10
    packPV = [PV,textrect,window,player,numPlayer]
    return packPV
