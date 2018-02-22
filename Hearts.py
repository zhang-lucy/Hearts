from random import *
class Deck:
    deck=[] #empty deck, to be initialized
    hasCard=[] #list of booleans, indicates if associated card is in deck
    values=["Ace","King","Queen","Jack","10","9","8","7","6","5","4","3","2"]
    suits=["Spades","Hearts","Diamonds","Clubs"]
    """Deck class: each card has name and index.
        spades: 0-12
        hearts: 13-25
        diamonds: 26-38
        clubs: 39-51
    """
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
        while(not(Deck.in_deck(self,pos))): #loops until selects non-empty card
              pos=randint(0,51)
        Deck.hasCard[pos]=False
        return (Deck.deck[pos],pos) #tuple that identifies index of card

    def reset(self):
        print("Reshuffling deck")
        for x in range(len(Deck.hasCard)):
            Deck.hasCard[x]=True
            
    def is_empty(self):
        for x in Deck.hasCard:
            if x==True:
                return False
        return True
    
class Pl: #player can be human or robot
    hand=[]
    points=0
    def __init__(self,Deck):
        for x in range (13):
            Pl.hand.append(Deck.draw())

    def getHand(self):
        cardNo=1
        print(self.name+"'s hand: ")
        for x in range (len(Pl.hand)):
            if (Pl.hand[x]!=0):
                print(str(cardNo)+": "+Pl.hand[x][0]) 
                cardNo+=1
    def getPoints(self):
        return Pl.points
    def addPoints(self, pts):
        Pl.points=Pl.points+pts
    def sortHand(self):
        ret=[]
        sample=Deck()
        for y in range (len(sample.deck)):
            for x in range (13):
                if sample.deck[y]==Pl.hand[x][0]:
                    ret.append((sample.deck[y],y))
                    Pl.hand[x]=("",0)
        Pl.hand=ret
        return ret
    def getSuit(self, index):
        if index>=0 and index<=12:
            return "spade"
        elif index>=13 and index<=25:
            return "heart"
        elif index>=26 and index<=38:
            return "diamond"
        elif index>=39 and index<=51:
            return "club"
        else:
            return ("ERROR: "+str(index)+" is not valid index in the deck.")
    def pickCard(self):
        pass #to be implemented by human or robot
    def playCard(self, selection): #plays the card chosen in pickCard
        pass

class Hu(Pl): #human
    def __init__(self,Deck, name):
        Pl.__init__(self,Deck)
        self.name=name
    def pickCard(self): #asks user to play a card
        user=int(input("Play a card (type the number of your selection): "))
        return Pl.hand[user-1][0] #user-1 because index for tuples vs. UI

class Rb(Pl): #robot
    def __init__(self,Deck,num):
        Pl.__init__(self,Deck)
        self.num=num
    def pickCard(self):
        pass #implement robot thinking process for card selection


###########TESTS############
myD=Deck()
#myD.print()
player1=Hu(myD,"Bob")
player1.getHand()
player1.sortHand()
print("------")
player1.getHand()
print(player1.getPoints())
player1.addPoints(5)
print(player1.getPoints())
print(player1.pickCard())



    
class Hearts: #main game sequence
    Deck
    def __init__(self):
        pass