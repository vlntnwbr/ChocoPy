"""Setup script."""

import subprocess

from setuptools import find_packages, setup

NAME = "choco-py"

if __name__ == '__main__':
    setup(
        name=NAME,
        version="0.1.4",
        description="Chocolatey update check and upgrade notification.",
        license="GPLv3",
        platforms=["Windows"],
        author="Valentin Weber",
        author_email="vweber@stud.hs-heilbronn.de",
        url="https://github.com/vlntnwbr/ChocoPy",
        download_url="https://github.com/vlntnwbr/ChocoPy/archive/master.zip",
        packages=find_packages(),
        install_requires=["win10toast>=0.0.9"],
        include_package_data=True,
        entry_points={"console_scripts": [NAME + " = choco_py.main:main"]},
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
