import os

for x in range(1,11):
    os.system(f"python3 ../../../../../bin/es.py -f ant.ini -g bestgS{x}.npy")