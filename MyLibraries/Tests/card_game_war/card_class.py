'''*************************************************************************************************
Class card creation and card translate from code to color and value. 
'''
class CardRankAndSuit:
    '''
    Source dictionary with value to certain string
    This class has not got __init__() method
    Contain only constant dictionary object
    '''
    BIT_MASK_RANK = 0xF0
    BIT_MASK_SUIT = 0x0F

    CARD_RANK_VAL_FROM_STR = {"TWO" : 0x20, "THREE" : 0x30, "FOUR" : 0x40,
                        "FIVE" : 0x50, "SIX" : 0x60, "SEVEN" : 0x70,
                        "EIGHT" : 0x80, "NINE" : 0x90, "TEN" : 0xA0,
                        "JACK" : 0xB0, "QUEEN" : 0xC0, "KING" : 0xD0, "ACE" : 0xE0}
    
    CARD_RANK_STR_FROM_VAL = {0x20 : "TWO", 0x30 : "THREE", 0x40 : "FOUR", 
                        0x50 : "FIVE", 0x60 : "SIX", 0x70 : "SEVEN", 
                        0x80 : "EIGHT", 0x90 : "NINE", 0xA0 : "TEN", 
                        0xB0 : "JACK", 0xC0 : "QUEEN", 0xD0 : "KING", 0xE0 : "ACE"}
    
    CARD_SUIT_VAL_FROM_STR = {"clubs" : 0x04, "diamonds" : 0x03, "hearts" : 0x02, "spades" : 0x01}
    CARD_SUIT_STR_FROM_VAL = {0x04 : "clubs", 0x03 : "diamonds", 0x02 : "hearts", 0x01 : "spades"}
    #================================================================================================
#====================================================================================================

'''**************************************************************************************************
Class card creation and card translate from code to color and value. 
This calss contain only static methods
'''
class CardTranslate(CardRankAndSuit):
    '''***********************************************************************************************
    @name       TransleteCard
    @brief      Class with only static methods
    @param[in]  deck_value - Input coded value of a card 0xAB
    @note       0xAB
                A - Rank value 
                B - Suit value

    @return     (rank_value, suit_value, rank_str, suit_str)
    '''
    @staticmethod
    def TransleteCard(deck_value):

        rank_value = (deck_value & CardRankAndSuit.BIT_MASK_RANK)
        suit_value = (deck_value & CardRankAndSuit.BIT_MASK_SUIT)

        rank_str = CardTranslate.__INTERN_GetRank_str_from_val(rank_value)
        suit_str = CardTranslate.__INTERN_GetSuit_str_from_val(suit_value)

        return (rank_value, suit_value, rank_str, suit_str)
    #================================================================================================
    '''**********************************************************************************************
    @name       __INTERN_GetRank_val_from_str
    @brief      Static method that convert string to int 
    @param[in]  rank_str - Input string rank card
    @note       This metod use dictionary from base staic class
    @return     rank_val - Value of a card rank
    '''
    @staticmethod
    def __INTERN_GetRank_val_from_str(rank_str):
        try:
            rank_val = CardRankAndSuit.CARD_RANK_VAL_FROM_STR[rank_str]
        except:
            rank_val = 0
        finally:
            return rank_val
    #================================================================================================
    '''**********************************************************************************************
    @name       __INTERN_GetRank_str_from_val
    @brief      Static method that convert int to string
    @param[in]  rank_val - Input value of card
    @note       This metod use dictionary from base staic class
    @return     rank_str - String of a rank card
    '''
    @staticmethod
    def __INTERN_GetRank_str_from_val(rank_val):
        try:
            rank_str = CardRankAndSuit.CARD_RANK_STR_FROM_VAL[rank_val]
        except:
            rank_str = "EMPTY"
        finally:
            return rank_str
    #================================================================================================
    '''**********************************************************************************************
    @name       __INTERN_GetSuit_val_from_str
    @brief      ...
    @param[in]  suit_str - Input suit string
    @note       ...
    @return     suit_val - Value of a suit card
    '''
    @staticmethod
    def __INTERN_GetSuit_val_from_str(suit_str):
        try:
            suit_val = CardRankAndSuit.CARD_SUIT_VAL_FROM_STR[suit_str]
        except:
            suit_val = 0
        finally:
            return suit_val
    #================================================================================================
    '''**********************************************************************************************
    @name       __INTERN_GetSuit_str_from_val
    @brief      ...
    @param[in]  suit_val - Input suit value
    @note       ...
    @return     suit_str - String of a suit card
    '''
    @staticmethod
    def __INTERN_GetSuit_str_from_val(suit_val):
        try:
            suit_str = CardRankAndSuit.CARD_SUIT_STR_FROM_VAL[suit_val]
        except:
            suit_str = "EMPTY"
        finally:
            return suit_str
    #================================================================================================
#====================================================================================================

'''**************************************************************************************************
Single card class, deck will be build with this.
'''    
class SingleCard():
    '''
    @name       __init__
    @brief      Initialization for SingleCard object.

    @param[in]  rank_value - Input rank value
    @param[in]  suit_value - Input suit value
    @param[in]  rank_str - Input rank string
    @param[in]  suit_str - Input suit string

    @note       ...
    @return     None
    '''
    def __init__(self, rank_value, suit_value, rank_str, suit_str):

        self.rank_value = rank_value
        self.suit_value = suit_value

        self.rank_str = rank_str
        self.suit_str = suit_str

        return None
    #================================================================================================
    '''**********************************************************************************************
    @name       __str__
    @brief      Class definition for Print()
    @param[in]  void
    @note       ...
    @return     String format for Print() funtion.
    '''
    def __str__(self):
        return "| rank= {} | suit= {} |".format(self.rank_str, self.suit_str)
    #================================================================================================
    '''**********************************************************************************************
    @name       __str__
    @brief      Method definition for int() 
    @param[in]  void
    @note       ...
    @return     Int value for card
    '''
    def __int__(self):
        return self.suit_val + self.rank_val
    #================================================================================================
#====================================================================================================


