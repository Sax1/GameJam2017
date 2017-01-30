import pygame;
import character;

class Player(Character):
    def __init__(self, pos_x, pos_y, imgPath, hp, speed, numPlayer):
        Object.__init__(self, pos_x, pos_y, imgPath, hp, speed, listSorts)
        self.numPlayer = numPlayer;
        self.jump = false;
        self.sorts = listSorts;

        def setJump(self,state):
            self.jump = state;
        def getStateJump(self):
            return self.jump;
        def setSorts(self, newSorts):
            self.sorts = newSorts;
        def getSorts(self):
            return self.sorts;
