import click
from evorobotpy2.environments.env_controller import EnvironmentController

@click.group()
def cli():
    pass

@cli.command()
@click.option("--env", "-e", help="Target environment (acrobot, ant, hopper, etc...)")
@click.option("--seed", "-s", help="Specify a seed to run the simulator")
def run_simulator(env, seed):
    env_controller = EnvironmentController()
    env_controller.run_env(env, seed)

if __name__ == "__main__":
    cli()