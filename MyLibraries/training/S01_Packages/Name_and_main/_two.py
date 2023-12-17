#python _two.py
import _one
print("TOP LEVEL _two.py!")

_one.OneFun()

if __name__ == "__main__":
    print("DIRECT RUN: _two.py ")
    # Then run SCRIPT!
    # It mean it run directly in "__main__.py"
else:
    print("IMPORT RUN: _two.py ")
    # Do nothing beacuse run indirectly