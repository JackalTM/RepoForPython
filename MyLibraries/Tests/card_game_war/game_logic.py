from card_game_war.card_class import *
from card_game_war.deck_class import *
from card_game_war.player_class import *

if (__name__ != "__main__"):
    instDeck = DeckCards(nStacks= 1)
    instPlayer1 = PlayerHand("Yasuo")
    instPlayer2 = PlayerHand("Yohn")
else:
    print("Work only as include file!")

'''******************************************************************************
Generate game deck and suffle generated cards
Instances with deck and palyer are global
'''
def GameLogic_GenerateDeck():
    print("Deck is generated:")
    instDeck.SuffleDeck()
    instDeck.TranslatedDeck()
    #instDeck.PrintListInt()
#================================================================================

'''******************************************************************************
Deal card for game players
Card deal untill teres is no equal card left
'''
def GameLogic_DealCard(playersAmount= 2):
    tempStop = int(instDeck.listLenght / playersAmount)
    for i in range(0, tempStop, 1):
        instPlayer1.AddCardObj(instDeck.GetCardObj())
        instPlayer2.AddCardObj(instDeck.GetCardObj())
#================================================================================
        
'''******************************************************************************
Show players cards object content 
'''
def ShowPlayersCards():
    instPlayer1.PrintAllCards()
    instSingleCard = instPlayer1.DrawLastCardObj(remove= True)
    print("Card from {} is {}".format(instPlayer1.playerName, instSingleCard))
    instSingleCard = instPlayer1.DrawLastCardObj(remove= True)
    print("Card from {} is {}".format(instPlayer1.playerName, instSingleCard))
    instPlayer1.PrintAllCards()


'''******************************************************************************
Function return state of game.
When some player lost then return false
'''
def ContinueGame():
    if (instPlayer1.LostCheck() == False) and (instPlayer2.LostCheck() == False):
        return True
    else:
        return False
    
        
'''******************************************************************************
war condition
When players have war 
'''
def PlayersWar():
    pass
