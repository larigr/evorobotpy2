from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as r:
    requirements = r.read()

setup(
    name="evorobotpy2",
    version="0.1.0",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arthur-plautz/evorobotpy2",
    project_urls={
        "Bug Tracker": "https://github.com/arthur-plautz/evorobotpy2/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    package_dir={"evorobotpy2": "evorobotpy2"},
    package_data={'evorobotpy2': ['bin/*', 'environments/*', 'environments/*/*', 'environments/*/*/*']},
    include_package_data=True,
    packages=find_packages(include=['evorobotpy2', 'evorobotpy2.*']),
    entry_points={
        'console_scripts': [
            'evorobot=evorobotpy2.cli:cli',
        ],
    },
    python_requires=">=3.7",
    install_requires=requirements
)