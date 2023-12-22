'''*****************************************************************************************
Player class
'''
from card_game_war.card_class import SingleCard

class PlayerHand(SingleCard):

    '''*************************************************************************************
    @name       __init__
    @brief      Initialization of a Player class object
    @param[in]  playerName
    @note       ...
    @return     None
    '''
    def __init__(self, playerName):
        self.playerName = playerName
        self.__INTERN_handListObj = []
        self.__INTERN_handListInt = []
        self.__INTERN_cardsAmount = 0x00
        return None
    #=======================================================================================

    '''*************************************************************************************
    @name       PrintCards  
    @brief      Print all cards in collection
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def PrintCards(self):
        for card in self.__INTERN_handList:
            try:
                print(card)
            except:
                print("Wrong object!")

    #=======================================================================================

    '''*************************************************************************************
    @name       RemoveCard
    @brief      Return last card on stack
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def RemoveLastCard(self):
        if self.__INTERN_cardsAmount > 0x00:
            self.__INTERN_cardsAmount = self.__INTERN_cardsAmount - 0x01
            return self.__INTERN_handList.pop()
        else:
            return 0x00
    #=======================================================================================
        
    '''*************************************************************************************
    @name       AddCardInt
    @brief      Add card data code in int format
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def AddCardInt(self, singleCardInt):
        if type(singleCardInt) == int:
            self.__INTERN_handListInt.append(singleCardInt)
            self.__INTERN_cardsAmount = self.__INTERN_cardsAmount + 0x01
            return True
        else:
            return False
    #=======================================================================================
        
    '''*************************************************************************************
    @name       AddCardObj
    @brief      Add card data code in SingleCard object format
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def AddCardObj(self, singleCardObj):
        if type(singleCardObj) == SingleCard:
            self.__INTERN_handListObj.append(singleCardObj)
            self.__INTERN_cardsAmount = self.__INTERN_cardsAmount + 0x01
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
        if type(indexCard) == int:
            if indexCard < self.__INTERN_cardsAmount:
                return str(self.__INTERN_handList[indexCard])
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
        if type(indexCard) == int:
            if indexCard < self.__INTERN_cardsAmount:
                return int(self.__INTERN_handList[indexCard])
        return 0x00
    #=======================================================================================
#===========================================================================================
