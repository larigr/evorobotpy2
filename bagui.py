file = "xhopper/hopper.ini"
txt = open(file,'r')
t = txt.readlines()
dicionario = {}
policy = {}
algo = {}
cont = 0
import json 
import os
def ini_to_json(file,newfile='ini_data.json'):
    txt = open(file,'r')
    t = txt.readlines()
    dicionario = {}
    policy = {}
    algo = {}
    cont = 0
    txt.close()
    for linha in t:
        linha=linha[:-1].strip() 
        cont+=1
        if linha == '':
            continue 
        if cont == 2:
            exp = linha

        if cont > 12:
        
            index = linha.find('=')
            policy[linha[:index-1]] = linha[index+1:]
            
        elif cont >4 and cont < 11:
            index = linha.find('=')
            algo[linha[:index-1]] = linha[index+1:]
    dicionario['[ALGO]'] = algo
    dicionario['[POLICY]'] = policy
    final = {exp:dicionario}

    with open('ini_tudo.json','a') as fp:
        fp.write(',')
        json.dump(final,fp)
        

    fp.close()
dir = os.listdir()
print(dir)
#bagui = open('ini_data.json','a')
#bagui.write('[')
for d in dir:
    if d[0]== 'x':
        for filename in os.listdir(d):
            if filename.endswith(".ini" ):
                ini_to_json(os.path.join(d,filename))

#bagui.write(']')