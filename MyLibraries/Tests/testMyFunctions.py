from card_game_war.game_logic import *

'''*************************************************************
@name       CALL_test  
@brief      Call for testing functon
@param[in]  void 
@note       ...
@return     void 
'''
def CALL_test():
    GameLogic_GenerateDeck()
    GameLogic_DealCard()
    ShowPlayersCards()

    gameState = GameData.CMP_COND_CONTINUE

    # 1. First in while loop game condition is chekq
    while(gameState == GameData.CMP_COND_CONTINUE):
        gameState = GameData.GAME_CODE_BREAK

        # 2. GAme continue conditions
        gameState = GameLogic_DisplayWinPLayer()
        
        # 3. Round number is displayed.
        print(GameData)

        # 4.Start normal round
        # Resoult could be war condition
        warCondition = GameLogic_CompareCards()
        
        # 5. Reinitialize list with drawen cards from players
        # When war occur game stare is set as WAR_CONDITION
        if(warCondition == GameData.WAR_COND_CONTINUE):
            GameLogic_ClearTableCards()

        # 6. If war occures then start war.
        # After each war cards are chequed
        # If the cards are then same war continues
        while(warCondition == GameData.WAR_COND_CONTINUE):
            warCondition = GameData.GAME_CODE_BREAK

            # 6.1 Put hidden cards on table
            GameLogic_PutCardsOnTable_nTimes()

            # 6.2 Cheque again stae of game
            # Resoult could be war again
            warCondition = GameLogic_CompareCards()
            
    # 7. When some player lost card cheq which player won
    GameLogic_DisplayWinPLayer()
#===============================================================

if (__name__ == "__main__"):
    CALL_test()
else:
    print("WRONG CALL!")
