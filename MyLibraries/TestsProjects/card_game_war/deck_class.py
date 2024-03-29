from card_game_war.random_only_def import *
from card_game_war.card_class import CardTranslate
from card_game_war.card_class import SingleCard

'''*****************************************************************************************
This class contain two static class. 
They are used to translate card value.
No need to use __int__() from these classes.
'''
class DeckCards(CardTranslate):    
    '''
    @name       __init__
    @brief      Initialize self instance of Random object
    @param[in]  nStacks - Amount of stacks
    @note       ...
    @return     ...
    '''
    def __init__(self, nStacks : int):
        self.instRandom = random.Random()

        self.__INTERN_stackListInt = []
        self.__INTERN_stackListObj = []

        n = 0
        while(n < nStacks):
            for i in CardTranslate.CARD_SUIT_STR_FROM_VAL:
                for j in CardTranslate.CARD_RANK_STR_FROM_VAL:
                    self.__INTERN_stackListInt.append( i | j )
            n = n + 1

        self.listLenght = len(self.__INTERN_stackListInt)
        self.currentLenght = self.listLenght 

        self.deckIsSuffled = False

        return None
    #=======================================================================================
    '''*************************************************************************************
    @name       SuffleDeck
    @brief      Initialize self instance of Random object
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def SuffleDeck(self):
        self.instRandom.shuffle(self.__INTERN_stackListInt)
        self.deckIsSuffled = True
        return None
    #=======================================================================================
    '''*************************************************************************************
    @name       TranslatedDeck
    @brief      Convert card list from int to SingleCard object
    @param[in]  void
    @note       Method shoud be called after SuffleDeck() to create new translated deck.
    @return     None
    '''
    def TranslatedDeck(self):
        self.__INTERN_stackListObj = []

        for cardInt in self.__INTERN_stackListInt:
            if type(cardInt) == int:
                (rank_value, suit_value, rank_str, suit_str) = CardTranslate.TransleteCard(deck_value= cardInt)
                self.__INTERN_stackListObj.append(SingleCard(rank_value, suit_value, rank_str, suit_str))
            
        return None
    #=======================================================================================
    '''*************************************************************************************
    @name       GetCard
    @brief      Return last card on stack
    @param[in]  void 
    @note       index is decremented before read coz initialized index is len()
                Then should be 1 less from start 
    @return     Value of a card 
    '''
    def GetCardInt(self, remove= False) -> bool:
        if self.currentLenght > 0x00:
            if(remove == False):
                self.currentLenght -= 1
                return self.__INTERN_stackListInt[self.currentLenght]
            elif(remove == True):
                self.currentLenght -= 1
                self.__INTERN_stackListObj.pop()
                return self.__INTERN_stackListInt.pop()
            else:
                return 0x00
        else:
            return 0x00
    #=======================================================================================
    '''*************************************************************************************
    @name       PutCardInt
    @brief      Return last card on stack
    @param[in]  cardInt - This argument must by of type int
    @note       ...
    @return     True / False - Depend if Object added 
    '''
    def PutCardInt(self, cardInt : int) -> bool:
        if (self.currentLenght < self.listLenght) and (type(cardInt) == int):
            self.__INTERN_stackListInt[self.currentLenght] = cardInt
            self.currentLenght += 1
            return True
        else:
            return False
    #=======================================================================================
    '''*************************************************************************************
    @name       GetCardObj
    @brief      Return last card on stack
    @param[in]  void 
    @note       index is decremented before read coz initialized index is len()
                Then should be 1 less from start
    @return     Object SingleCard from list
    '''
    def GetCardObj(self, remove : bool= False) :
        if self.currentLenght > 0x00:
            if(remove == False):
                self.currentLenght -= 1
                return self.__INTERN_stackListObj[self.currentLenght]
            elif(remove == True):
                self.currentLenght -= 1
                self.__INTERN_stackListInt.pop()
                return self.__INTERN_stackListObj.pop()
            else:
                return 0x00
        else:
            return 0x00

    #=======================================================================================
    '''*************************************************************************************
    @name       PutCardObj
    @brief      Return last card on stack
    @param[in]  CardObj - This arguent must to be of type SingeCard object 
    @note       ...
    @return     True / False - Depend if Object added 
    '''
    def PutCardObj(self, CardObj : SingleCard):
        if (self.currentLenght < self.nMAX) and (type(CardObj) == SingleCard):
            self.__INTERN_stackListObj[self.currentLenght] = CardObj
            self.indcurrentLenghtex += 1
            return True
        else:
            return False
    #=======================================================================================
    '''*************************************************************************************
    @name       PrintListInt
    @brief      Print list of card in int format.
    @param[in]  void
    @note       ...
    @return     None
    '''
    def PrintListInt(self) ->None:
        print("Card value deck content:", end= '\n')
        for card in self.__INTERN_stackListInt:
            print("- {}".format(hex(card)))
        return None
    #=======================================================================================
    '''*************************************************************************************
    @name       PrintListObj
    @brief      Print list of card in int format.
    @param[in]  void
    @note       ...
    @return     None
    '''
    def PrintListObj(self) -> None:
        print("Card object deck content:", end= '\n')
        for card in self.__INTERN_stackListObj:
            print(card)
        return None
    #=======================================================================================
    '''*************************************************************************************
    @name       __iter__
    @brief      Iterator method
    @param[in]  void
    @note       This method is an iterator for retur card 
    @return     self
    '''
    def __iter__(self):
        return self
    #=======================================================================================
    '''*************************************************************************************
    @name       __next__
    @brief      Next method for generator 
    @param[in]  void
    @note       This method is an iterator for retur c
    @return     Next element for "for" iteration
    '''
    def __next__(self):
        if self.currentLenght > 0x00:
            self.currentLenght -= 1
            return self.__INTERN_stackListInt[self.currentLenght]
        else:
            raise StopIteration
    #=======================================================================================
    '''*************************************************************************************
    @name       GeneratorCardObj
    @brief      Iterator method
    @param[in]  void
    @note       This method is an iterator for retur card 
    @return     yield current object from card list
    '''
    def GeneratorCardObj(self):
        while(self.index > 0x00):
            self.currentLenght -= 1
            yield self.__INTERN_stackListInt[self.index]
    #=======================================================================================
#===========================================================================================
