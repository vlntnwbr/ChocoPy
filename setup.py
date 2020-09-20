"""Setup script."""

import os
import subprocess

from typing import List, Optional, TextIO
from setuptools import find_packages, setup

NAME = "choco-py"
REQUIREMENTS_TXT = "requirements.txt"
HEREDIR = os.path.abspath(os.path.dirname(__file__))


def open_local(filename: str, mode: str = "r") -> TextIO:
    """Open file in this directory."""

    return open(os.path.join(HEREDIR, filename), mode)


def execute_command(args: List[str]) -> List[str]:
    """Execute external command and return stdout"""

    try:
        process = subprocess.run(
            args,
            capture_output=True,
            text=True,
            check=True
        )
        return [line.strip() for line in process.stdout.splitlines()]
    except subprocess.CalledProcessError:
        return []


def create_requirements_txt() -> None:
    """Create file 'requirements.txt' from 'Pipfile.lock'."""

    try:
        with open_local("Pipfile.lock"):
            pass
    except FileNotFoundError:
        return

    pipenv_lines = execute_command(["pipenv", "lock", "-r"])
    if not pipenv_lines:
        return

    reqs = [line for line in pipenv_lines[1:] if line]
    with open_local(REQUIREMENTS_TXT, "w") as req_file:
        req_file.write("\n".join(reqs) + "\n")


def read_requirements() -> List[str]:
    """Read lines of requirements.txt and return them as list"""

    with open_local(REQUIREMENTS_TXT) as req_file:
        return [line.strip() for line in req_file.readlines() if line]


if __name__ == '__main__':
    create_requirements_txt()
    README = "\n".join(open_local("README.md").readlines()[1:])
    REQUIREMENTS = read_requirements()
    setup(
        name=NAME,
        version="0.2.1",
        description="Chocolatey update check and upgrade notification.",
        long_description=README,
        license="GPLv3",
        platforms=["Windows"],
        author="Valentin Weber",
        author_email="vweber@stud.hs-heilbronn.de",
        url="https://github.com/vlntnwbr/chocopy",
        download_url="https://github.com/vlntnwbr/chocopy/archive/master.zip",
        packages=find_packages(),
        install_requires=REQUIREMENTS,
        include_package_data=True,
        entry_points={
            "gui_scripts": [NAME + " = choco_py.main:main"]
        },
        classifiers=[
            "Development Status :: 1 - Planning",
            "Operating System :: Microsoft :: Windows :: Windows 10",
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: English",
            "Topic :: Utilities"
            "Intended Audience :: End Users/Desktop",
            "Intended Audience :: Other Audience",
        ]
    )
