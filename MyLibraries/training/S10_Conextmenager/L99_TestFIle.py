def main1():

    parameters = {}

    parameters['A'] = '90m2'
    parameters['B'] = '150m3'


    for i in parameters:

        key = i
        val = parameters[i]
        print('{}={}'.format(key,val))

    return None

def main2():

    def F1():
        '''
        Ciekawa sztuczka przy pomocy generatora
        zmiena zwracanych liczb przy kolejnych wywołaniach ffunkcji generatora
        '''
        A = 1
        B = 2
        C = 3
        yield A
        yield B
        yield C
        return None

    for i in F1():
        print(i)

    return None

main2()
