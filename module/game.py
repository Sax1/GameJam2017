import sys;
import pygame;
from pygame.locals import *;
import physic;
import util;
import magic;
import projectile;

def launch(window, listHUD, listDecors, listPlayers, gravity, playerDeplacement, nbJoueur, ascendDecrement,listSorts,height,width):
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
                    util.actionForKeyInput(keys,listPlayers, playerDeplacement, nbJoueur, listDecors, listSorts);

        for player in listPlayers:
            if(not player.isDead()):
                physic.applyGravity(player, gravity);
                physic.applyCollisionWithFloor(player, listDecors);
                physic.applyJump(player, ascendDecrement);
                physic.jumpCollide(player, listDecors);
        magic.applySort(listSorts,listPlayers,height,width)

        #display all the element on screen
        util.displayAllImages(window, listHUD);
        util.displayAllImages(window, listPlayers);
        util.displayAllImages(window, listSorts);
        util.displayAllImages(window, listDecors);

        pygame.display.flip();
