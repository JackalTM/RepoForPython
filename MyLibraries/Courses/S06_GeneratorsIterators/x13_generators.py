
"""**************************************************************************************************
Idea behind generatorts 
Next value is calculated
This will save a lot of RAM when many numbers need to be loop throught
"""
class SomeGen:

    def __init__(self, n)->None:
        self.n = n
        self.last = 1
        return None

    def __next__(self)->int:
        return self.Next()

    def Next(self)->int:
        if(self.last >= self.n):
            raise StopIteration()
        else:
            retVal = self.last * 2
            self.last += 1

        return retVal
#====================================================================================================
    
"""**************************************************************************************************
Real builded generator
"""
def MyGenerator(n)->int:
    for i in range(0x00, n, 0x01):
        yield i*2
#====================================================================================================

"""**************************************************************************************************
Main call function
"""
def CALL_Generator():
    instGen = SomeGen(0x0F)

    while(instGen.Next()):
        i = instGen.last
        print("- {}".format(hex(i)))

    print("=====================================")

    #for i in MyGenerator(0x0f):
    #    print(hex(i))
    
    return None
#====================================================================================================

'''*************************************************************************************************************************************
@name       GeneratorsPart1
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def GeneratorsPart1():
    listA = list(range(0x00, 0x04, 0x01))
    listB = list(range(0x00, 0x04, 0x01))

    # Generator jest opeketem króry generuje następny element wegług jakiegos wzoru
    # Generator jest opbeiktem który oszczędza pamięć RAM

    # Generator stworzony z innych list
    genAB = ((a,b) for a in listA for b in listB if a%2==1 and b%2==1)
    for a,b in genAB:
        print("a= ", a, "b= ", b)
    else:
        print(end='\n')

    # Generator całkowiecie stworzony z inych generatorów
    genAB = ((a,b) for a in range(0x00, 0x04, 0x01) for b in range(0x00, 0x04, 0x01) if a%2==1 and b%2==1)
    for a,b in genAB:
        print("a= ", a, "b= ", b)
    else:
        print(end='\n')

    # Aby na nowo wywołać generator należy do od nowa zdefiniować
    # Nie zawiera on polecenia resetowania
    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       GeneratorsPart2
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def GeneratorsPart2():
    # Aby na nowo wywołać generator należy do od nowa zdefiniować
    # Nie zawiera on polecenia resetowania
    genAB = ((a,b) for a in range(0x00, 0x04, 0x01) for b in range(0x00, 0x04, 0x01) if a%2==1 and b%2==1)
    while(1):
        try:
            (a,b) = next(genAB)
            (a,b) = genAB.__next__()

        except StopIteration:
            print("except StopIteration")
            break
        print("a= ", a, "b= ", b)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       GeneratorsPart3
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
#=======================================================================================================================================


if (__name__ == "__main__"):
    GeneratorsPart2()
else:
    pass