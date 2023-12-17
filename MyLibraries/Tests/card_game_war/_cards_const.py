'''*****************************************************************************************
Class card creation and card translate from code to color and value. 
'''
class CardRankAndSuit:
    '''
    Source dictionary with value to certain string
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
    #=======================================================================================

    '''*************************************************************************************
    @name       __init__
    @brief      Init card const
    @param[in]  ...
    @note       ...
    @return     ...
    '''
    def __init__(self):
        self.created = True
        return None
    #=======================================================================================
#===========================================================================================