import datetime as dt

'''******************************************************************************************
@name   MilionDays_Generator
@breif  Funkcja która zwraca kolajne wartosci 
        Funkcja jest dalej aktywna w pamięci dopuki nie zostanie zakonczona
@note   Dopiero po zakonczeniu pamięc jets zwalniana
        Po wyczerpaniu zwracany jest bład StopIteration() który przerywa pętlę for
'''
def MilionDays_Generator(year:int=1, month:int=1, day:int=1, maxdays:int=1)->int:
    tdate = dt.date(year, month, day)
    for i in range(maxdays):
        yield (tdate + dt.timedelta(days=i))
#==============================================================================================
def CALL_Test1():
    for i in MilionDays_Generator(2024,9,1,90):
        print(i)
#==============================================================================================
'''********************************************************************************************
@Name   VariablesSize_Generator
@brief  Przykłądowe działanie generator dla petli while.
@note   Aby przerwac generowanie kolejnych watości należy zwrócic "return StopIteration()"
        Nozwa dla generowanie wartości w momncie kiedy sa potrzebne nazywa sie "Lazy Eveluation"
        Dla wiekszych obiektów zmniejsza urzucie pamieci RAM czasem też CPU
'''
def VariablesSize_Generator():
    num = 1
    while(num < 5):
        yield (">> {}".format(num * 8))
        num = num + 1
    return StopIteration()
#==============================================================================================
def CALL_Test2():
    for i in VariablesSize_Generator():
        print(i)
#==============================================================================================

'''********************************************************************************************
@name   ExerciseGenerator
'''
def ExerciseGenerator_Inceprion(refProducts:list, refPromotions:list, refCostomers:list)->str:
    i:int = 0
    j:int = 0
    k:int = 0
    iMax:int = len(refProducts)
    jMax:int = len(refPromotions)
    kMax:int = len(refCostomers)
    nMax = 0
    while(i<iMax):
        str_i = refProducts[i]
        i = i + 1
        while(j<jMax):
            str_j = refPromotions[j]
            j = j + 1
            while(k<kMax):
                str_k = refCostomers[k]
                k = k + 1
                yield (">> {}-{}-{}".format(str_i, str_j, str_k))
                if(nMax > 100):
                    raise Exception
            k=0
        j=0
    return StopIteration()
#==============================================================================================
def CALL_Test_Exercise():
    for i in ExerciseGenerator_Inceprion(["i0", "i1"], ["j0", "j1"], ["k0", "k1"]):
        print(i)
#==============================================================================================

if(__name__ == ("__main__")):
    CALL_Test_Exercise()
else:
    pass