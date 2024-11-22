'''*************************************************************************************************************************************
@name       Call_Function_return1
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def CALL_Test1()->None:

    def ReadFile(line : int)->str:
        return "Line number {}".format(line)

    def OpenFile(MyFileOperation : ReadFile):
        def _Internal(*args, **kwargs):
            print("File is opened:")
            status = MyFileOperation(*args, **kwargs)
            print("File is closed:")
            return status
        return _Internal

    NewReadFile = OpenFile(ReadFile)
    print(NewReadFile(5))
    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_Function_return1
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def Call_Function_return1()->None:

    def AddNums(numA:int, numB:int)->int:
        return numA + numB
    
    def SubNums(numA:int, numB:int)->int:
        return numA - numB
    
    def MulNums(numA:int, numB:int)->int:
        return numA * numB

    def Calculate(Funct:object, *args)->int:
        res = 0
        for i in args:
            if(type(i) == int):
                res = Funct(res, i)
            else:
                pass

        return res
    
    listFinctions = (AddNums, SubNums, MulNums)
    listArgs = (1,2,3,4,5,6,7,8,9)

    for f in listFinctions:
        res = Calculate(f, *listArgs)
        print("res = ", res)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_Function_return2
@brief      Creating function depend on functionality
@param[in]  ...
@note       Usefull depend whn some function need to done many times
@return     ...
'''
def Call_Function_return2()->None:

    def CreateFunction(kind:str)->object:
        startVal0 = ('+', '-')
        startVal1 = ('*', '/')

#************************************************
# Genaration function if else statment
        if(kind in startVal0):
            surceStrFunction = '''
def Function(*args):
    res = 0
    for i in args:
        res = res {} i
    return res
'''.format(kind)
        elif(kind in startVal1):
            surceStrFunction = '''
def Function(*args):
    res = 1
    for i in args:
        res = res {} i
    return res
'''.format(kind)
        else:
            surceStrFunction = '''
def Function(*args):
    res = 0
    for i in args:
        res = res {} i
    return res
'''.format(kind)

        exec(surceStrFunction, globals())
        return Function
#====================================================
        
    MyFunction1 = CreateFunction('+')
    MyFunction2 = CreateFunction("-")
    MyFunction3 = CreateFunction("*")
    listArgs = (1,2,3,4,5,6,7,8,9)

    print("Function add: ")
    res = MyFunction1(*listArgs)
    print("res= ", res)

    print("Function sub: ")
    res = MyFunction2(*listArgs)
    print("res= ", res)

    print("Function mull: ")
    res = MyFunction3(*listArgs)
    print("res= ", res)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_WrappersFunctions
@brief      Creating function that wrap input function by some other functionality
@param[in]  ...
@note       ...
@return     ...
'''
def Call_WrappersFunctions1()->None:

    def ChangeSalary1(employName:str, newSalary:float, asBonus:bool)->float:
        print("ChangeSalary: ",end='\n')
        print("Emplout name: ", employName, "; New salary: ", newSalary, end='\n')
        return newSalary
    
    def CreateFunWithWrapper(SomeFunction:object)->object:
        def FunWithWrapper(*args, **kwargs)->object:
            print("--"*0x10, end= '\n')

            print("Function name: ", SomeFunction.__name__, end= '\n')

            print("*args: ", end= '\t')
            for i in args:
                print(i, end= ', ')
            else:
                print(end= '\n')

            print("**kwargs: ", end= '\t')
            for i in kwargs:
                print("key: ", i, "arg: ", kwargs[i], end= ', ')
            else:
                print(end= '\n')

            ResFunction = SomeFunction(*args, **kwargs)
            print("=="*0x10, end='\n')
            return ResFunction
        return FunWithWrapper

    NewFunction = CreateFunWithWrapper(ChangeSalary1)
    NewFunction("Jack O lantern", 9.99, True)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_WrappersFunctions
@brief      Creating function that wrap input function by some other functionality
@param[in]  ...
@note       ...
@return     ...
'''
def Call_WrappersFunctions2()->None:
    #import functools
    
    def CreateFunWithWrapper(SomeFunction:object)->object:
        def FunWithWrapper(*args, **kwargs)->object:
            print("--"*0x10, end= '\n')

            print("Function name: ", SomeFunction.__name__, end= '\n')

            print("*args: ", end= '\t')
            for i in args:
                print(i, end= ', ')
            else:
                print(end= '\n')

            print("**kwargs: ", end= '\t')
            for i in kwargs:
                print("key: ", i, "arg: ", kwargs[i], end= ', ')
            else:
                print(end= '\n')

            ResFunction = SomeFunction(*args, **kwargs)

            print("=="*0x10, end='\n')
            return ResFunction
        return FunWithWrapper
    
    @CreateFunWithWrapper
    def ChangeSalary1(employName:str, newSalary:float, asBonus:bool)->float:
        print("ChangeSalary: ",end='\n')
        print("Emplout name: ", employName, "; New salary: ", newSalary, end='\n')
        return newSalary
    
    ChangeSalary1("Jack O Lantern Panik", 9.99, True)


    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_WrapperFunWithParameter1
@brief      Wraper functionality wih parameter
@param[in]  ...
@note       ...
@return     ...
'''
def Call_WrapperFunWithParameter1()->None:

    def CreateFunWithWrapper(SomeFunction:object)->object:
        def FunWithWrapper(*args, **kwargs)->object:
            print("--"*0x10, end= '\n')

            print("Function name: ", SomeFunction.__name__, end= '\n')
            print("*args: ", end= '\t')
            for i in args:
                print(i, end= ', ')
            else:
                print(end= '\n')

            print("**kwargs: ", end= '\t')
            for i in kwargs:
                print("key: ", i, "arg: ", kwargs[i], end= ', ')
            else:
                print(end= '\n')

            ResFunction = SomeFunction(*args, **kwargs)

            fileMainFolder = "E:/Dokumenty/testFiles/"
            fileName = "text_file1.txt"
            with open((fileMainFolder + fileName), 'a') as file:
                file.write("---"*0x10 + '\n')

                file.write("*args: ")
                for i in args:
                    file.write("{}, ".format(i))
                else:
                    file.write('\n')

                file.write("**kwargs: ")
                for i in kwargs:
                    file.write("| key= {},  value= {} ".format(i, kwargs[i]))
                else:
                    file.write('\n')

                file.write("+++"*0x10 + '\n')
            return ResFunction
        return FunWithWrapper
    
    @CreateFunWithWrapper
    def ChangeSalary1(employName:str, newSalary:float, asBonus:bool)->float:
        print("ChangeSalary: ",end='\n')
        print("Emplout name: ", employName, "; New salary: ", newSalary, end='\n')
        return newSalary
    
    #ChangeSalary1("Jack O Lantern Panik", 9.99, True)
    ChangeSalary1("Genos cyborg", 345.79, True)


    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_WrapperFunWithParameter1
@brief      Wraper functionality wih parameter
@param[in]  ...
@note       ...
@return     ...
'''
def Call_WrapperFunWithParameter2()->None:

    def CreateFunWrapper_fullDir(fullDirectory:str)->object:
        def CreateFunWithWrapper(SomeFunction:object)->object:
            def FunWithWrapper(*args, **kwargs)->object:
                print("--"*0x10, end= '\n')

                print("Function name: ", SomeFunction.__name__, end= '\n')
                print("*args: ", end= '\t')
                for i in args:
                    print(i, end= ', ')
                else:
                    print(end= '\n')

                print("**kwargs: ", end= '\t')
                for i in kwargs:
                    print("key: ", i, "arg: ", kwargs[i], end= ', ')
                else:
                    print(end= '\n')

                ResFunction = SomeFunction(*args, **kwargs)

                with open((fullDirectory), 'a') as file:
                    file.write("---"*0x10 + '\n')

                    file.write("*args: ")
                    for i in args:
                        file.write("{}, ".format(i))
                    else:
                        file.write('\n')

                    file.write("**kwargs: ")
                    for i in kwargs:
                        file.write("| key= {},  value= {} ".format(i, kwargs[i]))
                    else:
                        file.write('\n')

                    file.write("+++"*0x10 + '\n')
                return ResFunction
            return FunWithWrapper
        return CreateFunWithWrapper
    
    @CreateFunWrapper_fullDir("E:/Dokumenty/testFiles/text_file1.txt")
    def ChangeSalary1(employName:str, newSalary:float, asBonus:bool)->float:
        print("ChangeSalary: ",end='\n')
        print("Emplout name: ", employName, "; New salary: ", newSalary, end='\n')
        return newSalary
    
    #ChangeSalary1("Jack O Lantern Panik", 9.99, True)
    ChangeSalary1("Tatsumaki", 864.79, True)


    return None
#=======================================================================================================================================

#=======================================================================================================================================
if (__name__ == "__main__"):
    Call_WrapperFunWithParameter2()
else:
    pass
#=======================================================================================================================================
