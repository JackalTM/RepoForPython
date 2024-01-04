from card_game_war.card_class import *
from card_game_war.deck_class import *
from card_game_war.player_class import *

'''******************************************************************************
Staic class with game round data 
'''
class GameData:

    PLR_AMOUNT = 0x02

    TIE_CARDS_AMOUNT = 0x03
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
    def ResetCounter():
        GameData.roundCounter = 0

    @staticmethod
    def IncCounter():
        GameData.roundCounter += 1

    @staticmethod
    def GetRoundNumber():
        return GameData.roundCounter
    
    @staticmethod
    def PrintGamedata():
        print("Round number: {}".format(GameData.roundCounter))
    
    @staticmethod
    def __str__():
        print("Round number: {}".format(GameData.roundCounter))
#================================================================================

'''******************************************************************************
If this file is not mmain then intialize object from classes
This is a game object setup
'''
if (__name__ != "__main__"):
    instDeck = DeckCards(nStacks= 1)
    instPlayer1 = PlayerHand("Yasuo")
    instPlayer2 = PlayerHand("Yohnn")

    instlistTableCardsPlr1 = []
    instlistTableCardsPlr2 = []
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
        instDeck.PrintListObj()
#================================================================================

'''******************************************************************************
Deal cards for game players
Card deal untill there is no enought cards left
'''
def GameLogic_DealCard():
    tempStop = int(instDeck.listLenght / GameData.PLR_AMOUNT)
    tempStop = tempStop - 20
    for i in range(0, tempStop, 1):
        instPlayer1.AddCardObjBack(instDeck.GetCardObj())
        instPlayer2.AddCardObjBack(instDeck.GetCardObj())
#================================================================================
        
'''******************************************************************************
Players have own __str__() method for print().
Overview method
'''
def GameLogic_PrintPlayersContent():
    print("Players content: ", end= '\n')
    print(instPlayer1)
    print(instPlayer2)
#================================================================================
    
'''******************************************************************************
Players conditions cheque
Win and lost player is displayed
'''
def GameLogic_ChequeLostPlayer(debugPrint= False):
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
    if instlistTableCardsPlr1 != []:
        instlistTableCardsPlr1 = []

    if instlistTableCardsPlr2 != []:
        instlistTableCardsPlr2 = []
#================================================================================

'''******************************************************************************
In new round card are put on table from every player
This function is used in to put certain amount of carads on tabale
'''
def GameLogic_PutCardsOnTable_nTimes():
    print("Amount of cards are put on table")
    for i in range(start= 0, stop= GameData.TIE_CARDS_AMOUNT, step= 1):
        instlistTableCardsPlr1.append(instPlayer1.DrawFirstCardObj(remove= True))
        instlistTableCardsPlr2.append(instPlayer2.DrawFirstCardObj(remove= True))
#================================================================================

'''******************************************************************************
Game mode are cheque.
Theres is 3 posibolity od game.
Some player took cards or cards are qual then war happen.
On table are put certain amount of cards then won player takes them all.
'''
def GameLogic_CompareCards(debugPrint= False):
    instCardObjPl1 = instPlayer1.DrawFirstCardObj(remove= True)
    instCardObjPl2 = instPlayer2.DrawFirstCardObj(remove= True)

    print("Plr1: {} vs Plr2: {}".format(instCardObjPl1, instCardObjPl2), end= '\t')

    # Certain player takes all cards, from table and also from last compare
    if(int(instCardObjPl1) > int(instCardObjPl2)):
        print("Won: Plr1", end= '\n')
        instPlayer1.AddCardObjBack(instCardObjPl1)
        instPlayer1.AddCardObjBack(instCardObjPl2)
        if(instlistTableCardsPlr1 != []) and (instlistTableCardsPlr2 != []):
            print("List is append {} and {}".format(instlistTableCardsPlr1, instlistTableCardsPlr2))
            instPlayer1.AddCardObj_nAmount(instlistTableCardsPlr1)
            instPlayer1.AddCardObj_nAmount(instlistTableCardsPlr2)
        return GameData.CMP_COND_CONTINUE
    
    # Certain player takes all cards, from table and also from last compare
    elif(int(instCardObjPl1) < int(instCardObjPl2)):
        print("Won: Plr2", end= '\n')
        instPlayer2.AddCardObjBack(instCardObjPl2)
        instPlayer2.AddCardObjBack(instCardObjPl1)
        if(instlistTableCardsPlr1 != []) and (instlistTableCardsPlr2 != []):
            print("List is append {} and {}".format(instlistTableCardsPlr2, instlistTableCardsPlr2))
            instPlayer2.AddCardObj_nAmount(instlistTableCardsPlr2)
            instPlayer2.AddCardObj_nAmount(instlistTableCardsPlr1)
        return GameData.CMP_COND_CONTINUE

    # Players have equal cards then war conditions is set.
    # In war certain amount of cards must to be put on table.
    # Then won player takes all cards
    else:# War condition
        print("War condition", end= '\n')
        return GameData.WAR_COND_CONTINUE
#================================================================================
        
'''******************************************************************************
Game mode are cheque.
Theres is 3 posibolity od game.
Some player took cards or cards are qual then war happen.
On table are put certain amount of cards then won player takes them all.
'''
def GameLogic_WarPosibility(debugPrint= False):
    # Players have equal cards then war conditions is set.
    # In war certain amount of cards must to be put on table.
    # Then won player takes all cards
    # War condition
    print("War condition", end= '\t')
    warConditionsPl1 = instPlayer1.WarPosibilityCheq(GameData.TIE_CARDS_AMOUNT)
    warConditionsPl2 = instPlayer2.WarPosibilityCheq(GameData.TIE_CARDS_AMOUNT)

    if(warConditionsPl1 == True) and (warConditionsPl2 == True):
        print("war posible")
        return GameData.WAR_COND_CONTINUE

    elif(warConditionsPl1 == True) and (warConditionsPl2 == False):
        print("Plr2 lost")
        return GameData.WAR_COND_PLR_LOST

    elif(warConditionsPl1 == False) and (warConditionsPl2 == True):
        print("Plr1 lost")
        return GameData.WAR_COND_PLR_LOST

    elif(warConditionsPl1 == False) and (warConditionsPl2 == False):
        print("Both players lost")
        return GameData.WAR_COND_BOTH_LOST
    
    else:
        return GameData.WAR_COND_BOTH_LOST
#================================================================================