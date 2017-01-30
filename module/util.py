import sys
import pygame

def load_image(name):
    image = pygame.image.load(name)
    return image

def displayAllImages(window, listElements):
    for elem in listElements:
        window.blit(elem.get_img(),elem.get_pos());
def isLanded(j,elem):
    midBottomJoueur = (j.get_pos()[0]+(j.get_img().get_width()/2),j.get_pos()[1]+(j.get_img().get_height()));
    if(elem.get_pos()[0]<=midBottomJoueur[0] and elem.get_pos()[0]+elem.get_img().get_width() >= midBottomJoueur[0]):
        if(elem.get_pos()[1] <= midBottomJoueur[1] and elem.get_pos()[1]+elem.get_img().get_width() >= midBottomJoueur[1]):
            return 1;
    return 0;
