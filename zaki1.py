from termcolor import cprint
import os
import time
for i in range(2):
    cprint("this file would duplicate theoraticly exponantialy if we alter it ","yellow")
    os.system(f"copy test.py zaki{i}.py")