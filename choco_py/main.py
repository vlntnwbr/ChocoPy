"""Application for choco-py"""

import ctypes
import subprocess
import sys
from typing import Union

import win32api
from .win10toast import ToastNotifier


class ChocoPy:
    """ChocoPy Application."""

    def __init__(self):

        toaster = ToastNotifier()
        self.toast = toaster.show_toast
        self.error = None
        self.outdated = self._get_outdated()

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
            return None

        except subprocess.CalledProcessError as exc:
            self.error = f"'{exc.cmd} exited with code {exc.returncode}"
            return None

        return process.stdout.splitlines()[-1].strip()

    def notify(self, text: str = None, click: bool = True) -> None:
        """Show a choco-py notification"""

        msg = "Click to install available updates."
        text = self.outdated + msg if text is None else text
        click = self.start_upgrade if click is True else None

        self.toast(
            title="Choco Py",
            msg=text,
            icon_path=None,
            callback_on_click=click
        )


    @staticmethod
    def start_upgrade():
        """Execute choco upgrade with elevated privileges."""

        win32api.ShellExecute(
            0, "runas", "choco", "upgrade all -y", None, 1
        )


def main():
    """Entrypoint for choco-py."""

    choco = ChocoPy()

    if choco.outdated is None:
        choco.notify(choco.error, False)
        sys.exit(choco.error)

    choco.notify()


if __name__ == "__main__":
    main()
