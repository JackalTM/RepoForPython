from card_game_war.card_class import *
from card_game_war.deck_class import *
from card_game_war.player_class import *

'''******************************************************************************
Staic class with game round data 
'''
class GameData:

    TIE_CARDS_AMOUNT = 0x05
    MAX_ROUND_AMOUNT = 0x200

    CMP_COND_CONTINUE = 0x1100
    CMP_COND_PLR_LOST = 0x1111
    CMP_COND_BOTH_LOST = 0x1122

    WAR_COND_CONTINUE = 0x2200
    WAR_COND_PLR_LOST = 0x2211
    WAR_COND_BOTH_LOST = 0x2222

    GAME_CODE_BREAK = 0xFFFF

    roundCounter = 0

    @staticmethod
    def IncCounter():
        GameData.roundCounter += 1

    @staticmethod
    def GetRoundNumber():
        return GameData.roundCounter
    
    @staticmethod
    def __str__():
        return "Current rounst number: {}".format(GameData.roundCounter)
#================================================================================

'''******************************************************************************
If this file is not mmain then intialize object from classes
This is a game object setup
'''
if (__name__ != "__main__"):
    instDeck = DeckCards(nStacks= 1)
    instPlayer1 = PlayerHand("Yasuo")
    instPlayer2 = PlayerHand("Yohn")

    tableCards_pl1 = []
    tableCards_pl2 = []
else:
    print("Work only as include file!")
#================================================================================
    
'''******************************************************************************
Generate game deck and suffle generated cards
Instances with deck and palyer are global
'''
def GameLogic_GenerateDeck(printDeck= False):
    print("Deck is generated:")
    instDeck.SuffleDeck()
    instDeck.TranslatedDeck()

    if printDeck == True:
        instDeck.PrintListInt()
#================================================================================

'''******************************************************************************
Deal card for game players
Card deal untill there is no enought cards left
'''
def GameLogic_DealCard(playersAmount= 2):
    tempStop = int(instDeck.listLenght / playersAmount)
    for i in range(start= 0, stop= tempStop, step= 1):
        instPlayer1.AddCardObj(instDeck.GetCardObj())
        instPlayer2.AddCardObj(instDeck.GetCardObj())
#================================================================================
        
'''******************************************************************************
Players object cards print test
'''
def ShowPlayersCards():
    print(instPlayer1)
    print(instPlayer2)
#================================================================================
    
'''******************************************************************************
Players conditions cheque
Win and lost player is displayed
'''
def GameLogic_DisplayWinPLayer():
    GameData.IncCounter()

    playerOne = instPlayer1.LostCheck()
    playerTwo = instPlayer2.LostCheck()

    if(playerOne == True) and (playerTwo == False):
        print("Player {} won!".format(instPlayer2.playerName))
        return GameData.CMP_COND_PLR_LOST
    
    elif(playerOne == False) and (playerTwo == True):
        print("Player {} won!".format(instPlayer1.playerName))
        return GameData.CMP_COND_PLR_LOST
    
    elif(playerOne == True) and (playerTwo == True):
        print("Player {} won!".format(instPlayer1.playerName))
        return GameData.CMP_COND_BOTH_LOST
    
    else:
        return GameData.CMP_COND_CONTINUE
#================================================================================
        
'''******************************************************************************
Cards on table are reset 
Should be called before war
Table before war need to certain clear
'''
def GameLogic_ClearTableCards():
    # Both lists with cards to win
    # Lists are asigned to empty 
    if(tableCards_pl1 != []):
        tableCards_pl1 = []

    if(tableCards_pl2 != []):
        tableCards_pl2 = []
#================================================================================

'''******************************************************************************
In new round card are put on table from every player
This function is used in to put certain amount of carads on tabale
'''
def GameLogic_PutCardsOnTable_nTimes():
    for i in range(start= 0, stop= GameData.TIE_CARDS_AMOUNT, step= 1):
        tableCards_pl1.append(instPlayer1.DrawLastCardObj(remove= True))
        tableCards_pl2.append(instPlayer2.DrawLastCardObj(remove= True))
#================================================================================

'''******************************************************************************
Game mode are cheque.
Theres is 3 posibolity od game.
Some player took cards or cards are qual then war happen.
On table are put certain amount of cards then won player takes them all.
'''
def GameLogic_CompareCards():
    instCardObjPl1 = instPlayer1.DrawLastCardObj(remove= False)
    instCardObjPl2 = instPlayer2.DrawLastCardObj(remove= False)

    # Certain player takes all cards, from table and also from last compare
    if(int(instCardObjPl1) > int(instCardObjPl2)):
        instPlayer1.AddCardObj(instPlayer2.DrawLastCardObj(remove= True))
        if(tableCards_pl1 != []) and (tableCards_pl2 != []):
            instPlayer1.AddCardObj_nAmount(tableCards_pl1)
            instPlayer1.AddCardObj_nAmount(tableCards_pl2)
        return GameData.CMP_COND_CONTINUE
    
    # Certain player takes all cards, from table and also from last compare
    elif(int(instCardObjPl1) < int(instCardObjPl2)):
        instPlayer2.AddCardObj(instPlayer1.DrawLastCardObj(remove= True))
        if(tableCards_pl1 != []) and (tableCards_pl2 != []):
            instPlayer2.AddCardObj_nAmount(tableCards_pl1)
            instPlayer2.AddCardObj_nAmount(tableCards_pl2)
        return GameData.CMP_COND_CONTINUE

    # Players have equal cards then war conditions is set.
    # In war certain amount of cards must to be put on table.
    # Then won player takes all cards
    else:# War condition
        warConditionsPl1 = instPlayer1.WarPosibilityCheq(GameData.TIE_CARDS_AMOUNT)
        warConditionsPl2 = instPlayer2.WarPosibilityCheq(GameData.TIE_CARDS_AMOUNT)

        if(warConditionsPl1 == True) and (warConditionsPl2 == True):
            return GameData.WAR_COND_CONTINUE

        elif(warConditionsPl1 == True) and (warConditionsPl2 == False):
            return GameData.WAR_COND_PLR_LOST

        elif(warConditionsPl1 == False) and (warConditionsPl2 == True):
            return GameData.WAR_COND_PLR_LOST

        elif(warConditionsPl1 == False) and (warConditionsPl2 == False):
            return GameData.WAR_COND_BOTH_LOST
        
        else:
            return GameData.WAR_COND_BOTH_LOST
#================================================================================