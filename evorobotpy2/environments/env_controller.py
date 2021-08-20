from evorobotpy2.bin.es import main
import sys
import os

class EnvironmentController:
    def __init__(self):
        self.envs = {
        'acrobot': 'acrobot',
        'ant': 'ant',
        'bodybrain': 'bodybrain',
        'discrim': 'ErDiscrim',
        'dpole': 'ErDpole',
        'halfcheetah': 'halfcheetah',
        'hopper': 'hopper',
        'humanoid': 'humanoid',
        'mountaincar': 'mountaincarcontinuous',
        'pendulum': 'pendulum',
        'predprey': 'ErPredPrey',
        'staybehind': 'ErStayBehind',
        'swingup': 'swingup',
        'walker': 'walker2d'
    }

    def verify_env(self, env):
        if env in self.envs.keys():
           return True
        else:
            print("The Environment passed is invalid, please try one of the following options:")
            [print(key) for key in self.envs.keys()]

    def run_env(self, env, seed=None):
        if self.verify_env(env):
            work_dir = os.path.dirname(os.path.abspath(__file__))
            env_dir = f'/x{env}'
            os.chdir(work_dir + env_dir)
            sys.argv = sys.argv[:1]
            sys.argv += ['-f', f'{self.envs[env]}.ini']
            sys.argv += ['-s', seed]
            main(sys.argv)
