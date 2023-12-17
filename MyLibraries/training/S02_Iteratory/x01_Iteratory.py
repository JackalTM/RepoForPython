import csv

#**********************************************************************************
# Name      TupletListSet
#
# Brief     Tworzenie obiektu iteratora z tupletu
#           Lista działa podobnie z tym wypadku
#           Set moża z niego zrobic obiekt iterowant  
#    
# parameter[in] void
#
def TupletListSet():
    mytuplet  = (1, 2, 3, 4, 5)
    mylista   = [1, 2, 3, 4, 5]
    Set = {1, 2, 'A','B', ('C','B')}

    # Tworzenie obiektu iteratora z tupletu
    # Lista działa podobnie z tym wypadku
    # Set moża z niego zrobic obiekt iterowant

    iterableObject = iter(Set)

    temp = next(iterableObject)
    print(temp)

    temp = next(iterableObject)
    print(temp)

    temp = next(iterableObject)
    print(temp)

    temp = next(iterableObject)
    print(temp)
    # Iterator wyczerpał sie
    temp = next(iterableObject)
    print(temp)

    return None
#=================================================================================

#**********************************************************************************
# Name      IterFromFileFile
# Brief     Show how iterators work
#           next() function is called
#           when next expired then iterator is finished            
#                
# parameter[in] void
#
def IterFromFileFile1():
    print("IterFromFileFile2")
    direction = "D:/01_Programistyczne_pliki/x07_WZ_Workspace_for_Python/Packages/training/S09_Iteratory/text.txt"
    print("CD: {}".format(direction))
    with open(direction, 'r') as file:
        while True:
            try:  
                row = next(file) # iterators have can be next()
                print(" {} ".format(row))

            except StopIteration:
                break
    return None

#**********************************************************************************
# Name      IterFromFileFile
# Brief     Iteration from file 
#                
# parameter[in] void
#
def IterFromFileFile2():
    print("IterFromFileFile2")
    direction = "D:/01_Programistyczne_pliki/x07_WZ_Workspace_for_Python/Packages/training/S09_Iteratory/text.txt"
    print("CD: {}".format(direction))
    with open(direction, 'r') as file:
        for row in file:
            print(" {} ".format(row))

    return None
    #Jesli napotkamy na koniec pliku zgloszony bedzie bład
#=================================================================================

#**********************************************************************************
# Name      IteratorsAndIterables_S1
# Brief     Creatig iterators
#                
# parameter[in] void
#
def IteratorsAndIterables_S1():
    nums = [1,2,3,4,5,6,7,8,9]
    i_nums = nums.__iter__() 
    j_nums = iter(nums)

    # Object are the same
    print(" {} - {} - {}".format(next(i_nums), next(i_nums), next(i_nums)))
    print(" {} - {} - {}".format(next(j_nums), next(j_nums), next(j_nums)))
    return None

    #Jesli napotkamy na koniec pliku zgloszony bedzie bład
#==================================================================================

#**********************************************************************************
# Name      MyRangeLike
# Brief     Range like class
#                
class MyRangeLike:

    def __init__(self, inStart, inEnd):
        self.value  = inStart
        self.end    = inEnd
        return None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if( self.value > self.end):
            raise StopIteration

        current = self.value
        self.value += 1
        return current
#==================================================================================

#**********************************************************************************
# Name      MyGeneratorLike
# Brief     Generator function
# 
def MyGeneratorLike(instart, inEnd):
    current = instart
    while(current < inEnd):
        yield current
        current += 1
#==================================================================================


def CallIteratorsAndIterables_S2():
    nums = MyRangeLike(0, 9)
    print("Iterator")
    for i in nums:
        print("i={} num(i)= {}".format(i, i))
    return None

def CallGenerator1():
    nums = MyGeneratorLike(0, 9)
    print("Generator")
    for i in nums:
        print("i={} num(i)= {}".format(i, i))
    return None


#**********************************************************************************
# Name      Exercise1
# Brief     Initialization of renumber NC class       
# parameter[in] void
#
def Exercise1():
    # W opdpowiedzi dostaje listy
    with open('text.csv','r') as fileCSV:
        csvreader = csv.reader(fileCSV, delimiter=',')

        for temp in csvreader:
            print('{} \t {} \t {}'.format(temp[0], temp[1], temp[2]))
#=================================================================================

#**********************************************************************************
# Name      
# Brief           
# parameter[in] 
# parameter[in] 
def Exercise2():
    # W opdpowiedzi dostaje listy
    with open('text.csv','r') as fileCSV:
        csvreader = csv.reader(fileCSV, delimiter=',')

        while 1:
            try:
                temp = next(csvreader)
                print('{} \t {} \t {}'.format(temp[0], temp[1], temp[2]))

            except StopIteration:
                print('koniec')
                break
    return None
#=================================================================================

#**********************************************************************************
# Name      
# Brief           
# parameter[in] 
# parameter[in] 



#**********************************************************************************
# Name      
# Brief           
# parameter[in] 
# parameter[in] 
def Call_x01_Iteratory():
    #TupletListSet()
    #IterFromFileFile1()
    #IterFromFileFile2()
    #Exercise1()
    #Exercise2()
    #IteratorsAndIterables_S1()
    #IteratorsAndIterables_S2()
    CallGenerator1()
    return None
#=================================================================================
