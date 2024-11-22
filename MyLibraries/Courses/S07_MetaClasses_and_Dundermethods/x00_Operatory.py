'''*************************************************************************************************************************************
@name       ...
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       DungeonsAndDragonsCharacter
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
class DungeonsAndDragonsCharacter:
    def __init__(self, name:str, hp:int, armor:int) -> None:
        self.name:str = name
        self.hp:int = hp
        self.armor:int = armor
        self.description:str = ""

    def __str__(self) -> str:
        return "Name-{} | health-{} | armor- {} | desc-{}".format(self.name, self.hp, self.armor, self.description)
    
    @overload
    def __add__(self, hp:int)->object:
        tInt1:int = self.hp + hp
        return DungeonsAndDragonsCharacter(self.name, tInt1, self.armor)
    
    
    def __sub__(self, hp:int)->object:
        tInt1:int = self.hp + hp
        return DungeonsAndDragonsCharacter(self.name, tInt1, self.armor)


def CALL_OperatorForClass()->None:
    instCharacter:DungeonsAndDragonsCharacter = DungeonsAndDragonsCharacter("Dorqen", 120, 30)
    print(instCharacter)
    instCharacter = instCharacter + 15
    print(instCharacter)
    instCharacter = instCharacter + 50
    print(instCharacter)

#=======================================================================================================================================


if (__name__ == "__main__"):
    CALL_OperatorForClass()
else:
    pass