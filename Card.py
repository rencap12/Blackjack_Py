class Card():
    cardSuitMap = {
        1: "Spades",
        2: "Clubs",
        3: "Hearts",
        4: "Diamonds"
    }
    cardNumMap = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 10,
        12: 10,
        13: 10
    }
    def __init__(self, number, suit):
        self.suit = self.cardSuitMap[suit]
        self.number = self.cardNumMap[number]
    
    def getNumber(self):
        return self.number
    
    def getSuit(self):
        return self.suit