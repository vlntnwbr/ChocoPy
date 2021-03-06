# ChocoPy ![](https://github.com/vlntnwbr/chocopy/workflows/Tests/badge.svg)

ChocoPy is a helper tool for the Windows package manager [Chocolatey][1]. It
generates a notification displaying the number of updatable packages that can
initiate the upgrade process when clicked.

## Installation
Installing with [pipx][1] isolates packages in their own environment and
exposes their entrypoints on PATH.
```
pipx install https://github.com/vlntnwbr/choco-py/releases/latest/download/choco-py.tar.gz
```
Alternatively install with pip: 
```
pip install https://github.com/vlntnwbr/choco-py/releases/latest/download/choco-py.tar.gz
```

## Credits
This project includes a file from [win10toast][2] that has been modified by
user [CharnelX][3] to include a click handler. The modified project was 
published under the MIT License and can be found [here][4].

The included icon is part of the [Demo 3D Food Icon Set][5] by [icons-land][6]
published under their [Demo License][7].

[1]: https://chocolatey.org/
[2]: https://pypi.org/project/win10toast/
[3]: https://github.com/Charnelx
[4]: https://github.com/Charnelx/Windows-10-Toast-Notifications

[5]: http://www.icons-land.com/3d-food-png-icons.php
[6]: http://www.icons-land.com
[7]: http://www.icons-land.com/license-agreements.php#DemoLicenseAgreement
