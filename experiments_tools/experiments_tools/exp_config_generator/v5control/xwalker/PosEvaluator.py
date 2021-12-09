import os

for x in range(1,11):
    os.system(f"python ../../../../../bin/es.py -f walker2d.ini -g bestgS{x}.npy -p ")