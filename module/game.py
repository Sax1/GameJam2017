import sys;
import pygame;
from pygame.locals import *;
import physic;
import util;

def launch(window, listHUD, listDecors, listPlayers, gravity, playerDeplacement, nbJoueur, ascendDecrement):
    while 1:
        for event in pygame.event.get():
            listPlayers[0].set_image("./sprite/Joueur1/MageAV-1.png");
            keys = pygame.key.get_pressed();
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if( event.key == 27):
                    sys.exit();
                else:
                    util.actionForKeyInput(keys,listPlayers, playerDeplacement, nbJoueur, listDecors);

        for player in listPlayers:
            physic.applyGravity(player, gravity);
            physic.applyCollisionWithFloor(player, listDecors);
            physic.applyJump(player, ascendDecrement);
            physic.jumpCollide(player, listDecors);

        #display all the element on screen
        util.displayAllImages(window, listHUD);
        util.displayAllImages(window, listDecors);
        util.displayAllImages(window, listPlayers)
        pygame.display.flip();
