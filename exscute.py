CHUNK=1####CHUNK = 50 * 1024 * 1024          # 50 MB
MAX=10####MAX   = 1024**3               # 2 GB ceiling
#those are vallues are for testing
GB = 1024 **3
from random_File import random_name
import os,subprocess
Here=os.path.dirname(__file__)
SUB=os.path.join(Here,"the_big_folder")
os.makedirs(SUB,exist_ok=True)
name=random_name()

subprocess.run(['fsutil'
                ,"file"
                ,"createnew"
                ,f"{name}"
                ,str(GB)
                ])
with open(name, "r+b") as f:
        f.write(b"X" * 4096)