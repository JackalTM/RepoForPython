from card_game_war.card_class import *
from card_game_war.deck_class import *
from card_game_war.player_class import *

if (__name__ != "__main__"):
    instDeck = DeckCards(nStacks= 1)
    instPlayer1 = PlayerHand("Player1")
    instPlayer2 = PlayerHand("Player2")
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
    instDeck.PrintListInt()
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
        

