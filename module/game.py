import sys;
import pygame;
from pygame.locals import *
import physic;
import util;

def launch(window, listHUD, listDecors, listPlayers, gravity, playerDeplacement, nbJoueur, ascendDecrement):
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                util.actionForKeyInput(event.key,listPlayers, playerDeplacement, nbJoueur);
        for player in listPlayers:
            physic.applyGravity(player, gravity);
            physic.applyCollisionWithFloor(player, listDecors);
            physic.applyJump(player, ascendDecrement);

            print "status : ";
            print player.getLanded();
            print player.getAscend();
        #display all the element on screen
        util.displayAllImages(window, listHUD);
        util.displayAllImages(window, listDecors);
        util.displayAllImages(window, listPlayers)
        pygame.display.flip();
