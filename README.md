# evorobotpy2
## Setup

Firstly, if you are using Linux, install the following library:
```bash
sudo apt-get install libgsl-dev libopenmpi-dev
```
After that, make shure to create a virtual environment in the root directory:
```bash
virtualenv -p python3 venv
source venv/bin/activate
```
Then install the requirements:
```bash
pip install -r requirements.txt
```

To make things easier you can create an alias to run the simulator:
```
make create_alias
```

And now we are good to go!

## Compiling

Before running the models, you need to compile the resource that you'll use.
The main resources available are: ErDiscrim, ErDpole, ErPredprey, ErStaybehind and Evonet.
You can look for the compile command in your terminal by writing `make compile_` and then pressing `tab` to see all commands.
You can find all of them in the `Makefile`, but here's a list:
```
make compile_erdiscrim
make compile_erdpole
make compile_evonet
make compile_erpredprey
make compile_erstaybehind
```
And if you just want to install all of them at once:
```
make compile_all
```

## Running

To run a model, first go to the target environment, and then run the following command:
```bash
evrun -f {target envirnoment}.ini
```
To see all execution options run:
```bash
evrun --help
```

## Contributing

If at some point you installed a new package, and therefore it will be needed to run the new code, you can update the requirements by running:
```bash
make update_requirements
```

## Concepts

A tool for training robots through evolutionary and reinforcement learning methods

The tool is documented in [How to Train Robots through Evolutionary and Reinforcement Learning Methods](https://bacrobotics.com/Chapter13.html) which includes also a detailed tutorial with exercises.

For an introduction to the theory and to state-of-the-art research in this areas, see the associated open-access book [Behavioral and Cognitive Robotics: An Adaptive Perspective](https://bacrobotics.com)

## Credits

Please use this BibTeX to cite this repository in your publications:
```
@misc{evorobotpy2,
  author = {Stefano Nolfi},
  title = {A tool for training robots through evolutionary and reinforcement learning methods},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/snolfi/evorobotpy2}},
}
```
