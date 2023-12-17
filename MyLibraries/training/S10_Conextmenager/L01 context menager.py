import time


class TimeMeasure(object):
    """
    Jest to klasa która pełni role kontext menagera
    Należy zdefiniowac metode __enter__ ora __exit__
    """
    def __init__(self):
        pass
        return None

    def __enter__(self):
        '''
        Jest to metoda wywoływana przez with odobnie jak metoda z otwieraniem plików
        '''
        print(">> Time module start.")
        # __start jest to ukryta zmienna instancyjna
        self.__start = time.time()

        return self

    def __exit__(self, a, b, c):
        '''
        Jest to metoda wywoływana przy zamykaniu with
        Wstawiam 3 puste argumenty bez nich nie działa
        '''
        print(">> Time module exit.")
        # __stop jest to ukryta zmienna instancyjna
        self.__stop = time.time()
        self.__timeDelta = self.__stop - self.__start
        print(">> Execution time {}".format(self.__timeDelta))

        return self

class HtmlCM():
    '''
    Klasa jak kontext menager która generuje taxt html
    '''
    def __init__(self):
        pass

        return None

    def __enter__(self):
        print(">> Method __enter__ sterted")
        textLines = ['','','','']
        textLines[0] = '<TABLE>'
        textLines[1] = ' <TR>'
        textLines[2] = '     <TH>Number</TH><TH>Description</TH>'
        textLines[3] = ' </TR>'
        for i in range(0,len(textLines)):
            print(textLines[i])

        print(">> Method __enter__ finished")

        return self

    def __exit__(self, none1, none2, none3):
        print(">> Method __exit__ started")
        textLines = ['']
        textLines[0] = '</TABLE>'
        for i in range(0,len(textLines)):
            print(textLines[i])

        print("Method __exit__ finished")

        return self




def main():
    '''
    Jest to funkcja main gdzie wywoływanie sa wsztkie funkcjie
    '''

    '''
    with TimeMeasure():
        time.sleep(3)
    '''

    # Cwiczenie
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
main()
