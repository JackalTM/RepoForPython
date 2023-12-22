from card_game_war.card_class import *
from card_game_war.deck_class import *
from card_game_war.player_class import *

def CALL_test1():
    instDeck = DeckCards(nStacks= 1)
    #instDeck.SuffleDeck()
    instDeck.TranslatedDeck()
    instDeck.PrintListInt()

def CALL_test2():
    instDeck = DeckCards(nStacks= 1)
    #instDeck.SuffleDeck()
    instDeck.TranslatedDeck()
    instDeck.PrintListObj()


if __name__ == "__main__":
    CALL_test1()
else:
    print("WRONG CALL!")
