import random
from Card import Card



def main():
    seenCards = set()
    currentTotal = 0
    decision = input(f"Welcome to Blackjack! Current Total: {currentTotal} Draw a card? y or n ")
    if decision.lower() == 'y':
        print(f"hit! {decision}")
        currCard = doRandomGetNewCard(seenCards)
        currentTotal += currCard.getNumber()
        print(f"You got {currCard.getSuit()} {currCard.getNumber()}")
        print(f"Current Total: {currentTotal}")
    else:
        print("Done!")
        return 0 
    
    while currentTotal <= 21:
        decision = input("hit or stop? y or n ")
        if decision.lower() == 'y':
            print(f"hit! {decision}")
            currCard = doRandomGetNewCard(seenCards)
            currentTotal += currCard.getNumber()
            print(f"You got {currCard.getSuit()} {currCard.getNumber()}")
            print(f"Current Total: {currentTotal}")
        else:
            print(f"Final!: {currentTotal}")
            break
    
    if currentTotal > 21:
        print(f"Over! {currentTotal}")
    
def doRandomGetNewCard(seenCards):
    while True:
        num = random.randint(1,13)
        face = random.randint(1,4)
        if (num, face) not in seenCards:
            newCard = Card(num, suit=face)
            seenCards.add((num, face))
            return newCard
        
        
if __name__ == "__main__":
    main()