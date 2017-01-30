import pygame;
import character;

class Player(character.Character):
    def __init__(self, pos_x, pos_y, imgPath, hp, speed, numPlayer, listSorts):
        character.Character.__init__(self, pos_x, pos_y, imgPath, hp, speed)
        self.numPlayer = numPlayer;
        self.jump = 0;
        self.ascend = 0;
        self.landed = 0;
        self.sorts = listSorts;

    def setJump(self,state):
        self.jump = state;
    def getStateJump(self):
        return self.jump;
    def setSorts(self, newSorts):
        self.sorts = newSorts;
    def getSorts(self):
        return self.sorts;
    def getAscend(self):
        return self.ascend;
    def getLanded(self):
        return self.landed;
    def setAscend(self, state):
        self.ascend = state;
    def setLanded(self, state):
        self.landed = state;
    def jump(self):
        self.setLanded(0);
        self.setAscend(1);
