import os

for x in range(1,10):
    os.system(f"python3.7 ../../../../../bin/es.py -f Walker2DBulletEnv-v0-1.ini -g bestgS{x}.npy -p ")