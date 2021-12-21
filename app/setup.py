from setuptools import find_packages
from setuptools import setup

setup(
    name="MassCreator",
    version="0.1",
    packages=find_packages(),  # other arguments here...
    entry_points={
        "console_scripts": [
            "mc = src.main.python.statusUI:main",
            "mass-creator = src.main.python.statusUI:main",
        ]
    },
    include_package_data=True,
)
