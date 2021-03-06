from Card import Card
from DestinationCard import DestinationCard
class Player:
    def __init__(self, name):
        self.handCards = []
        self.cardIndex = 0
        self.destinationCards = []
        self.name = name
        self.points = 0

    def makeMove(self, gameState):
        print("player can not make a decision")

    def getHand(self):
        return self.handCards

    def addCardToHand(self, color):
        self.handCards.append(Card(color))
        self.cardIndex += 1

    def addDestCardToHand(self):
        breaker = 0
        tempCard = DestinationCard.drawDestinationCard()
        while tempCard in self.destinationCards:  # so dup dest cards are not added to hand
            tempCard = DestinationCard.drawDestinationCard()
            breaker += 1
            if breaker > 200:
                break
        self.destinationCards.append(tempCard)

    def getCardIndex(self):
        return self.cardIndex

    def getDestCards(self):
        return self.destinationCards

    def getName(self):
        return self.name
