import sys
import pygame

#Test if the player is on an element
def isLanded(j,elem):
    midBottomJoueur = (j.get_pos()[0]+(j.get_img().get_width()/2),j.get_pos()[1]+(j.get_img().get_height()));
    if(elem.get_pos()[0]<=midBottomJoueur[0] and elem.get_pos()[0]+elem.get_img().get_width() >= midBottomJoueur[0] and elem.get_pos()[1] <= midBottomJoueur[1] and elem.get_pos()[1]+elem.get_img().get_height() >= midBottomJoueur[1]):
        return 1;
    else:
        return 0;

def isTouching(dir,j,listDecors):
    if(dir == 'top'):
        pointPlayer = (j.get_pos()[0]+(j.get_img().get_width()/2),j.get_pos()[1]);
        print 'Nope';
    elif(dir == 'rigth'):
        pointPlayer = (j.get_pos()[0]+(j.get_img().get_width()),j.get_pos()[1]+(j.get_img().get_height()/2));
    elif(dir == 'left'):
        pointPlayer = (j.get_pos()[0],j.get_pos()[1]+(j.get_img().get_height()/2));
        print 'nopeBis';

def applyCollisionWithFloor(player, listDecors):
    for elem in listDecors:
        if(isLanded(player, elem) == 1):
            player.setLanded(1);
            player.setJump(0);
            player.setAscend(0);
            player.setAscendValue(10);
            break;
        else:
            player.setLanded(0);

def applyGravity(player, gravity):
    if(player.getAscend() == 0 and player.getLanded() == 0 and player.getJump() == 0):
        player.setDeplacement(0,gravity);

def applyJump(player, ascendDecrement):
    if(player.getJump() == 1 and player.getAscendValue() != 0):
        player.setDeplacement(0, -player.getAscendValue());
        player.setAscendValue(player.getAscendValue()-ascendDecrement);
    elif(player.getJump() == 1 and player.getAscendValue() == 0):
        player.setJump(0);
        player.setAscend(0);
        player.setAscendValue(10);
