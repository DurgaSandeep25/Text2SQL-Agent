import os
def from_root():
    cwd = os.getcwd()

    while cwd != os.path.dirname(cwd):
        if "environment.yml" in os.listdir():
            return cwd
    
    print("####################### from root does not work anymore")
    return ""
