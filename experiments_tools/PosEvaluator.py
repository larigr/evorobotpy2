import os


for x in range(1,11):
    os.system(f"python3.7 ../../evorobotpy2/bin/es.py -f AntBulletEnv-v0-2.ini -g  bestgS{x}.npy -p")