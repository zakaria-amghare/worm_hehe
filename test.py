from termcolor import cprint
import os
import time
for i in range(5):
    cprint("i will first creat simple file","yellow")
    f=open(f"zaki0{i}.py","w")
    from termcolor import cprint
    f.write("from termcolor import cprint\n"
    "cprint(\"zaki-chan\",\"green\")")
    f.close()
    os.system(f"copy zaki0{i}.py zaki000{i}.py ")
    os.system(f"python .\\zaki0{i}.py")
    os.system(f"python .\\zaki000{i}.py")