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
    pointCards=[] #hearts/Q of spades
    def __init__(self,Deck, seat):
        for x in range (13):
            Pl.hand.append(Deck.draw())
        self.seat=seat
    def getSeat(self):
        if self.seat==1:
            return "South"
        elif self.seat==2:
            return "West"
        elif self.seat==3:
            return "North"
        elif self.seat==4:
            return "East"
        else:
            return("ERROR: Seat number not properly entered.")
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
    def addPointCards(self,cards): #adds point cards to pointCards inventory
        for card in cards:
            Pl.pointCards.append(card)
    def displayPointCards(self):
        for card in Pl.pointCards:
            print(card[0])
    def getPointCards(self):
        return Pl.pointCards
    #def addPoints(self):
#        pass
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
    def __init__(self,Deck, seat, name):
        Pl.__init__(self,Deck,seat)
        self.name=name
    def getHand(self):
        cardNo=1
        print(self.name+"'s hand: ")
        for x in range (len(Pl.hand)):
            if (Pl.hand[x]!=0):
                print(str(cardNo)+": "+Pl.hand[x][0]) 
                cardNo+=1
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
    def __init__(self,Deck,seat, num):
        Pl.__init__(self,Deck,seat)
        self.num=num
    def getHand(self):
        cardNo=1
        print("Robot " + str(self.num) +"'s hand: ")
        for x in range (len(Pl.hand)):
            if (Pl.hand[x]!=0):
                print(str(cardNo)+": "+Pl.hand[x][0])
                cardNo+=1
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
player1=Hu(myD,1,"Bob")
print(player1.getSeat())
#player1.getHand()
player1.sortHand()
#print("------")
player1.getHand()
#print()
#played=player1.pickCard()
#player1.playCard(played)
#player1.getHand()
player1.addPointCards([("Ace of Hearts", 0)])
print(player1.getPointCards())
player1.addPoints(1)
print(player1.getPoints())

##########ROBOT-TESTS#####
rb1=Rb(myD, 2, 1)
print("Seat: " + rb1.getSeat())
rb1.getHand()
#rb1.sortHand()
#rb1.getHand()
    
class Hearts: #main game sequence
    myD=Deck()
    round_no=1 #determines which way to pass cards
    def __init__(self):
        myD=Deck()
        name=input("What's your name? ")
        player=Hu(myD, name)
        rb1=Rb(myD, 1)
        rb2=Rb(myD, 2)
        rb3=Rb(myD, 3)
    def direction(self):
        pass
        
