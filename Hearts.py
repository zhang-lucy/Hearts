from random import *
class Deck:
    deck=[] #empty deck, to be initialized
    hasCard=[] #list of booleans, indicates if associated card is in deck
    values=["Ace","King","Queen","Jack","10","9","8","7","6","5","4","3","2"]
    suits=["Hearts","Spades","Diamonds","Clubs"]
    """Deck class: each card has name and index.
        hearts: 0-12
        spades: 13-25
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
        ind=Pl.hand.index(selection) #find where the card is
        print(ind)
        Pl.hand.remove(selection)

    def addPoints(self):
        pass
    """Notes for implementation:
        - Each heart = 1 point - indices 0-12
        - Q of spades = 13 points - index 15 <- double check this value
"""
"""Methods to add:
- Identify who wins round
- Give them all the cards
- Count points in the round
- Add their points to total point count
"""

class Hu(Pl): #human
    def __init__(self,Deck, name):
        Pl.__init__(self,Deck)
        self.name=name
    def pickCard(self): #asks user to play a card
        while True:
            user=input("Play a card (type the number of your selection): ")
            if user.isdigit():
                user=int(user)
                if user<=len(Pl.hand) and user >0:
                    break
                else:
                    print("That value is invalid. Please print a number between 1 and " + str(len(Pl.hand))+".")
            else:
                print("That input is invalid. Please print a number between 1 and " + str(len(Pl.hand))+".")
                
        print(Pl.hand[user-1][0])
        return Pl.hand[user-1] #user-1 because index for tuples vs. UI

class Rb(Pl): #robot
    def __init__(self,Deck,num):
        Pl.__init__(self,Deck)
        self.num=num
    def pickCard(self):
        pass #implement robot thinking process for card selection

"""Notes about robot logic:
- Each robot will have a memory list for all played cards
- Second hand plays low
- Third hand plays high
- Fourth hand plays high if no gain of points (no hearts)
"""

###########TESTS############
myD=Deck()
#myD.print()
player1=Hu(myD,"Bob")
player1.getHand()
player1.sortHand()
print("------")
player1.getHand()
print()
played=player1.pickCard()
player1.playCard(played)
player1.getHand()



    
class Hearts: #main game sequence
    myD=Deck()
    def __init__(self):
        myD=Deck()
        name=input("What's your name? ")
        player=Hu(myD, name)
        rb1=Rb(myD, "rb1")
        rb2=Rb(myD, "rb2")
        rb3=Rb(myD, "rb3")
