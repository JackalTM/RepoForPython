'''*****************************************************************************************
Player class
'''
from card_game_war.card_class import SingleCard

class PlayerHand(SingleCard):
    '''
    @name       __init__
    @brief      Initialization of a Player class object
    @param[in]  playerName
    @note       ...
    @return     None
    '''
    def __init__(self, playerName):
        self.playerName = playerName
        self.__INTERN_handListObj = []
        self.__INTERN_cardsAmount = 0x00
        return None
    #=======================================================================================
    '''*************************************************************************************
    @name       PrintCards  
    @brief      Print all cards in collection
    @param[in]  void 
    @note       Print all cards inside player hand
    @return     void 
    '''
    def PrintCards(self):
        print("----------------------------------------", end='\n')
        print("PLAYER: {} card list:".format(self.playerName), end= '\n')
        for card in self.__INTERN_handListObj:
            try:
                print(card)
            except:
                print("Wrong object!")
    #=======================================================================================
    '''*************************************************************************************
    @name       RemoveCard
    @brief      Return last card on stack
    @param[in]  void 
    @note       Zero when wrong object exist
    @return     Object SingleCard pop from list.
    '''
    def PopLastCard(self):
        if self.__INTERN_cardsAmount > 0x00:
            self.__INTERN_cardsAmount -= 0x01
            return self.__INTERN_handListObj.pop()
        else:
            return 0x00
    #=======================================================================================
    '''*************************************************************************************
    @name       AddCardObj
    @brief      Add card data code in SingleCard object format
    @param[in]  Object of SingleCard class instance
    @note       List in ince aby instance of object SingleCard type
    @return     Boolean value of state of operation.
    '''
    def AddCardObj(self, inSingleCard):
        if type(inSingleCard) == SingleCard:
            self.__INTERN_handListObj.append(inSingleCard)
            self.__INTERN_cardsAmount += 0x01
            return True
        else:
            return False
    #=======================================================================================
    '''*************************************************************************************
    @name       GetCardStr
    @brief      Retun string from class element
    @param[in]  indexCard - Index of a card element class
    @note       str( method __str__ )
    @return     string 
    '''
    def GetCardStr(self, indexCard):
        if (indexCard >= 0x00) and (indexCard < self.__INTERN_cardsAmount):
            return str(self.__INTERN_handListObj[indexCard])
        return "EMPTY"
    #=======================================================================================
    '''*************************************************************************************
    @name       GetCardValue
    @brief      Return value from class element
    @param[in]  indexCard - Index of a card element class
    @note       int( method __int__ )
    @return     int value of a card
    '''
    def GetCardValue(self, indexCard):
        if (indexCard >= 0x00) and (indexCard < self.__INTERN_cardsAmount):
            return int(self.__INTERN_handListObj[indexCard])
        return 0x00
    #=======================================================================================
#===========================================================================================
