from gerador_ini import GeraIni


class combinador():
    def __init__(self):
        self.combinados = []
        self.lista = []

    def todasCombina(self, lista_params, dicionario, n=0):
        if n == 0:
            self.lista = []
        if n == len(lista_params):
            return
        else:
            for x in dicionario[lista_params[n]]:
                self.lista.append(x)
                if n == len(lista_params)-1:
                    self.combinados.append(self.lista.copy())

                self.todasCombina(lista_params, dicionario, n+1)
                self.lista.pop()

    def combinados_to_dict(self, lista_params):
        new_dic = {}
        new_list = []
        for lista in self.combinados:
            for x in range(len(lista_params)):
                new_dic[lista_params[x]] = lista[x]

            new_list.append(new_dic.copy())
        self.combinados = new_list


if __name__ == '__main__':
    d = combinador()
    base = {'enviroment': ['HopperBulletEnv-v0', 'Walker2DBulletEnv-v5'],
            'maxmsteps': [27, 32, 23], 'steps': [1, 2]}
    lista = list(base.keys())

    bat = d.todasCombina(lista, base)
    print(d.combinados)
    d.combinados_to_dict(lista)
# print(d.combinados)

    gerador = GeraIni(d.combinados)
    gerador.criar_all_exp()
