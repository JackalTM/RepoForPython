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
    @name       PrintAllCards  
    @brief      Print all cards in collection
    @param[in]  void 
    @note       Print all cards inside player hand
    @return     void 
    '''
    def PrintAllCards(self):
        print("----------------------------------------", end='\n')
        print("PLAYER: {} card list:".format(self.playerName), end= '\n')
        for card in self.__INTERN_handListObj:
            try:
                print(card)
            except:
                print("Wrong object!")
        print("----------------------------------------", end='\n')
    #=======================================================================================
    '''*************************************************************************************
    @name       __str__
    @brief      Method for print() function
    @param[in]  void
    @note       Return specyfin string format for print funtion
    @return     str
    '''
    def __str__(self):
        return "PLAYER: {} has {} amount of cards".format(self.playerName, self.__INTERN_cardsAmount)
    #=======================================================================================
    '''*************************************************************************************
    @name       DrawLastCardObj
    @brief      Return last card on stack
    @param[in]  remove - Drawn cards should be removed or not
    @note       Zero when wrong object exist
    @return     Object SingleCard pop from list.
    '''
    def DrawFirstCardObj(self, remove= True):
        if (self.__INTERN_cardsAmount > 0x00):
            if(remove == True):
                self.__INTERN_cardsAmount -= 0x01
                return self.__INTERN_handListObj.pop(0)
            else:
                return self.__INTERN_handListObj[0]
        else:
            return 0x00
    #=======================================================================================
    '''*************************************************************************************
    @name       DrawLastCardObj
    @brief      Return last card on stack
    @param[in]  remove - Drawn cards should be removed or not
    @note       Zero when wrong object exist
    @return     Object SingleCard pop from list.
    '''
    def DrawLastCardObj(self, remove= True):
        if (self.__INTERN_cardsAmount > 0x00):
            if(remove == True):
                self.__INTERN_cardsAmount -= 0x01
                return self.__INTERN_handListObj.pop(-1)
            else:
                return self.__INTERN_handListObj[-1]
        else:
            return 0x00
    #=======================================================================================
    '''*************************************************************************************
    @name       DrawLastCardObj_nAmount
    @brief      Certain amount of cards are draw from main list 
    @param[in]  nAmount - Int amount of cards
    @param[in]  remove - Drawn cards should be removed or not
    @note       This method use self.DrawLastCardObj()
    @return     List that contain cards from player hand
    '''
    def DrawLastCardObj_nAmount(self, nAmount, remove=True):
        retList = []
        if(nAmount <= self.__INTERN_cardsAmount) and (nAmount > 0):
            for i in range(start= 0, stop= nAmount, step= 1):
                retList.append(self.DrawLastCardObj(remove))

        return retList
    #=======================================================================================

    '''*************************************************************************************
    @name       AddCardObj
    @brief      Add card data code in SingleCard object format
    @param[in]  Object of SingleCard class instance
    @note       List in ince aby instance of object SingleCard type
    @return     Boolean value of state of operation.
    '''
    def AddCardObjBack(self, inSingleCard):
        if type(inSingleCard) == SingleCard:
            self.__INTERN_handListObj.append(inSingleCard)
            self.__INTERN_cardsAmount += 0x01
            return True
        else:
            return False
    #=======================================================================================
    '''*************************************************************************************
    @name       AddCardObj_nAmount
    @brief      Add certain amout of card object 
    @param[in]  Object list of SingleCard class instance
    @note       This method is using  add single card method
    @return     Boolean value of state of operation.
    '''
    def AddCardObj_nAmount(self, CardObjList):
        if type(CardObjList) == list:
            for singleCardObject in CardObjList:
                self.AddCardObj(singleCardObject)
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
    def GetCardStr(self, indexCard= 0):
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
    def GetCardValue(self, indexCard= 0):
        if (indexCard >= 0x00) and (indexCard < self.__INTERN_cardsAmount):
            return int(self.__INTERN_handListObj[indexCard])
        else:
            return 0x00
    #=======================================================================================
    '''*************************************************************************************
    @name       WarPosibilityCheq
    @brief      Posibility to card war condition
    @param[in]  warAmount - war cards amount 
    @note       Player should have some cards amout to war attempt
    @return     bool - State of war attempt posibility
    '''
    def WarPosibilityCheq(self, warAmount= 5):
        if(warAmount < self.__INTERN_cardsAmount):
            return True
        else:
            return False
    #=======================================================================================
    '''*************************************************************************************
    @name       LostCheck
    @brief      Return state if player already lost 
    @param[in]  void 
    @note       If player lost then return true 
    @return     bool
    '''
    def LostCheck(self):
        if(self.__INTERN_cardsAmount <= 0x00):
            return True
        else:
            return False
    #=======================================================================================
#===========================================================================================
