'''*************************************************************************************************************************************
@name       ...
@brief      ...
@note       ...
'''
from typing import Any

class MemoryClass:
    def __init__(self, inList:list) -> None:
        self.thisList = inList
        return None
    
    # Wywołanie instancji jako instMemoryClass(item) doda item do listy
    def __call__(self, inItem:Any) -> None:
        self.thisList.append(inItem)
        return None
    
    def __str__(self) -> str:
        tStr = ""
        for i in self.thisList:
            tStr = "{}, {}".format(tStr, str(i))
        return tStr
#=======================================================================================================================================

def Call_MemoryClass1()->None:
    myMemory = MemoryClass([1,2,3,4])
    myMemory(5)
    myMemory(6)

    print(str(myMemory))
    return None

#=======================================================================================================================================
if (__name__ == "__main__"):
    Call_MemoryClass1()
else:
    pass
#=======================================================================================================================================