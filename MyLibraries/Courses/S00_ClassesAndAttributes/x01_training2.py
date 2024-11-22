'''*************************************************************************************************************************************
@name       FunctionEvaluation
@brief      Przetwarzanie kodu jaki jest wprowadzany zewnętrznie
@param[in]  ...
@note       ...
@return     ...
'''
def FunctionEvaluation1():
    value_x = 0xA
    str_password = "password"

    dict_globals = globals().copy()

    str_source_code = "value_x + value_x"
    resoult_eval = eval(str_source_code)

    print("Source code evaluation: ", resoult_eval, '\n', '\n')
    for i in dict_globals.values():
        print("- ", i)

    # Kasowanie zmiennej "str_password"
    del globals["str_password"]
    for i in dict_globals.values():
        print("- ", i)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       FunctionEvaluation
@brief      Przetwarzanie kodu jaki jest wprowadzany zewnętrznie
@param[in]  ...
@note       ...
@return     ...
'''
def FunctionEvaluation2():
    value_x = 0xA
    str_password = "password"
    
    #  Kasowanie wszystkich wartości aby dodać je ręcznie
    globals = {}
    str_source_code = "value_x + value_x"
    resoult_eval = eval(str_source_code)

    print("Source code evaluation: ", resoult_eval, '\n', '\n')

    for i in globals.values():
        print("- ", i)

    return None
#=======================================================================================================================================


'''*************************************************************************************************************************************
@name       Function_expr
@brief      Umożliwnie wykonywanie calych wyrażeń programistycznych zewnętrznie napisanych
            Jest to dośc niebiespiecznie rozwiązanie.
@param[in]  ...
@note       ...
@return     ...
'''
def Function_expr()->None:
    var_x = 15
    src_code = "var_x + var_x"
    code_resoult = eval(src_code)
    print("eval() = ", code_resoult)

    var_x = 15
    src_code = "var_x = var_x * 2"
    code_resoult = exec(src_code)
    print("var_x = ", var_x)

    # Możliwośc wykonawania zewnętrznego kodu
    src_code = '''
for i in range(0,10):
    print("i= ", i)
    '''
    code_resoult = exec(src_code)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Function_compile
@brief      Zewnętrzny kod który ma duzy opszar. Prkompilacja zewnętrznego kodu
@param[in]  ...
@note       ...
@return     ...
'''
def Function_compile()->None:
    num = 0
    source = "num = num + 1"
    scr_compiled = compile(source, 'Internal variabale source', "exec")

    for i in range(0,16):
        exec(scr_compiled)
        print("reportLine= ", num)
    else:
        print("Finish value= ", num)

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Function_args
@brief      Wztawienie wiele argumnetów jako tuplet. Można dac wiele.
@param[in]  ...
@note       ...
@return     ...
'''
def Function_args(*args)->None:
    for i in args:
        print("- ", i)
    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Function_kwargs
@brief      Wztawienie wiele argumnetów jako słonik. Można dac wiele.
@param[in]  ...
@note       ...
@return     ...
'''
def Function_kwargs(**kwargs)->None:
    for i in kwargs:
        print("key= ", i, " value= ", kwargs[i])
    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Function_args_kwargs
@brief      ...
@param[in]  ...
@note       ...
@return     ...
'''
def Function_args_kwargs(*args, **kwargs)->None:
    #Wyświetlanie dla *args
    for i in args:
        print("i= ", i)

    #Wyswietlanie dla **kwargs
    for j in kwargs:
        print("key= ", j, " value= ", kwargs[j])
    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_Function_args_kwargs
@brief      Wywoływanie funkcji dla *args oraz **kwargs
@param[in]  ...
@note       ...
@return     ...
'''
def Call_Function_args_kwargs()->None:
    programNum = 1
    '''
    Required python version >= 3.10
    current version 3.9.13
    match programNum:
        case 1:
            Function_args(1,2,3,4,5,6,7,8,9)
        case 2:
            Function_kwargs(color= "red", size= "XL")
        case 3:
            my_args = (1,2,3,4)
            my_kwargs = {"A":1, "B":2, "C":3, "D":4}
            Function_args_kwargs(*my_args, **my_kwargs)
        case _:
            pass
    '''

    if(programNum == 1):
        Function_args(1,2,3,4,5,6,7,8,9)
    elif(programNum == 2):
        Function_kwargs(color= "red", size= "XL")
    elif(programNum == 3):
        my_args = (1,2,3,4)
        my_kwargs = {"A":1, "B":2, "C":3, "D":4}
        Function_args_kwargs(*my_args, **my_kwargs)
    else:
        pass
    
    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_FunctionsAsAgrs
@brief      Testing Functions as argument to another function
@param[in]  ...
@note       ...
@return     ...
'''
def Call_FunctionsAsAgrs()->None:

    def AddNums(numA:int, numB:int)->int:
        return numA + numB
    
    def SubNums(numA:int, numB:int)->int:
        return numA - numB
    
    def MulNums(numA:int, numB:int)->int:
        return numA * numB
    

    def FunctionWraper(Funct:object, arg1:int, arg2:int)->None:
        print("Wrapper start: ", end='\t')
        res = Funct(arg1, arg2)
        print("{} {} = {}".format(arg1, arg2, res), end= ' ')
        print(" end", end= '\n')
        return None
    
    listFinctions = (AddNums, SubNums, MulNums)
    listArgs = ((1,2), (3,4), (5,6))
    
    for f in listFinctions:
        for i,j in listArgs:
            FunctionWraper(f, i,j)

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
    def ChangeSalary(employName:str, newSalary:float, asBonus:bool)->float:
        print("ChangeSalary: ",end='\n')
        print("Hero name: ", employName, "; New salary: ", newSalary, end='\n')
        return newSalary
    
    @CreateFunWrapper_fullDir("E:/Dokumenty/testFiles/text_file2.txt")
    def ChangePosition(employName:str, newPosition:int, asBonus:bool)->float:
        print("ChangePosition: ",end='\n')
        print("Hero", employName, "; New position: ", newPosition, end='\n')
        return newPosition
    
    #ChangeSalary1("Jack O Lantern Panik", 9.99, True)
    ChangeSalary("Tank Top Master", 398.79, True)
    ChangePosition("Tank Top Master", 0x0D, True)


    return None
#=======================================================================================================================================


'''*************************************************************************************************************************************
@name       Call_LambdaExpresion1
@brief      Lambda function written in more simple way. Can be use for ony une use
@param[in]  ...
@note       ...
@return     ...
'''
def Call_LambdaExpresion1()->None:

    def FunDoubleNormal(x:float)->float:
        return (x * x)
    
    FunDoubleLambda = lambda x: (x * x)

    def FunPowerNormal(x:float, y:float)->float:
        return (x * y)
    
    FunPowerLambda = lambda x,y: x**y
    #add = lambda x: int, y: int -> int: x + y
    #FunPowerLambda = lambda x:float, y:float -> float: x**y
    #FunPowerLambda = lambda x,y: x**y
    #FunPowerLambda = lambda x,y: ->float: x**y

    print("Normal fun: ", FunDoubleNormal(2.718), ", Lambda fun: ", FunDoubleLambda(2.718))

    return None
#========================================
def Call_LambdaExpresion2()->None:

    tuplNums = (0,1,2,3,4,5,6,7,8,9)

    def NormalParityCheck(n:int)->bool:
        return (n % 2) == 0
    
    LambdaParityCheck = lambda n: (n%2 == 0)

    tuplFiltr = tuple(filter(NormalParityCheck, tuplNums))
    print("Normal fun: ", tuplFiltr)

    tuplFiltr = tuple(filter(LambdaParityCheck, tuplNums))
    print("Lambda asigned: ", tuplFiltr)

    tuplFiltr = tuple(filter(lambda n: (n%2 == 0), tuplNums))
    print("Lambda as arg:  ", tuplFiltr)  
    
    return None
#========================================
def Call_LambdaExprestion3()->None:

    def GenFunctions(n:int)->object:
        return (lambda x: n*x)
    
    FunMulBy3 = GenFunctions(3)
    print("FunMulBy3({})= ".format(5), FunMulBy3(5))

    return None
#=======================================================================================================================================

'''*************************************************************************************************************************************
@name       Call_IfShortCondition
@brief      Short if statement expresion
@note       ...
'''
def Call_IfShortCondition()->None:

    def ShortIf(condition:bool, text:str)->None:
        text = text if condition ==  True else "Error"
        print("msg: ", text, end= '\n')
        return None
    
    def ShortIfNested(number:int)->None:
        num = 0x11 if number == 1 else 0x22 if number == 2 else 0x33 if number == 0x33 else 0xFF
        print("Number: ", hex(num))
        return None
    
    ShortIfNested(2)
    

    return None
#=======================================================================================================================================

#=======================================================================================================================================
if (__name__ == "__main__"):
    pass
else:
    pass
#=======================================================================================================================================