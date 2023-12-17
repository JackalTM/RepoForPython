'''
Class for player to menage card
'''
from card_game_war.card_class import SingleCard
class PlayerHand(SingleCard):

    '''*************************************************************************************
    @name       __init__
    @brief      ...

    @param[in]  void

    @note       ...
    @return     None
    '''
    def __init__(self, inCardList= None):
        if type(inCardList) == list:
            self.__INTERN_handList = inCardList
            self.__INTERN_cardsAmount = len(self.handList)
        else:
            self.__INTERN_handList = []
            self.__INTERN_cardsAmount = 0x00
        return None
    #=======================================================================================

    '''*************************************************************************************
    @name       RemoveCard
    @brief      Return last card on stack
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def RemoveCard(self):
        if self.__INTERN_cardsAmount > 0x00:
            self.__INTERN_cardsAmount = self.__INTERN_cardsAmount - 0x01
            return self.__INTERN_handList.pop()
        else:
            return 0x00
    #=======================================================================================
        
    '''*************************************************************************************
    @name       AddCard
    @brief      Return last card on stack
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def AddCard(self, inCard):
        if type(inCard) == SingleCard:
            self.__INTERN_handList.append(inCard)
            self.__INTERN_cardsAmount = self.__INTERN_cardsAmount + 0x01
            return True
        else:
            return False
    #=======================================================================================
#===========================================================================================
