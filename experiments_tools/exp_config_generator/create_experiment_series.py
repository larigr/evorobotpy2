from Combiner import Combiner
from Ini_generator import Ini_Generator


dicionario = {'enviroment': ['AntBulletEnv-v0'],
              'random_change':[True],
              'maxsteps_change':[50]}


def generate_all_inis(base,foldername='experiment'):
    d = Combiner()

    dic_keys = list(base.keys())

    d.combine_dict_to_array(dic_keys, base)
    print(d.all_combinations)
    d.array_to_dict(dic_keys)

    gerador = Ini_Generator(d.all_combinations, foldername)
    gerador.create_all_exp()


generate_all_inis(dicionario,"ExperimentRandom")
