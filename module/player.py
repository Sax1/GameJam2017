import pygame;
import character;

class Player(character.Character):
    def __init__(self, pos_x, pos_y, imgPath, hp, speed, numPlayer, listSorts):
        character.Character.__init__(self, pos_x, pos_y, imgPath, hp, speed)
        self.numPlayer = numPlayer;
        self.sorts = listSorts;


    def setSorts(self, newSorts):
        self.sorts = newSorts;
    def getSorts(self):
        return self.sorts;
