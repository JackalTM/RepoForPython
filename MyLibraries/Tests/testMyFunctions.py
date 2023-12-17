#from card_game_war.card_class import *
from card_game_war.deck_class import *

def CALL_test_card():
    instDeckCards = DeckCards(0x01)
    instDeckCards.SuffleDeck()

    while(True):
        cardNum = instDeckCards.GetCard()
        if(cardNum > 0x00):
            print("- {} - left {}".format(hex(cardNum), instDeckCards.index))
        else:
            break

if __name__ == "__main__":
    CALL_test_card()
else:
    print("WRONG CALL!")
