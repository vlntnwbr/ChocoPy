"""Setup script."""

from setuptools import find_packages, setup
from types import FunctionType


def get_entrypoint(ep: str, func: FunctionType) -> str:
    """Return formatted setuptools entrypoint string for function"""
    return "{} = {}:{}".format(ep, func.__module__, func.__name__)


if __name__ == '__main__':
    setup(
        name=None,
        version=None,
        install_requires=["win10toast>=0.9"],
        author="Valentin Weber",
        author_email="dev@example.com",
        packages=find_packages(),
        include_package_data=True,
        entry_points={
            "console_scripts": []
        }
    )
