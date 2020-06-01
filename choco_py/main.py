"""Application for choco-py"""

import subprocess
import sys
from types import FunctionType
from typing import Union

from win10toast import ToastNotifier


NAME = "choco-py"


class ChocoPy:
    """ChocoPy Application.""" 

    def __init__(self):
        
        toaster = ToastNotifier()
        self.toast = toaster.show_toast
        self.error = None
        self.outdated = self._get_outdated()

    def notify(self, text: str, click: FunctionType = None) -> None:
        """Show a choco-py notification"""

        self.toast(  # pylint: disable=unexpected-keyword-arg
            title="Choco Py",
            msg=text,
            icon_path=None,
            callback_on_click=click
        )

    def _get_outdated(self) -> Union[str, None]:
        """Determine number of outdated chocolatey packages."""

        try:
            process = subprocess.run(
                "choco outdated",
                capture_output=True,
                text=True,
                check=True
            )
        
        except FileNotFoundError:  # choco is not installed
            self.error = "Could not locate Chocolatey"
            return

        except subprocess.CalledProcessError as exc:
            self.error = f"'{exc.cmd} exited with code {exc.returncode}"
            return
        
        return process.stdout.splitlines()[-1].strip()


def main():
    """Entrypoint for choco-py."""

    choco = ChocoPy()

    if choco.outdated is None:
        choco.notify(choco.error)
        sys.exit(choco.error)
    
    choco.notify(choco.outdated)


if __name__ == "__main__":
    main()