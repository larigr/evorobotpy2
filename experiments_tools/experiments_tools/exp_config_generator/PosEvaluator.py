import os

for x in range(1,11):
    os.system(f"python3.7 ../../../../../bin/es.py -f Walker2DBulletEnv-v0-3.ini -g bestgS{x}.npy -p ")