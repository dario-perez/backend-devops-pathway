# 00-Setup

Bootstrap for the shell environment, the `dev` command, and the
automation reference.

## Requirements

- Fedora Linux
- `zsh`
- `git`
- Network access for Oh My Zsh and plugin installation

Optional tools such as Docker, `uv`, `gh`, `gitleaks`, and `terraform` are
detected automatically. Missing tools produce warnings instead of breaking
the shell.

## Install

Clone the repository and run the installer:

```bash
git clone git@github.com:dario-perez/backend-devops-pathway.git
cd backend-devops-pathway/00-setup
./install.sh
exec zsh
The installer:
- symlinks ~/.zshrc to 00-setup/dotfiles/.zshrc
- installs dev into ~/.local/bin/dev
- creates ~/.config/zsh/user_aliases.zsh for local overrides
Verify
dev doctor
All required tool checks should show [OK].
Layout
00-setup/
├── install.sh
├── bin/
│   └── dev
├── dotfiles/
│   ├── .zshrc
│   └── starship.toml
└── docs/
    └── AUTOMATION.md
Common commands
dev help
dev new api payments-api
dev run
dev test
dev lint
dev ship "feat: add payments endpoint"
See docs/AUTOMATION.md for every command, example, environment variable,
and fallback.
```

---