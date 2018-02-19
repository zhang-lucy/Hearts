from random import *
class Deck:
    deck=[] #empty deck, to be initialized
    hasCard=[] #list of booleans, indicates if associated card is in deck
    values=["Ace","King","2","3","4","5","6","7","8","9","10","Jack","Queen"]
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

class Hearts:
    Deck 
    def __init__(self):
        pass
    
       
    class Pl: #short for player
        hand=[]
        def __init__(self,Deck):
            for card in pl.hand()
