import subprocess
import  os
folders  = ['humanoidV5control']

for f in folders:
    for i in range(1, 11):
        print(f"folder {f} e seed {i}")
        cmd = f"cd {f} && python ../../../../../bin/es.py -f humanoid.ini -g bestgS{i}.npy -p"
        os.system(cmd) 
