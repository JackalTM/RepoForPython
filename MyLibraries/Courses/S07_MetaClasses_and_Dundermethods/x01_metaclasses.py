
def FunMetaClassReturn():
    class Numbers:
        def __init__(self, num) -> None:
            self.num = num
            return None
        
    return Numbers

"""*******************************************
The way to create class object
"""
class BaseClass:
    def Name(self):
        print("BaseClass")
        return None

def AddAttribute(self, x, y):
    self.z = x + y
    print("x + y = {}".format(self.z))
    return None

InheritanceClass = type("BaseClass", (BaseClass,), { "x":5 , "AddAttribute" : AddAttribute})
#============================================
def CALL_test():
    print("==========================")

    SNumbers = FunMetaClassReturn()
    instNumbers = SNumbers(5)

    print(instNumbers.num)

    print("==========================")

    instTest2 = InheritanceClass()
    instTest2.Name()
    instTest2.AddAttribute(4, 5)

 #============================================++++++++++++++++++++++++   
class MetaClass(type):
    """ 
    __new__ do stuff before init
    """
    def __new__(self, className : str, bases : tuple, attributes : dict)->type:

        print("className:   {}".format(className))
        print("bases:       {}".format(bases))
        print("attributes:  {}".format(attributes))

        myAttributes = {}
        for  name, value in attributes.items():
            if( name.startswith("__")):
                myAttributes[name] = value
            else:
                myAttributes[name.upper()] = value 

        print("myAttributes:{}".format(myAttributes))

        return type(className, bases, myAttributes)
    
class Dog(metaclass= MetaClass):
    x = 2
    y = 4

    def __init__(self, name):
        self.name = name

    def bark(self):
        print("{} How How!".format(self.name))

def CALL_Test2():
    instDog = Dog("Nasus")
    instDog.BARK()

    return None


if (__name__ == "__main__"):
    CALL_Test2()
else:
    pass