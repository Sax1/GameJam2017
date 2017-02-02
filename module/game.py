import sys;
import pygame;
from pygame.locals import *;
import physic;
import util;
import magic;
import projectile;
import mobs;
import levels;


def launch(window,listBG, listHUD, listDecors, listPlayers, listEnnemis, gravity, playerDeplacement, nbJoueur, ascendDecrement,listSorts,height,width,listCombo,lap):
    levels.loadLevel(1,listDecors);
    while 1:
        for event in pygame.event.get():
            listPlayers[0].set_image("./sprite/Joueur1/MageAV-1.png");
            if (nbJoueur ==2):
                lap = lap+1;
                listPlayers[1].set_image("./sprite/Joueur2/Mage2AV-1.png");
            elif (lap != 0 and nbJoueur !=2):
                listPlayers[1].set_pos(-3000,0);
            keys = pygame.key.get_pressed();
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if( event.key == 27):
                    sys.exit();
                else:
                    util.actionForKeyInput(keys,listPlayers, playerDeplacement, nbJoueur, listDecors, listSorts);

        for player in listPlayers:
            physic.applyGravity(player, gravity);
            physic.applyCollisionWithFloor(player, listDecors);
            physic.applyJump(player, ascendDecrement);
            physic.jumpCollide(player, listDecors);
        magic.applySort(listSorts,listPlayers,height,width,listCombo)


        #for mobs in listEnnemis:
        for squelette in listEnnemis[0]:
            if(not squelette.isDead()):
                physic.applyGravity(squelette, gravity);
                physic.applyCollisionWithFloor(squelette, listDecors);
                physic.applyJump(squelette, ascendDecrement);
                physic.jumpCollide(squelette, listDecors);
                if(len(listPlayers) == 2):
                    if ( (abs(squelette.pos_x-listPlayers[0].pos_x)+23) < (abs(squelette.pos_x-listPlayers[1].pos_x)+43) ):
                        jCible = listPlayers[0];
                    else:
                        jCible = listPlayers[1];
                    if (squelette.pos_x+23 < jCible.pos_x+43):
                        squelette.setDeplacement(6,0);
                    elif (squelette.pos_x+23 > jCible.pos_x+43):
                        squelette.setDeplacement(-6,0);
                else:
                    jCible = listPlayers[0];
                    if (squelette.pos_x+23 < jCible.pos_x+43):
                        squelette.setDeplacement(6,0);
                    elif (squelette.pos_x+23 > jCible.pos_x+43):
                        squelette.setDeplacement(-6,0);
                magic.contactHurting(jCible, squelette)
        magic.applySort(listSorts,listEnnemis[0],height,width,listCombo)


        magic.applySort(listSorts,listEnnemis[0],height,width,listCombo)
        for e in pygame.event.get():
            if(e.type == pygame.USEREVENT):
                for combos in listCombo:
                    for combo in combos:
                        combo.reinitProjectile()


        for squelette in listEnnemis[1]:
            if(not squelette.isDead()):
                physic.applyGravity(squelette, gravity);
                physic.applyCollisionWithFloor(squelette, listDecors);
                physic.applyJump(squelette, ascendDecrement);
                physic.jumpCollide(squelette, listDecors);
                if(len(listPlayers) == 2):
                    if ( (abs(squelette.pos_x-listPlayers[0].pos_x)+23) < (abs(squelette.pos_x-listPlayers[1].pos_x)+43) ):
                        jCible = listPlayers[0];
                    else:
                        jCible = listPlayers[1];
                    if (squelette.pos_x+23 < jCible.pos_x+43):
                        squelette.setDeplacement(6,0);
                    elif (squelette.pos_x+23 > jCible.pos_x+43):
                        squelette.setDeplacement(-6,0);
                else:
                    jCible = listPlayers[0];
                    if (squelette.pos_x+23 < jCible.pos_x+43):
                        squelette.setDeplacement(6,0);
                    elif (squelette.pos_x+23 > jCible.pos_x+43):
                        squelette.setDeplacement(-6,0);
                magic.contactHurting(jCible, squelette)
        magic.applySort(listSorts,listEnnemis[1],height,width,listCombo)


        for squelette in listEnnemis[2]:
            if(not squelette.isDead()):
                physic.applyGravity(squelette, gravity);
                physic.applyCollisionWithFloor(squelette, listDecors);
                physic.applyJump(squelette, ascendDecrement);
                physic.jumpCollide(squelette, listDecors);
                if(len(listPlayers) == 2):
                    if ( (abs(squelette.pos_x-listPlayers[0].pos_x)+23) < (abs(squelette.pos_x-listPlayers[1].pos_x)+43) ):
                        jCible = listPlayers[0];
                    else:
                        jCible = listPlayers[1];
                    if (squelette.pos_x+23 < jCible.pos_x+43):
                        squelette.setDeplacement(6,0);
                    elif (squelette.pos_x+23 > jCible.pos_x+43):
                        squelette.setDeplacement(-6,0);
                else:
                    jCible = listPlayers[0];
                    if (squelette.pos_x+23 < jCible.pos_x+43):
                        squelette.setDeplacement(6,0);
                    elif (squelette.pos_x+23 > jCible.pos_x+43):
                        squelette.setDeplacement(-6,0);
                magic.contactHurting(jCible, squelette)
        magic.applySort(listSorts,listEnnemis[2],height,width,listCombo)


        if(listPlayers[0].isDead()):
            break;
        elif(nbJoueur == 2 and listPlayers[1].isDead()):
            break;


        #display all the element on screen
        util.displayAllImages(window, listBG);
        util.displayAllImages(window, listPlayers);
        for listElem in listSorts:
            util.displayAllImages(window, listElem);
        util.displayAllImages(window, listDecors);
        util.displayAllImages(window, listEnnemis[0]);
        util.displayAllImages(window, listEnnemis[1]);
        util.displayAllImages(window, listEnnemis[2]);
        util.displayAllImages(window, listHUD);
        for Combo in listCombo:
            util.displayAllImages(window, Combo);


        pygame.display.flip();
