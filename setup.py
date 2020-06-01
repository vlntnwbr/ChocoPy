"""Setup script."""

from setuptools import find_packages, setup
from types import FunctionType

from choco_py import NAME


def get_entrypoint(ep: str, func: FunctionType) -> str:
    """Return formatted setuptools entrypoint string for function"""
    return "{} = {}:{}".format(ep, func.__module__, func.__name__)


if __name__ == '__main__':
    setup(
        name=NAME,
        version="0.1.0",
        description="Chocolatey update check and upgrade notification.",
        license="GPLv3",
        platforms=["Windows"],
        author="Valentin Weber",
        author_email="vweber@stud.hs-heilbronn.de",
        url="https://github.com/vlntnwbr/ChocoPy",
        packages=find_packages(),
        install_requires=["win10toast>=0.9"],
        include_package_data=True,
        entry_points={
            "console_scripts": []
        },
        classifiers=[
            "Development Status :: 1 - Planning",
            "Environment :: Console",
            "Operating System :: Microsoft :: Windows :: Windows 10",
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: English",
            "Topic :: Utilities"
            "Intended Audience :: End Users/Desktop",
            "Intended Audience :: Other Audience",
        ]
    )
