from queue import Queue 

"""
Dunder methods allow to implement sepcial functionality acording to task like: +, -, print(), *, 
Any functionality can be implemented
https://docs.python.org/3/reference/datamodel.html
"""

class Person:

    def __init__(self, name):
        self.name = name
        return None
    
    def __repr__(self) -> str:
        return "Person - {}".format(self.name)
    
    def __mul__(self, x):
        if(type(x) == int):
            self.name = self.name * x
        else:
            raise Exception("Wrong argument!")
        
    def __call__(self, y):
        print("__call__ y = {}".format(y))
        return None
    

class NewQueue(Queue):
        def __repr__(self) -> str:
            return "Queue({})".format(self._qsize())
        
        def __add__(self, item : int)->None:
            self.put(item)
            return  None
        
        def __sub__(self, item : int)->None:
            self.get()
            return  None

def CALL_Test():

    Mike = Person("Mike")
    Mike * 3
    print(Mike)
    Mike(5)

    instQueue = NewQueue()

    print(instQueue)

    instQueue + 0xFF
    print(instQueue)

    instQueue + 0xAA
    print(instQueue)


    return None


if (__name__ == "__main__"):
    CALL_Test()
else:
    pass