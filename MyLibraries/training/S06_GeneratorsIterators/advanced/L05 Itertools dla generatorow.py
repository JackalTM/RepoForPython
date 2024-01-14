import itertools as it
import math

def Fexample():
    list = ['a', 'b', 'c', 'd']

    # Unikalne kombinacje
    for i in it.combinations(list ,1):
        print(i)

    print("\n \n")

    # Wsztkie kombinacje ze wzgladu na kolejnosc
    for i in it.permutations(list ,1):
        print(i)

    print("\n \n")

    # Losowanie ze wracaniem
    for i in it.combinations_with_replacement(list, 1):
        print(i)

    return None


def Money():

    list = []

    wallet = [20, 20, 20, 20, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

    for i in range(6, 15):
        for c in it.combinations(wallet, i):
            if (sum(c) == 100):
                list.append(c)
            else:
                pass

    return set(list)
def Nutes():
    notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

    for x in it.permutations(notes, 4):
        print(x)

    print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(math.factorial(len(notes))/math.factorial(len(notes) - 4)))

    input('Press enter')

    for x in it.product(notes, repeat=4):
        print(x)

    print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(pow(len(notes), 4)))

    return None

def main():

    #Fexample()

    #set = Money()
   # print(set)

    Nutes()

    return None
main()
