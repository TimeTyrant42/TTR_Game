class Player:
    def __init__(self):
        self.handCards = []
        self.cardIndex = 0;
        self.destinationCards = []

    def makeMove(self, state):
        print("player can not make a decision")

    def getHand(self):
        return self.handCards

    def getCardIndex(self):
        return self.cardIndex

    def getDestCards(self):
        return self.destinationCards
