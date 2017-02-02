import sys;
import pygame;
from pygame.locals import *;
import sprite;

def loadLevel(numLevel,listDecors):
    if (numLevel == 1):
    #etage1
        listDecors.append(sprite.Sprite(20,810,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(220,810,'./data/Decors/Plateforme-1.png'));
        #listDecors.append(sprite.Sprite(420,810,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(620,810,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(820,810,'./data/Decors/Plateforme-1.png'));
        #listDecors.append(sprite.Sprite(1020,810,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(1220,810,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(1420,810,'./data/Decors/Plateforme-1.png'));
        #listDecors.append(sprite.Sprite(1460,810,'./data/Decors/Plateforme-1.png'));

        #listDecors.append(sprite.Sprite(220,810,'./data/Decors/Mur-1.png'));
        #listDecors.append(sprite.Sprite(1420,810,'./data/Decors/Mur-1.png'));

        #etage2
        #listDecors.append(sprite.Sprite(20,580,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(220,580,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(420,580,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(620,580,'./data/Decors/Plateforme-1.png'));
        #listDecors.append(sprite.Sprite(820,580,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(1020,580,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(1220,580,'./data/Decors/Plateforme-1.png'));
        #listDecors.append(sprite.Sprite(1420,580,'./data/Decors/Plateforme-1.png'));
        #listDecors.append(sprite.Sprite(1460,580,'./data/Decors/Plateforme-1.png'));

        #listDecors.append(sprite.Sprite(220,330,'./data/Decors/Mur-1.png'));

        #etage3
        listDecors.append(sprite.Sprite(20,330,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(220,330,'./data/Decors/Plateforme-1.png'));
        #listDecors.append(sprite.Sprite(420,330,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(620,330,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(820,330,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(1020,330,'./data/Decors/Plateforme-1.png'));
        #listDecors.append(sprite.Sprite(1220,330,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(1420,330,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(1510,330,'./data/Decors/Plateforme-1.png'));

        #listDecors.append(sprite.Sprite(420,580,'./data/Decors/Mur-1.png'));

        #plafond
        listDecors.append(sprite.Sprite(20,0,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(220,0,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(420,0,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(620,0,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(820,0,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(1020,0,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(1220,0,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(1420,0,'./data/Decors/Plateforme-1.png'));
        listDecors.append(sprite.Sprite(1460,0,'./data/Decors/Plateforme-1.png'));

        listDecors.append(sprite.Sprite(220,20,'./data/Decors/Mur-1.png'));
        listDecors.append(sprite.Sprite(820,20,'./data/Decors/Mur-1.png'));
        listDecors.append(sprite.Sprite(1020,20,'./data/Decors/Mur-1.png'));
        listDecors.append(sprite.Sprite(1510,20,'./data/Decors/Mur-1.png'));

    else:
        print("Bla");
