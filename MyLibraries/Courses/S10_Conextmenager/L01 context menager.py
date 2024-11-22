import time

'''***********************************************************************************
@Brief Klasa stworzona dla "Context menager"
'''
class TimeMeasure(object):
    """
    Jest to klasa która pełni role kontext menagera
    Należy zdefiniowac metode __enter__ ora __exit__
    """
    def __init__(self):
        self.__start = 0.0
        self.__timeDelta = 0.0
        self.__stop = 0.0
        return None
    #-----------------------------------------------------------------------------------

    '''*********************************************************************************
    @brief  Jest to metoda wywoływana przez with odobnie jak metoda z otwieraniem plików
    @note   Jest to wywołane kiedy urzytkownik urzywa "with"
    '''
    def __enter__(self):
        print(">> TimeMeasure: start.")
        self.__start = time.time()
        return self
    #-----------------------------------------------------------------------------------
    
    '''*********************************************************************************
    @brief  Jest to metoda wywoływana przy zamykaniu "with"
            Wstawiam 3 puste argumenty bez nich nie działa
    '''
    def __exit__(self, a, b, c):
        print(">> TimeMeasure: exit.")

        self.__stop = time.time()
        self.__timeDelta = self.__stop - self.__start

        print(">> TimeMeasure: execution time {}".format(self.__timeDelta))
        return self
#========================================================================================
def CALL_TimeMeasure()->None:
    with TimeMeasure() as myTime:
        time.sleep(2)
#========================================================================================

'''***************************************************************************************
@Brief  Klasa jak kontext menager która generuje taxt html
'''
class HtmlCM():

    def __init__(self)->None:
        return None
    #-----------------------------------------------------------------------------------

    '''*********************************************************************************
    @brief  Jest to metoda wywoływana przez "with" odobnie jak metoda z otwieraniem plików
    @note   Jest to wywołane kiedy urzytkownik urzywa "with"
    '''
    def __enter__(self):
        print(">> Method __enter__ sterted")
        textLines = ['','','','']
        textLines[0] = '<TABLE>'
        textLines[1] = ' <TR>'
        textLines[2] = '     <TH>Number</TH><TH>Description</TH>'
        textLines[3] = ' </TR>'
        for i in range(0,len(textLines)):
            print(textLines[i])

        print(">> HtmlCM::__enter__ - finished")

        return self
    #-----------------------------------------------------------------------------------

    '''*********************************************************************************
    @brief  Jest to metoda wywoływana przy zamykaniu "with"
        Wstawiam 3 puste argumenty bez nich nie działa
    '''
    def __exit__(self, in_type:str, in_value:str, in_traceback:str):
        print(">> Method __exit__ started")
        textLines = ['']
        textLines[0] = '</TABLE>'
        for i in range(0,len(textLines)):
            print(textLines[i])

        print(">> HtmlCM::__exit__ - finished")

        return self
    #-----------------------------------------------------------------------------------
#========================================================================================
def CALL_HtmlCM()->None:

    with HtmlCM():
        textLines = ['','','','','','']
        textLines[0] = ' <TR>'
        textLines[1] = '     <TD>1</TD><TD>Say hello!</TD)'
        textLines[2] = ' </TR>'
        textLines[3] = ' <TR>'
        textLines[4] = '     <TD>2</TD><TD>Say good bye!</TD)'
        textLines[5] = ' </TR>'

        for i in range(0,len(textLines)):
            print(textLines[i])

    return None
#========================================================================================


if(__name__== "__main__"):
    CALL_HtmlCM()
else:
    pass
