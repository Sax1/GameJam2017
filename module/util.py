import sys
import pygame

def load_image(name):
    image = pygame.image.load(name)
    return image

def displayAllImages(window, listElements):
    for elem in listElements:
        window.blit(elem.get_img(),elem.get_pos());
    pygame.display.flip();
