"""Application for choco-py"""

import ctypes
import re
import subprocess
import sys
from typing import Union

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

        outdated = re.findall(r"\b\d+\b", process.stdout.splitlines()[-1])
        return int(outdated[0])

    def notify(self, text: str = None, clickable: bool = True) -> None:
        """Show a choco-py notification"""

        if text is None:
            template = "Chocolatey has determined {} package{} outdated."

            if self.outdated == 1:
                verb = " is"
            else:
                verb = "s are"

            text = template.format(self.outdated, verb)
            if self.outdated > 0:
                text += " Click to upgrade."

        self.toast(
            title="Choco Py",
            msg=text,
            icon_path=None,
            callback_on_click=self.start_upgrade if clickable is True else None
        )


    @staticmethod
    def start_upgrade():
        """Execute choco upgrade with elevated privileges."""

        ctypes.windll.shell32.ShellExecuteW(
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
