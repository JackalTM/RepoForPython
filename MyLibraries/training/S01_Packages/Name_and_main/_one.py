#python _one.py
print("Hello: ")

def OneFun():
    print("Func in _one.py ")
    return

print("Top level in _one.py:")

if __name__ == "__main__":
    print("DIRECT: call _one.py")
    # Then run SCRIPT!
    # It mean it run directly in "__main__.py"
else:
    print("IMPORT: call _one.py")
        # Do nothing beacuse run indirectly
    
