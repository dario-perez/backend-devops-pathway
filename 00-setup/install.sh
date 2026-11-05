#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p "$HOME/.local/bin" "$HOME/.config/zsh"

install -m 755 "$ROOT/bin/dev" "$HOME/.local/bin/dev"
ln -sfn "$ROOT/dotfiles/.zshrc" "$HOME/.zshrc"
touch "$HOME/.config/zsh/user_aliases.zsh"

echo "Installed. Open a new shell, then run: dev doctor"