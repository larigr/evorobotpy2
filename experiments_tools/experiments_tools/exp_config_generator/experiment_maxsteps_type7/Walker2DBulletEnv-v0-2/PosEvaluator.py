import os

for x in range(1,10):
    os.system(f"python ../../../../../bin/es.py -f Walker2DBulletEnv-v0-2.ini -g bestgS{x}.npy")