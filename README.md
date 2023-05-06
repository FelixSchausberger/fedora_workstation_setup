# Setup Fedora Workstation

Personal configuration and other convenient files.

## Index

- [Repository overview](repository-overview)
- [First steps](#first-steps)

## Repository overview

```shell
--[ base_folder
    |--[ .config
    |--[ .local
    |--[ Pictures
```

- [.config](.config/): Hosts configuration files for various applications.
- [.local](.local/): Hosts executables and fonts.
- [Pictures](Pictures/): Hosts background and profile pictures.

## First steps

- Follow [this](https://github.com/devangshekhawat/Fedora-38-Post-Install-Guide) guide.
- Prerequisites:

  ```shell
  cd ~
  git init
  git branch -m main
  git remote add origin https://github.com/FelixSchausberger/fedora_workstation_setup
  git fetch
  git pull origin main
  ```
  
- To set up the system:

  ```shell
  .local/bin/system_setup.py
  ```

- To add autologin:

  Edit `/etc/gdm/custom.conf`:

  ```shell
  [daemon]
  AutomaticLoginEnable=true
  AutomaticLogin=fesch
  ```

- To maintain the system:

  ```shell
  topgrade
  ```

- Install Gnome extensions:

  - [Caffeine](https://extensions.gnome.org/extension/517/caffeine/)
  - [Dash to Dock](https://extensions.gnome.org/extension/307/dash-to-dock/)
  - [GSConnect](<https://extensions.gnome.org/extension/1319/gsconnect/>)
  - [Clipboard History](https://extensions.gnome.org/extension/4839/clipboard-history/)
  - [Vitals](https://extensions.gnome.org/extension/1460/vitals/)
