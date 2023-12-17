class Weapon():

    def __init__(self):
        print("Class Weapon created!", end= '\n')
        return

    def WhatKind(self):
        print("Weapon depend of situation", end= '\n')
        return

    def Atack(self):
        print("Atacking!", end= '\n')
        return

class Sword(Weapon):

    def __init__(self):
        Weapon.__init__(self)
        print("Sword created!")
        return

    def WhatKind(self):
        print("White metal weapon", end= '\n')    
        return
    
    def Swing(self, nTimes):
        print("Sword swing {} times!".format(nTimes), end= '\n')
        return


def CALL_ClassInheritance_01():
    instWeapon = Weapon()
    instWeapon.WhatKind()
    instWeapon.Atack()
    return

def CALL_ClassINheritance_02():
    instSword = Sword()
    instSword.WhatKind()
    instSword.Atack()
    instSword.Swing(0x03)
    return

#========================================================================================

class Pistol():

    def __init__(self, name):
        self.name = name
        return
    
    def Shoot(self, caliber):
        tStr = "Pistol {} of {} caliber shoot!".format(self.name ,caliber)
        return tStr
    
class Rifle():

    def __init__(self, name):
        self.name = name
        return
    
    def Shoot(self, caliber):
        tStr = "Rifle {} of {} caliber shoot!".format(self.name, caliber)
        return tStr

def CALL_PolimorfismPistolRifle():
    instPistol = Pistol("USP")
    instRifle = Rifle("L96")

    print(instPistol.Shoot(".45 cal"))
    print(instRifle.Shoot("7,56"))
    return

def CALL_IterThroughtClass():
    instPistol = Pistol("USP")
    instRifle = Rifle("L96")

    for i in (instPistol, instRifle):
        print(i.Shoot(" .045 "))
    return

#========================================================================================

class Knife():
    #Every instance of class will have some attributes
    def __init__(self, typs):
        self.typs = typs
        return
    
    def Cut(self):
        raise NotImplementedError("Base class, implementation needed!")
    
class Folder(Knife):

    def Cut(self, nTimes):
        print("Folding {} knive cut {} times.".format(self.typs, nTimes), end= '\n')
        return
    
class Machete(Knife):

    def Cut(self, nTimes):
        print("Machete {} blade cut {} times.".format(self.typs, nTimes), end= '\n')
        return
    

def CALL_BaseClassDerived():
    instFolder = Folder("Cold Steel")
    instMachete = Machete("Condor")

    instFolder.Cut(4)
    instMachete.Cut(7)

    return

#========================================================================================