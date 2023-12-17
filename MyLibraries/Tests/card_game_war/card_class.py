'''*****************************************************************************************
Class card creation and card translate from code to color and value. 
'''
from card_game_war._cards_const import CardRankAndSuit
class CardTranslate(CardRankAndSuit):
    '''
    @name       __init__
    @brief      Initialize self instance of Random object
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def __init__(self):
        self.created = True
        return None
    #=======================================================================================

    '''*************************************************************************************
    @name       __INTERN_GetRank_val_from_str
    @brief      ...
    @param[in]  rank_str - Input string rank card
    @note       ...
    @return     rank_val - Value of a card rank
    '''
    def __INTERN_GetRank_val_from_str(self, rank_str):
        try:
            rank_val = CardRankAndSuit.CARD_RANK_VAL_FROM_STR[rank_str]
        except:
            rank_val = 0
        finally:
            return rank_val
    #=======================================================================================
        
    '''*************************************************************************************
    @name       __INTERN_GetRank_str_from_val
    @brief      ...
    @param[in]  rank_val - Input value of card
    @note       ...
    @return     rank_str - String of a rank card
    '''
    def __INTERN_GetRank_str_from_val(self, rank_val):
        try:
            rank_str = CardRankAndSuit.CARD_RANK_STR_FROM_VAL[rank_val]
        except:
            rank_str = "EMPTY"
        finally:
            return rank_str
    #=======================================================================================
        
    '''*************************************************************************************
    @name       __INTERN_GetSuit_val_from_str
    @brief      ...
    @param[in]  suit_str - Input suit string
    @note       ...
    @return     suit_val - Value of a suit card
    '''
    def __INTERN_GetSuit_val_from_str(self, suit_str):
        try:
            suit_val = CardRankAndSuit.CARD_SUIT_VAL_FROM_STR[suit_str]
        except:
            suit_val = 0
        finally:
            return suit_val
    #=======================================================================================
        
    '''*************************************************************************************
    @name       __INTERN_GetSuit_str_from_val
    @brief      ...
    @param[in]  suit_val - Input suit value
    @note       ...
    @return     suit_str - String of a suit card
    '''
    def __INTERN_GetSuit_str_from_val(self, suit_val):
        try:
            suit_str = CardRankAndSuit.CARD_SUIT_STR_FROM_VAL[suit_val]
        except:
            suit_str = "EMPTY"
        finally:
            return suit_str
    #=======================================================================================
        
    '''*************************************************************************************
    @name       TransleteCard
    @brief      ...
    @param[in]  deck_value - Input coded value of a card 0xAB
    @note       0xAB
                A - Rank value 
                B - Suit value

    @return     (rank_value, suit_value, rank_str, suit_str)
    '''
    def TransleteCard(self, deck_value):

        rank_value = (deck_value & self.BIT_MASK_RANK)
        suit_value = (deck_value & self.BIT_MASK_SUIT)

        rank_str = self.__INTERN_GetRank_str_from_val(rank_value)
        suit_str = self.__INTERN_GetSuit_str_from_val(suit_value)

        return (rank_value, suit_value, rank_str, suit_str)
    #=======================================================================================
#===========================================================================================

'''*****************************************************************************************
Single card class, deck will be build with this.
'''    
class SingleCard():
    '''
    @name       __init__
    @brief      ...

    @param[in]  rank_value - Input rank value
    @param[in]  suit_value - Input suit value
    @param[in]  rank_str - Input rank string
    @param[in]  suit_str - Input suit string

    @note       ...
    @return     ...
    '''
    def __init__(self, rank_value, suit_value, rank_str, suit_str):

        self.rank_value = rank_value
        self.suit_value = suit_value

        self.rank_str = rank_str
        self.suit_str = suit_str

        return None
    #=======================================================================================

    '''*************************************************************************************
    @name       __str__
    @brief      ...
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def __str__(self):
        return "< {} >< {} <".format(self.rank_str, self.suit_str)
    #=======================================================================================

    '''*************************************************************************************
    @name       __str__
    @brief      ...
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def __int__(self):
        return self.suit_val + self.rank_val
    #=======================================================================================
#===========================================================================================


