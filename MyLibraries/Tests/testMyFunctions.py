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
#===============================================================

if (__name__ == "__main__"):
    CALL_test()
else:
    print("WRONG CALL!")
