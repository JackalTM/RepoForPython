class FullClassExample():
    # Atributes the same for every instance
    FULL_DIR = "C:/New Folder/file.exe"
    atribute1 = 1
    atribute2 = 2

    # When instance is created:
    def __init__(self, inPar1= 0, inPar2= 1):
        self.par1 = inPar1
        self.par2 = inPar2
        self.methamount = 0
        return

    # Methods / actions
    def BlueMethUpdate(self, amount):
        self.methamount = amount
        return

    # Methods / actions
    def BlueMethPrint(self):
        print("Amount of blumeth {}".format(self.methamount), end= '\n')
        return
