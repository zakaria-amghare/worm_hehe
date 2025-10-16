CHUNK=1####CHUNK = 50 * 1024 * 1024          # 50 MB
MAX=10####MAX   = 1024**3               # 2 GB ceiling
#those are vallues are for testing

from random_File import random_name
import os 
Here=os.path.dirname(__file__)
SUB=os.path.join(Here,"the_big_folder")
os.makedirs(SUB,exist_ok=True)
#print(random_name()) 
#####for testing reasons i wouldnt use random extantions 

total=0
while total < MAX:
    with open(os.path.join(SUB,random_name()),"wb") as f:
        f.write(b"hahaha\n"*CHUNK)
    total+=CHUNK
    print("total",total)
