from random import *
class Deck:
    deck=[] #empty deck, to be initialized
    hasCard=[] #list of booleans, indicates if associated card is in deck
    values=["Ace","King","Queen","Jack","10","9","8","7","6","5","4","3","2"]
    suits=["Spades","Hearts","Diamonds","Clubs"]
    def __init__(self):
        for suit in Deck.suits:
            for value in Deck.values:
                card=value+" of "+suit
                Deck.deck.append(card)

        for x in range(52):
            Deck.hasCard.append(True)
            
    def print(self):
        for x in range(52):
            if Deck.hasCard[x]:
                print(Deck.deck[x])
                
    def in_deck(self,pos):
        return Deck.hasCard[pos]
    
    def draw(self):
        pos=randint(0,51)
        while(not(Deck.in_deck(self,pos))):
              pos=randint(0,51)
        Deck.hasCard[pos]=False
        return Deck.deck[pos]

    def reset(self):
        print("Reshuffling deck")
        for x in range(len(Deck.hasCard)):
            Deck.hasCard[x]=True
            
    def is_empty(self):
        for x in Deck.hasCard:
            if x==True:
                return False
        return True
    
class Pl: #player
    hand=[]
    points=0
    def __init__(self,Deck,name):
        for x in range (13):
            Pl.hand.append(Deck.draw())
        self.name=name
    def getHand(self):
        print(self.name+"'s hand: ")
        for card in Pl.hand:
            print(card)
    def getPoints(self):
        return Pl.points
    def sortHand(self):
        ret=[]
        sample=Deck()
        for card in sample.deck:
            for x in range (13):
                if card==Pl.hand[x]:
                    ret.append(card)
                    Pl.hand[x]=""
        Pl.hand=ret

###########TESTS############
myD=Deck()
#myD.print()
player1=Pl(myD,"Bob")
player1.getHand()
player1.sortHand()
print("------")
player1.getHand()


    
class Hearts: #main game sequence
    Deck
    def __init__(self):
        pass
