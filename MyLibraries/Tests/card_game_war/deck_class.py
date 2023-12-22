import random

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
    def __init__(self, nStacks):
        self.instRandom = random.Random()

        self.stackListInt = []
        self.stackListObj = []

        n = 0
        while(n < nStacks):
            for i in CardTranslate.CARD_SUIT_STR_FROM_VAL:
                for j in CardTranslate.CARD_RANK_STR_FROM_VAL:
                    self.stackListInt.append( i | j )
            n = n + 1
        self.listLenght = len(self.stackListInt)
        self.index = self.listLenght 

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
        self.instRandom.shuffle(self.stackListInt)
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
        self.stackListObj = []

        for cardInt in self.stackListInt:
            if type(cardInt) == int:
                (rank_value, suit_value, rank_str, suit_str) = CardTranslate.TransleteCard(deck_value= cardInt)
                self.stackListObj.append(SingleCard(rank_value, suit_value, rank_str, suit_str))
            
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
    def GetCardInt(self):
        if self.index > 0x00:
            self.index = self.index - 1
            return self.stackListInt[self.index]
        else:
            return 0x00
    #=======================================================================================
        
    '''*************************************************************************************
    @name       PutCard
    @brief      Return last card on stack
    @param[in]  cardInt - This argument must by of type int
    @note       ...
    @return     ...
    '''
    def PutCardInt(self, cardInt):
        if (self.index < self.listLenght) and (type(cardInt) == int):
            self.stackListInt[self.index] = cardInt
            self.index = self.index + 1
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
    def GetCardObj(self):
        if self.index > 0x00:
            self.index = self.index - 1
            return self.stackListObj[self.index]
        else:
            return 0x00
    #=======================================================================================
        
    '''*************************************************************************************
    @name       PutCardObj
    @brief      Return last card on stack
    @param[in]  CardObj - This arguent must to be of type SingeCard object 
    @note       ...
    @return     ...
    '''
    def PutCardObj(self, CardObj):
        if (self.index < self.nMAX) and (type(CardObj) == SingleCard):
            self.stackListObj[self.index] = CardObj
            self.index = self.index + 1
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
    def PrintListInt(self):
        for card in self.stackListInt:
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
    def PrintListObj(self):
        for card in self.stackListObj:
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
        if self.index > 0x00:
            self.index = self.index - 1
            return self.stackListInt[self.index]
        else:
            raise StopIteration
    #=======================================================================================
        
    '''*************************************************************************************
    @name       __iter__
    @brief      Iterator method
    @param[in]  void
    @note       This method is an iterator for retur card 
    @return     self
    '''
    def GeneratorCardObj(self):
        while(self.index > 0x00):
            self.index = self.index - 1
            yield self.stackListInt[self.index]

    #=======================================================================================
    
#===========================================================================================
