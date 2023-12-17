import random
#================================================
def GetRecords(filePath):
    """
    Funkcja zwracająca elemanty w pliku txt
    Plik strumieniowy,  przetwarzany strumieniowo
    """
    print("--- Opening file ---")
    File = open(filePath)

    for line in File:
        l = line.replace("\n"," ")  # 1. Motoda rozczepiania stringu
        l = line.rstrip("\n")       # 2. Metoda rozczepiania stringu
        a,b = l.split(":")          # 3. Rozdzielanie stringu przez konkretnu element
        yield a,b

    print("--- Closing file ---")
    File.close()
    return None
#================================================
def RandomWithSum(valueNumbers, asertedSum):
    """
    Laboratorium zadanie na losowy generator
    """
    trial = 0
    numbers = list(range(valueNumbers))

    while True:
        trial = trial + 1
        for i in range(valueNumbers):
            numbers[i] = random.randint(1, 101)

        if (sum(numbers) == asertedSum):
            yield(trial, numbers)
            trial = 0
#================================================
def main():
    """
    Main funkcja główna
    """
    for i,j in GetRecords("txt1.txt"):
        print("{} <=> {}".format(i,j))

    print("==== \n")

    for i in range(10):
        (number_of_trials, numbers) = next(RandomWithSum(3, 100))
        print(number_of_trials, numbers)

    return None
#================================================
main()
