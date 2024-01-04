import random

DELETE_INSTANCES = True
if DELETE_INSTANCES:
    del random._inst 
    del random.seed 
    del random.random 
    del random.uniform
    del random.triangular 
    del random.randint
    del random.choice 
    del random.randrange
    del random.sample 
    del random.shuffle 
    del random.choices 
    del random.normalvariate 
    del random.lognormvariate 
    del random.expovariate 
    del random.vonmisesvariate 
    del random.gammavariate 
    del random.gauss 
    del random.betavariate 
    del random.paretovariate 
    del random.weibullvariate 
    del random.getstate 
    del random.setstate 
    del random.getrandbits 
    del random.randbytes