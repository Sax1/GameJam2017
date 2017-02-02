import sys;
import pygame;
from pygame.locals import *;
import physic;
import magic;
import sprite;
import util;

def keyPressedDown(keys,listPlayers, nbJoueur, listDecors, listSorts,keysPressed):
    keyPressedDownP1(keys,listPlayers[0],listSorts, keysPressed);
    if(nbJoueur == 2):
        keyPressedDownP2(keys,listPlayers[1],listSorts, keysPressed);

def keyPressedDownP1(keys,player,listSorts, keysPressed):
    if(keys[K_z]):
        keysPressed[0] = 1;
    if(keys[K_d] and keysPressed[2] == 0):
        keysPressed[1] = 1;
    elif(keys[K_q] and keysPressed[1] == 0):
        keysPressed[2] = 1;
    if(keys[K_a]):
        player.changeSort(1);
    elif(keys[K_e]):
        player.changeSort(-1);
    if(keys[K_g] and keys[K_y]):
        util.lauchboulecourant(player,(-1,-1),listSorts,5);
    elif(keys[K_g] and keys[K_h]):
        util.lauchboulecourant(player,(-1,1),listSorts,3)
    elif(keys[K_h] and keys[K_j]):
        util.lauchboulecourant(player,(1,1),listSorts,1)
    elif(keys[K_j] and keys[K_y]):
        util.lauchboulecourant(player,(1,-1),listSorts,7);
    elif(keys[K_y]):
        util.lauchboulecourant(player,(0,-1),listSorts,6);
    elif(keys[K_h]):
        util.lauchboulecourant(player,(0,1),listSorts,2);
    elif(keys[K_g]):
        util.lauchboulecourant(player,(-1,0),listSorts,4);
    elif(keys[K_j]):
        util.lauchboulecourant(player,(1,0),listSorts,0);

def keyPressedDownP2(keys,player,listSorts, keysPressed):
    if(keys[K_UP]):
        keysPressed[3] = 1;
    if(keys[K_RIGHT] and keysPressed[5] == 0):
        keysPressed[4] = 1;
    elif(keys[K_LEFT] and keysPressed[4] == 0):
        keysPressed[5] = 1;
    if(keys[K_KP4]):
        player.changeSort(1);
    elif(keys[K_KP6]):
        player.changeSort(-1);
    if(keys[K_KP1] and keys[K_KP5]):
        util.lauchboulecourant(player,(-1,-1),listSorts,5);
    elif(keys[K_KP1] and keys[K_KP2]):
        util.lauchboulecourant(player,(-1,1),listSorts,3)
    elif(keys[K_KP2] and keys[K_KP3]):
        util.lauchboulecourant(player,(1,1),listSorts,1)
    elif(keys[K_KP3] and keys[K_KP5]):
        util.lauchboulecourant(player,(1,-1),listSorts,7);
    elif(keys[K_KP5]):
        util.lauchboulecourant(player,(0,-1),listSorts,6);
    elif(keys[K_KP2]):
        util.lauchboulecourant(player,(0,1),listSorts,2);
    elif(keys[K_KP1]):
        util.lauchboulecourant(player,(-1,0),listSorts,4);
    elif(keys[K_KP3]):
        util.lauchboulecourant(player,(1,0),listSorts,0);

def keyPressedUp(key,listPlayers, nbJoueur, listDecors,keysPressed):
    keyPressedUpP1(key,listPlayers[0], keysPressed);
    if(nbJoueur == 2):
        keyPressedUpP2(key,listPlayers[1],keysPressed);

def keyPressedUpP1(key,player, keysPressed):
    if(key == K_z):
        keysPressed[0]= 0;
    if(key == K_d):
        keysPressed[1] = 0;
    elif(key == K_q):
        keysPressed[2] = 0;

def keyPressedUpP2(key,player, keysPressed):
    if(key == K_UP):
        keysPressed[3] = 0;
    if(key == K_RIGHT):
        keysPressed[4] = 0;
    elif(key == K_LEFT):
        keysPressed[5] = 0;

def applyDeplacement(keysPressed,player, listDecors, playerDeplacement):
    if(player.getNumPlayer() == 1):
        if(keysPressed[0] == 1):
            if(player.getJump() == 0 and player.getLanded() == 1):
                player.setJump(1);
                player.setAscend(1);
                player.setAscendValue(10);
                player.setDeplacement(0,-player.getAscendValue());
        if(keysPressed[2] == 1):
            if(physic.isTouching('left',player,listDecors) == 0):
                player.setDeplacement(-playerDeplacement,0);
                player.set_image("./sprite/Joueur1/MageGA-1.png")
        elif(keysPressed[1] == 1):
            if(physic.isTouching('right',player,listDecors) == 0):
                player.setDeplacement(playerDeplacement,0);
                player.set_image("./sprite/Joueur1/MageDR-1.png")
    else:
        if(keysPressed[3] == 1):
            if(player.getJump() == 0 and player.getLanded() == 1):
                player.setJump(1);
                player.setAscend(1);
                player.setAscendValue(10);
                player.setDeplacement(0,-player.getAscendValue());
        if(keysPressed[5] == 1):
            if(physic.isTouching('left',player,listDecors) == 0):
                player.setDeplacement(-playerDeplacement,0);
                player.set_image("./sprite/Joueur1/MageGA-1.png")
        elif(keysPressed[4] == 1):
            if(physic.isTouching('right',player,listDecors) == 0):
                player.setDeplacement(playerDeplacement,0);
                player.set_image("./sprite/Joueur1/MageDR-1.png")
