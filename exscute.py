import os
import random
file=os.path.basename(__file__)
x = random.randint(1,10)
if x == 5:
    print("you ar unlucky")
    print("what a miss")
    for i in range(4):
        os.system(f"copy {file} {i}{file}")
        os.system(f"python ./{i}{file}")
        os.system(f"python {i}{file}")
else:

    print("lucku you",x)