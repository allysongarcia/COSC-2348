'''
Project
Author: Allyson Garcia
Date: 05/10/2022
'''
#NOTE: This is the only file needed for the program. Simply run this program
#to start the randomized blackjack games.
import random
from random import randint

#*****CLASSES*****
class Player():
    def __init__(self, number):
        self.__number = number
        self.__bank = randint(500,5000)
        self.__roundsSatOut = 0
        self.__hand = []
        self.__status = 0
    def getNumber(self):
        return self.__number
    #Change the bank after each round
    def setBank(self):
        #2 = blackjack, 1 = winner, 0 or -1 = lost the game
        if (self.__status == 2):
            self.__bank+=2*(self.__bet)
        elif(self.__status == 1):
            self.__bank+=self.__bet
        else:
            self.__bank-=self.__bet
    def getBank(self):
        return self.__bank
    #Set the bet amount for each player, must be at least $25
    def setBet(self):
        if(self.__bank > 500):
          self.__bet = randint(25, 500)
        else:
          self.__bet = randint(25, (self.__bank - 10))
    def getBet(self):
        return self.__bet
    #Double the bet if the player chooses to during a game
    def doubleBet(self):
        self.__bet = self.__bet * 2
    #Set the player's hand of cards
    def setHand(self, tempCard):
        self.__hand.append(tempCard)
    #Print the player's hand of cards
    def getHand(self):
        for card in self.__hand:
          card.print()
    #Used to keep track of the choices a player makes each round
    def setPreviousChoice(self, choice):
        self.__prevChoice = choice
    def getPreviousChoice(self):
        return self.__prevChoice
    #Keep track of how many rounds a player has sat out
    def setRoundsSatOut(self):
        self.__roundsSatOut += 1
    def getRoundsSatOut(self):
        return self.__roundsSatOut
    #Reset the number of rounds sat out after each game
    def reSetRoundsSatOut(self):
        self.__roundsSatOut = 0
    #Check if the player has a blackjack, return the total value of the hand
    def check21(self):
        self.__total=0
        for card in self.__hand:
          self.__total+=card.getValue()
        return self.__total
    def changeStatus(self, num):
        #2 = blackjack, 1 = winner, 0 = still can draw cards, -1 = bust
        self.__status = num
    def getStatus(self):
        return self.__status
    #Clear the hand at the end of each round
    def clearHand(self):
        self.__hand.clear()

class Dealer():
    def __init__(self):
        self.__hand = []
    #Shuffle the cards before starting the games
    def shuffleCards(self, decks):
        random.shuffle(decks)
    #Deal a card to a player
    def dealCards(self, player, shoe):
        tempCard = Card(shoe[0].getColor(), shoe[0].getSuit(), shoe[0].getFace(), shoe[0].getValue())
        shoe.pop(0)
        if(tempCard.getFace() == "A"):
          if(player.check21()+11 > 21):
            tempCard.changeAceValue()
        player.setHand(tempCard)
    #Draw a card for the dealer
    def dealForSelf(self, shoe):
        tempCard = Card(shoe[0].getColor(), shoe[0].getSuit(), shoe[0].getFace(), shoe[0].getValue())
        shoe.pop(0)
        self.__hand.append(tempCard)
    #Check if the dealer has a blackjack
    def check21(self):
        total=0
        for card in self.__hand:
          total+=card.getValue()
        return total
    #Display the face up card
    def displayFaceUpCard(self):
        print("  Color:", self.__hand[1].getColor(), "| Symbol:", self.__hand[1].getSuit(), "| Value:", self.__hand[1].getFace())
    #Display the face down card, used at end of each game
    def displayFaceDownCard(self):
        print("  Color:", self.__hand[0].getColor(), "| Symbol:", self.__hand[0].getSuit(), "| Value:", self.__hand[0].getFace())
    def getHand(self):
        for card in self.__hand:
          card.print()
    def getFaceUpValue(self):
        return self.__hand[1].getValue()
    #Clear hand at end of each game
    def clearHand(self):
        self.__hand.clear()

class Card():
    def __init__(self, color, suit, face, value):
        self.__color = color
        self.__suit = suit
        self.__face = face
        self.__value = value
    def getColor(self):
        return self.__color
    def getSuit(self):
        return self.__suit
    def getFace(self):
        return self.__face
    #Change the value of a recently drawn ace if the player is going to bust
    def changeAceValue(self):
        self.__value = 1
    def getValue(self):
        return self.__value
    #Used to display the cards in the dealer's hand and in each player's hand
    def print(self):
        print("  Color:", self.__color, "| Symbol:",  self.__suit, "| Value:", self.__face)

#*****METHODS*****
def makeDecks():
    #Information for the cards, stored in lists
    suits = ["Spade", "Club", "Heart", "Diamond"]
    faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    #Create 52 cards for the deck
    cards = []
    for suit in suits:
        for i in range(0,13):
          if (suit == "Heart" or suit == "Diamond"):
            cards.append(Card("Red", suit, faces[i], values[i]))
          else:
            cards.append(Card("Black", suit, faces[i],values[i]))
    #Return the deck of cards
    return cards

def decision(dealer, player, shoe, round):
  #Randomly generate player's choice
  if(round != 2):
    choice = random.choice([1,3])
  elif(player.getRoundsSatOut() > 3):
    choice = 1
  elif(player.getBet()*2 > player.getBank()):
    choice = random.choice([1,3])
  else:
    choice = random.choice([1,2,3])
  #Store the player's choice
  player.setPreviousChoice(choice)
  #Perform certain actions depending on player's choice
  if(choice == 1):
    print ("  Player has chosen to hit.")
    dealer.dealCards(player, shoe)
  elif(choice == 2):
    print("  Player has chosen to double.")
    player.doubleBet()
    dealer.dealCards(player,shoe)
  else:
    print("  Player has chosen to stand.")
    player.setRoundsSatOut()

def displayPlayerCards(playerList):
  for player in playerList:
    print("Player",player.getNumber(),":")
    player.getHand()
    print("  Total Value:", player.check21(), " | Bet:", player.getBet(), "USD | In Bank:",player.getBank(), "USD")

#Main Function
def main():
    #Generate number of players at the table
    numPlayers = randint(1,6)
    print("This table has", numPlayers, "player(s).")

    #Create the players and store them in a list
    playerList = []
    for num in range(0,numPlayers):
        playerList.append(Player(num+1))

    #Random number of decks
    numDecks = randint(4,8)
    print("These games will be played with a shoe of cards containing",numDecks,"decks.")

    #Create several decks of cards, stored in a list
    decks = []
    for i in range(0,numDecks):
        decks.append(makeDecks())

    #Create the dealer
    dealer = Dealer()

    #Shuffle each deck of cards
    for num in range(0,numDecks):
        dealer.shuffleCards(decks[num])

    #Create the shoe of cards using the shuffled decks
    shoe = []
    for num in range(0,numDecks):
        shoe += decks[num]

    #Shuffle the entire shoe of cards
    dealer.shuffleCards(shoe)

    #Number of games to be played
    numGames = 10
    print("This table will be playing",numGames,"game(s).")

    #*****Start Games*****
    for game in range(0,numGames):
        print("********** GAME", game+1,"**********")

        #Place bets for each player
        for player in playerList:
          player.setBet()

        #*****Round 1*****
        print("ROUND 1")
        #Deal 1st round of cards
        for player in playerList:
          dealer.dealCards(player, shoe)

        dealer.dealForSelf(shoe)

        #Deal 2nd round of cards
        for player in playerList:
          dealer.dealCards(player,shoe)

        dealer.dealForSelf(shoe)

        #Display card for dealer (only face up card)
        print("Dealer :")
        dealer.displayFaceUpCard()
        print("  Total Value:", dealer.getFaceUpValue())

        #Display cards for players
        displayPlayerCards(playerList)

        #Check if any player has 21
        for player in playerList:
          totalValue = player.check21()
          if (totalValue == 21):
            player.changeStatus(2)
            print("Player", player.getNumber(), "has gotten a blackjack")

        #Check if dealer has 21
        dealerTotalValue=dealer.check21()
        if (dealerTotalValue == 21):
          print("\nDealer has won.")
          dealer.getHand()
          print("  Total Value:", dealer.check21())

        #If dealer doesn't have 21, continue to the next round
        if(dealerTotalValue != 21):
          #*****Round 2*****
          roundCounter = 2
          print("\nROUND", roundCounter)
          #Ask players to hit, double, or stand
          print("Options Available: 1. Hit, 2. Double, 3. Stand")
          for player in playerList:
            if (player.getStatus() == 0):
              print("Current player is Player", player.getNumber())
              decision(dealer, player, shoe, roundCounter)
              #Check each player's total
              if(player.check21() > 21):
                print("  BUST")
                player.changeStatus(-1)
              if(player.check21() == 21):
                print("  Player", player.getNumber(), " has gotten a blackjack.")
                player.changeStatus(2)

          #Check if anyone is able to keep drawing cards
          nextRound = 0
          for player in playerList:
            if(player.getStatus() == 0 and player.getPreviousChoice() != 2):
              nextRound = 1

          #Round 3, 4, ... n : Ask players to hit or stand
          while(nextRound == 1):
            #Print the number of the round
            roundCounter+=1
            print("\nROUND", roundCounter)
            #Print the dealer and player cards
            print("Dealer :")
            dealer.displayFaceUpCard()
            print("  Total Value:", dealer.getFaceUpValue())
            displayPlayerCards(playerList)
            #Ask players to hit or stand
            print("\nOptions Available: 1. Hit, 3. Stand")
            for player in playerList:
              if (player.getStatus() == 0 and player.getPreviousChoice() != 2):
                print("Current player is Player", player.getNumber())
                decision(dealer, player, shoe, roundCounter)
                #Check each player's total
                if(player.check21() > 21):
                  print("  BUST")
                  player.changeStatus(-1)
                if(player.check21() == 21):
                  print("  Player", player.getNumber(), "has gotten a blackjack.")
                  player.changeStatus(2)
            #Check if anyone is able to keep drawing cards
            nextRound = 0
            for player in playerList:
              if(player.getStatus() == 0 and player.getPreviousChoice() == 1):
                nextRound = 1

          #Reveal dealer's face down card
          print("\nDealer is now opening their closed hand:")
          dealer.displayFaceDownCard()

          #Dealer should draw cards until the sum of cards is 17 or higher
          print("\nDealer is drawing cards...")
          while(dealer.check21() < 17):
            dealer.dealForSelf(shoe)

        #Check which players are winners
        if(dealer.check21() > 21):
          print("Dealer has gone over 21. Everyone who is not bust is a winner!")
          for player in playerList:
            if(player.getStatus() == 0):
              player.changeStatus(1)
        else:
          print("Dealer's total is", dealer.check21(), ". Everyone with a higher value is a winner!")
          for player in playerList:
            if(player.check21() > dealer.check21() and player.getStatus()!=-1):
              player.changeStatus(1)

        #Payoff
        for player in playerList:
          player.setBank()

        #Display Final Hands
        print("\nFinal hands:\nDealer:")
        dealer.getHand()
        print("  Total Value:", dealer.check21())
        displayPlayerCards(playerList)

        #Reset each player's status, hand, and # of rounds sat out
        #after each game. Also reset the dealer's hand
        for player in playerList:
          player.changeStatus(0)
          player.clearHand()
          player.reSetRoundsSatOut()
        dealer.clearHand()

        #Determine which players can play next game
        tempList = []
        for player in playerList:
          if(player.getBank() >= 50):
            tempList.append(player)
          else:
            print("\nPlayer", player.getNumber(), "has dropped from the game.")
        playerList = tempList

        #Determine if there are any players left to play the game
        if(len(playerList) == 0):
          print("\nAll players have dropped from the game.")
          break

        #Check if the shoe of cards is running low before the next game
        if(len(shoe) < 25 and game != 9):
          print("Shoe is running out of cards. Creating a new shoe...")
          decks.clear()
          for i in range(0,numDecks):
            decks.append(makeDecks())
          for num in range(0,numDecks):
            dealer.shuffleCards(decks[num])
          shoe.clear()
          for num in range(0,numDecks):
            shoe += decks[num]
          dealer.shuffleCards(shoe)

        print()

#Execute main function
if __name__ == "__main__":
    main()
