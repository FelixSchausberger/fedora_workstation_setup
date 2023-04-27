#!/usr/bin/env python3

import shutil
import subprocess

# Terminal color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


class Formatter:
    def __init__(self):
        self.tools = [
            ("python3 -m black", ["py"]),
            ("clang-format -i -style=file $file", ["c", "h", "cpp", "hpp"]),
        ]
        self.exclude = [".local/bin/clustergit"]

    def check_commands(self):
        """Check if required commands are available in the system"""
        commands = ["black", "clang-format", "fd"]
        for cmd in commands:
            if not shutil.which(cmd):
                print(f"{RED}:: Error: '{cmd}' not found.{RESET}")
                return False
        return True

    def run_tools(self):
        """Run formatting tools on files"""

        for command, file_suffix in self.tools:
            file_suffix_str = (
                f"-e {' -e '.join(file_suffix)}"
                if len(file_suffix) > 1
                else f"-e {file_suffix[0]}"
            )
            exclude_str = f"-E {' -E '.join(self.exclude)}" if self.exclude else ""
            file_list = (
                subprocess.check_output(
                    f"fd {file_suffix_str} {exclude_str}",
                    shell=True,
                    executable="/bin/bash",
                )
                .decode("utf-8")
                .splitlines()
            )

            if file_list:
                try:
                    subprocess.run(
                        f"fd {file_suffix_str} {exclude_str} -X {command}",
                        shell=True,
                        check=True,
                        executable="/bin/bash",
                    )
                except subprocess.CalledProcessError as error:
                    print(
                        f"{RED}:: Command failed with return code {error.returncode}.{RESET}"
                    )
            else:
                print(
                    f"\n{YELLOW}:: No *.{', *.'.join(file_suffix)} files found.{RESET}"
                )

    def run(self):
        if not self.check_commands():
            exit(1)

        self.run_tools()

        print(f"\n{GREEN}:: Finished{RESET}")


if __name__ == "__main__":
    Formatter().run()
