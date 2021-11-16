from Combiner import Combiner
from Ini_generator import Ini_Generator


dicionario = {'enviroment': ['AntBulletEnv-v0', 'HopperBulletEnv-v0', 'Walker2DBulletEnv-v0'],
              'maxsteps': [500], 'maxmsteps':[50]}


def generate_all_inis(base):
    d = Combiner()

    dic_keys = list(base.keys())

    d.combine_dict_to_array(dic_keys, base)
    print(d.all_combinations)
    d.array_to_dict(dic_keys)

    gerador = Ini_Generator(d.all_combinations, 'experiment_maxsteps_type5')
    gerador.create_all_exp()


generate_all_inis(dicionario)
