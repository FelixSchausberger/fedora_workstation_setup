#!/usr/bin/env python3

from os import getenv
from shlex import split
from shutil import which
from subprocess import run, CalledProcessError, DEVNULL, PIPE

# Terminal color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# Package install commands
PACKAGES = {
    "dnf install -y": [
        "bat",
        "clang-tools-extra",
        "cmake",
        "cronie",
        "exa",
        "fish",
        "fd-find",
        "fzf",
        "gnome-tweaks",
        "util-linux-user",  # For chsh
        "openssl nautilus-python",  # Used for GSConnect
        "python3-pip",
        "rclone",
        "ripgrep",
        # "terminator",
        "tlp tlp-rdw powertop",  # To improve battery life
        "trash-cli",
    ],
    "dnf groupinstall -y": ["'Development Tools'"],
    "flatpak install flathub -y": [
        # "org.blender.Blender",
        "org.gnome.DejaDup",
        # "org.gnome.EasyTAG",
        "com.mattjakeman.ExtensionManager",
        "org.ferdium.Ferdium",
        # "org.freecadweb.FreeCAD",
        "org.gimp.GIMP",
        # "org.jabref.jabref",
        "net.cozic.joplin_desktop",
        "io.neovim.nvim",
        # "com.prusa3d.PrusaSlicer",
        "org.gnome.seahorse.Application",
        "org.gnome.Shotwell",
        "org.videolan.VLC",
    ],
    "curl": [
        "--proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
    ],
    "cargo install": [
        "cargo-cache",  # Cleanup cargo packages
        "cargo-update",  # Update cargo packages
        "erdtree",
        "starship",
        "topgrade",
        "--git https://github.com/typst/typst",
        "zoxide --locked",
    ],
    "pip install": [
        "shell-gpt==0.9.0",
    ],
}


class Installer:
    """
    A class for setting up the system by installing packages.
    """

    def __init__(self):
        """
        Initializes the Installer object.
        """
        self.configure_hostname()
        self.configure_git()
        self.configure_flatpak()
        self.make_eurkey_visible()
        self.configure_surface_linux()
        self.add_game_launchers()
        self.add_dnf_flags()
        self.install_vscode()
        self.install_firacode()

    def add_game_launchers(self):
        """
        Asks user if they want to add game launchers and adds them if they do.
        """
        if input("Do you want to install game launchers? ") == "yes":
            PACKAGES.update({"dnf install -y": ["steam", "lutris", "firejail"]})

    def add_automount_gdrive(self):
        """
        Asks user if they want to automount google drive and does if they do.
        """
        if input("Do you want to automount google drive? ") == "yes":
            # Check if the cron job already exists
            if (
                b"@reboot .local/bin/startup_applications.sh"
                not in run(["crontab", "-l"], stdout=PIPE).stdout
            ):
                # If the cron job doesn't exist, add it
                run(
                    [
                        "echo",
                        "@reboot .local/bin/startup_applications.sh",
                        "|",
                        "crontab",
                        "-",
                    ],
                    stdout=DEVNULL,
                )

    def add_dnf_flags(self):
        """
        Asks user if they want to add some flags to the dnf conf file to speed it up and configures it if they do.
        """
        if input("Do you want to add dnf flags? ") == "yes":
            run(
                split(
                    f"echo max_parallel_downloads=10 | sudo tee -a /etc/dnf/dnf.conf",
                    f"echo fastestmirror=1 | sudo tee -a /etc/dnf/dnf.conf"
                ),
                shell=True,
            )

    def configure_fish(self):
        """
        Asks user if they want to configure fish shell and configures it if they do.
        """
        if input("Do you want to configure fish? ") == "yes":
            fish_user_paths = f"/home/{getenv('USER')}/.local/bin"
            PACKAGES.update(
                {
                    "": [
                        "chsh -s /usr/bin/fish",
                        f"mkdir -p {fish_user_paths}",
                        "fish",
                        f"set -Ua fish_user_paths {fish_user_paths}",
                    ],
                    "curl": [
                        "-sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher",
                    ],
                    "fisher install": [
                        "edc/bass",
                    ],
                }
            )

    def configure_hostname(self):
        """
        Asks user if they want to set a hostname and configures it if they do.
        """
        if input("Do you want to set a hostname? ") == "yes":
            hostname = input("Enter hostname: ")
            PACKAGES.update({"hostnamectl": ["set-hostname " + hostname]})

    def configure_git(self):
        """
        Asks user if they want to configure git and configures it if they do.
        """
        if input("Do you want to configure git? ") == "yes":
            username = input("Enter git user name: ")
            useremail = input("Enter git user email: ")
            PACKAGES.update(
                {
                    "git config --global ": [
                        f"user.name {username}",
                        f"user.email {useremail}",
                        "init.defaultBranch main",
                        "credential.helper store",
                        f"--add safe.directory /home/{getenv('USER')}",
                        "submodule.recurse true",
                    ],
                    "git ": ["config pull.rebase false"],
                }
            )

    def configure_flatpak(self):
        """
        Asks user if they want to configure Flatpak and configures it if they do.
        """
        if input("Do you want to configure Flatpak? ") == "yes":
            PACKAGES.update(
                {
                    "flatpak": [
                        "remote-add --user --if-not-exists",
                        "flathub https://flathub.org/repo/flathub.flatpakrepo",
                    ]
                }
            )

    def install_vscode(self):
        """
        Asks user if they want to install VS Code and installs it if they do.
        """
        if input("Do you want to install VS Code? ") == "yes":
            PACKAGES.update(
                {
                    "": [
                        "sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc",
                        "sudo sh -c 'echo -e \"[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc\" > /etc/yum.repos.d/vscode.repo'",
                        "sudo dnf install code",
                    ]
                }
            )

    def make_eurkey_visible(self):
        """
        Asks user if they want to make EurKEY visible and does it if they do.
        """
        if input("Do you wanna make EurKEY visible in Gnome? ") == ("yes"):
            PACKAGES.update(
                {
                    "gsettings set org.gnome.desktop.input-sources": [
                        "show-all-sources true",
                        "sources \"[('xkb', 'eu')]\"",
                    ]
                }
            )

    def configure_surface_linux(self):
        """
        Asks user if they want to configure surface linux and does it if they do.
        """
        if input("Do you wanna configure surface linux? ") == ("yes"):
            PACKAGES.update(
                {
                    "": [
                        "dnf config-manager --add-repo=https://pkg.surfacelinux.com/fedora/linux-surface.repo",
                        "dnf install --allowerasing kernel-surface iptsd libwacom-surface",
                    ]
                }
            )

    def install_firacode(self):
        """
        Asks user if they want to install and does it if they do.
        """
        if input("Do you wanna install Fira Code? ") == ("yes"):
            PACKAGES.update(
                {
                    "": [
                        "git clone --filter=blob:none --sparse https://github.com/ryanoasis/nerd-fonts ~/.local/share/fonts",
                        "cd ~/.local/share/fonts/nerd-fonts",
                        "git sparse-checkout add patched-fonts/FiraCode",
                        "./install.sh FiraCode",
                    ]
                }
            )

    def run(self):
        """
        Run the install commands.
        """
        for command, packages in PACKAGES.items():
            if which(command.split(" ", 1)[0]):
                for package in packages:
                    print(f"\n{YELLOW}:: {command} {package}{RESET}")
                    try:
                        run(
                            split(f"sudo {command} {package}"),
                            check=True,
                        )
                        print(f"{GREEN}:: Done{RESET}")
                    except CalledProcessError as error:
                        print(
                            f"{RED}:: Command failed with return code {error.returncode}.{RESET}"
                        )

        self.add_automount_gdrive()
        self.configure_fish()

        print(f"{GREEN}\n:: Finished{RESET}")


if __name__ == "__main__":
    Installer().run()
