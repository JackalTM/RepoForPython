
"""********************************************************************************
Idea behind generatorts 
Next value is calculated
This will safe a lot of RAM
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
#====================================================================================
    
"""**********************************************************************************
Real builded generator
"""
def MyGenerator(n)->int:
    for i in range(0x00, n, 0x01):
        yield i*2
#====================================================================================

def CALL_Generator():
    instGen = SomeGen(0x0F)

    while(instGen.Next()):
        i = instGen.last
        print("- {}".format(hex(i)))

    print("=====================================")

    #for i in MyGenerator(0x0f):
    #    print(hex(i))
    
    return None

if (__name__ == "__main__"):
    CALL_Generator()
else:
    pass