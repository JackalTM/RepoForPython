import random

'''*****************************************************************************************
Class with cards content 
'''
from card_game_war._cards_const import CardRankAndSuit
class DeckCards(CardRankAndSuit):    
    '''
    @name       __init__
    @brief      Initialize self instance of Random object
    @param[in]  nStacks - Amount of stacks
    @note       ...
    @return     ...
    '''
    def __init__(self, nStacks):
        self.instRandom = random.Random()
        self.stackList = []
        n = 0
        while(n < nStacks):
            for i in CardRankAndSuit.CARD_SUIT_STR_FROM_VAL:
                for j in CardRankAndSuit.CARD_RANK_STR_FROM_VAL:
                    self.stackList.append(i | j)
            n = n + 1
        self.nMAX = len(self.stackList)
        self.index = self.nMAX 

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
        self.instRandom.shuffle(self.stackList)
        return None
    #=======================================================================================

    '''*************************************************************************************
    @name       GetCard
    @brief      Return last card on stack
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def GetCard(self):
        if self.index > 0x00:
            self.index = self.index - 1
            return self.stackList[self.index]
        else:
            return 0x00
    #=======================================================================================
        
    '''*************************************************************************************
    @name       PutCard
    @brief      Return last card on stack
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def PutCard(self, inCard):
        if self.index < self.nMAX:
            self.stackList[self.index] = inCard
            self.index = self.index + 1
            return True
        else:
            return False
    #=======================================================================================
#===========================================================================================
