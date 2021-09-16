import os
nome = 'teste2'
base = {'enviroment':'environment = HopperBulletEnv-v0','maxmsteps ':27,'d':2}
import json

class GeraIni():
    def __init__(self,nome,dicionario):
        self.__nome = nome
        self.__entrada = dicionario
        self.exp = dicionario['enviroment']
        filename= 'ini_tud.json'
        with open(filename) as data:
            self.__ini_data = json.load(data)
        for dic in self.__ini_data:
            if self.exp in dic.keys():
                self.__ini_data = dic


    def modificar_dict(self):
        data = self.__ini_data[self.exp]
        for values in data.items():
            values = values[1]
            for key in self.__entrada:
                if key in values:
                    values[key]= self.__entrada[key]
        self.ini_feito = data    
        return data 

    def criar_ini(self):
        os.mkdir(self.__nome)
        path = os.path.join(self.__nome,self.__nome+'.ini')
        with open(path,'w') as inifile:
            inifile.write('[EXP]\n')
            inifile.write(self.exp+str('\n'))
            for key,args in self.ini_feito.items():
                inifile.write(key+"\n")
                for skey,sargs in args.items():
                    linha = skey+" = "+str(sargs)+"\n"
                    inifile.write(linha)

arquivo = GeraIni('pastel',base) 
arquivo.modificar_dict()
arquivo.criar_ini()


