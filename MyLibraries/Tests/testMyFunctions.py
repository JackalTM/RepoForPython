from card_game_war.card_class import *
from card_game_war.deck_class import *
from card_game_war.player_class import *

def CALL_test():
    print("Begin od CALL_test()")
    instDeck = DeckCards(nStacks= 1)
    instDeck.TranslatedDeck()
    
    instPlayer1 = PlayerHand("Player1")

    instPlayer1.AddCardObj(instDeck.GetCardObj())
    instPlayer1.AddCardObj(instDeck.GetCardObj())
    instPlayer1.AddCardObj(instDeck.GetCardObj())
    instPlayer1.AddCardObj(instDeck.GetCardObj())

    instPlayer1.PrintCards()    

if (__name__ == "__main__"):
    CALL_test()
else:
    print("WRONG CALL!")
