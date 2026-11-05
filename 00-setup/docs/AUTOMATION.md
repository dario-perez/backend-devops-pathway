# Shell and Dev Automation Reference

This document describes every automation in `00-setup/dotfiles/.zshrc` and
`00-setup/bin/dev`.

## Files and install

| File | Purpose |
| --- | --- |
| `00-setup/dotfiles/.zshrc` | Shell setup, aliases, functions, and hooks. |
| `00-setup/bin/dev` | Unified project and DevOps command runner. |
| `00-setup/dotfiles/starship.toml` | Prompt modules for Python, Docker, Kubernetes, and git. |
| `00-setup/docs/AUTOMATION.md` | This reference, including every automation case. |
| `~/Documents/study/AUTOMATION.pdf` | Personal printable copy; generated outside the repo and not tracked. |
| `~/.zshrc` | Symlink to the repo `.zshrc`. |

Recommended user-local install, which does not require `sudo`:

```bash
repo="${DEV_REPO:-$HOME/Documents/study/backend-devops-pathway}"
mkdir -p "$HOME/.local/bin"
install -m 755 "$repo/00-setup/bin/dev" "$HOME/.local/bin/dev"
ln -sfn "$repo/00-setup/dotfiles/.zshrc" "$HOME/.zshrc"
exec zsh
```

System-wide install, if you prefer `/usr/local/bin`:

```bash
repo="${DEV_REPO:-$HOME/Documents/study/backend-devops-pathway}"
sudo install -m 755 "$repo/00-setup/bin/dev" /usr/local/bin/dev
```

Verify the environment after installing:

```bash
dev doctor
```

Regenerate the personal PDF after editing this document. The PDF lives outside
the repository and is intentionally not committed:

```bash
repo="${DEV_REPO:-$HOME/Documents/study/backend-devops-pathway}"
pandoc "$repo/00-setup/docs/AUTOMATION.md" \
  -o "$HOME/Documents/study/AUTOMATION.pdf" \
  --pdf-engine=typst --toc --number-sections \
  -V fontsize=10pt
```

## Environment variables

These variables can be overridden before starting a shell:

| Variable | Default | Used by |
| --- | --- | --- |
| `DEV_REPO` | `~/Documents/study/backend-devops-pathway` | `.zshrc`, `dev` |
| `PROJECTS_DIR` | `~/Documents/study/projects` | `dev new`, `py-project`, `mkapi` |
| `DEV_LOG` | `$DEV_REPO/docs/worklog.md` | `log`, `today`, `study`, `dev log` |
| `BACKUP_DIR` | `~/Backups` | `backup`, `dev backup` |
| `PYTHON_VERSION` | `3.13` | `dev new`, `dev doctor` |
| `DEV_SKIP_INSTALL` | unset | Set to `1` to skip dependency installs |
| `SKIP_CHECKS` | unset | Set to `1` to skip lint/test in `dev ship` |
| `ZSH_PROFILE` | unset | Set to `1` to profile shell startup |
| `PORT` | `8000` | `dev run` |
| `STARSHIP_CONFIG` | repo `starship.toml` when present | Starship |

The `dev` script also reads `POSTGRES_USER` and `POSTGRES_DB` for database
commands. Both default to `app`.

---

# `.zshrc` automations

## Startup automations

### Oh My Zsh and plugin bootstrap

- Function: Automatically clones Oh My Zsh and the custom plugins when they are
  missing.
- Plugins: `git`, `zsh-autosuggestions`, `zsh-syntax-highlighting`.
- Example: Start a new shell; if `~/.oh-my-zsh` or a plugin is absent, the
  missing pieces are installed first.
- Notes: Requires `git` and network access on the first run.

### History

- Function: Stores 10,000 commands, ignores duplicate entries, appends
  immediately, and shares history between shells.
- Example: Open two terminals and use `history` in either one to see commands
  from both.
- Options: `HIST_IGNORE_ALL_DUPS`, `APPEND_HISTORY`, `INC_APPEND_HISTORY`,
  `SHARE_HISTORY`.

### PATH priority

- Function: Prepends `~/.local/bin` and `~/.opencode/bin` to `PATH`, so
  user-local tools are found before system copies.
- Example: Install `dev` in `~/.local/bin` and it overrides
  `/usr/local/bin/dev`.
- Notes: No `sudo` is needed for tools installed in `~/.local/bin`.

### Startup profiler

- Function: `zprof-start` starts an interactive shell with `zprof` enabled and
  prints the startup profile.
- Example:

```bash
zprof-start
```

- Notes: Profiles only the startup path. Use it if shell startup becomes slow.

### `cd` with directory listing

- Function: Every `cd` runs `ls` afterward.
- Example:

```bash
cd ~/Documents/study
```

- Notes: The function uses `builtin cd`, so it does not recurse.

### Auto-activate Python virtual environments

- Function: `_auto_venv` runs on every directory change, searches upward for
  `.venv/bin/activate` or `venv/bin/activate`, activates it, and deactivates it
  when leaving the project.
- Example:

```bash
cd ~/Documents/study/projects/payments
# [venv] activated: payments

cd ~/Documents/study
# [venv] deactivated
```

- Notes: Works with both `.venv` and `venv`. If `direnv` is installed, its hook
  is also loaded.

### FZF shell integration

- Function: Loads `fzf --zsh` when `fzf` is installed, enabling fuzzy history,
  file, and directory widgets.
- Example: Press `Ctrl-R` for history search, `Ctrl-T` to pick files, or
  `Alt-C` to change directory.
- Notes: The binding is provided by your installed `fzf` version.

### direnv hook

- Function: Loads the `direnv` hook when available, so directory-specific
  `.envrc` files are applied on `cd`.
- Example:

```bash
cd ~/Documents/study/projects/payments-api
echo 'export API_ENV=local' > .envrc
direnv allow
```

- Notes: The built-in `.venv` hook still works when `direnv` is absent.

### Starship prompt modules

- Function: Loads `00-setup/dotfiles/starship.toml` and shows
  username/hostname on SSH, directory, git branch/status, Python virtualenv,
  Docker context, Kubernetes context, and command duration.
- Example: Enter a project with an active venv and a git repository; the prompt
  shows the `py` and git modules.
- Notes: Set `STARSHIP_CONFIG` to override the file.

### zoxide directory jumping

- Function: Loads `zoxide init zsh` when `zoxide` is installed.
- Example:

```bash
z backend
z study
```

- Notes: `zoxide` learns directories as you visit them. Without it, use normal
  `cd`.

### NVM loading

- Function: Sources `$NVM_DIR/nvm.sh` and the NVM bash completion file when
  they exist.
- Example:

```bash
nvm use 20
nvm ls
```

- Notes: This loads an existing NVM installation; it does not install NVM.

### Welcome and system summary

- Function: Prints a welcome banner and runs `fastfetch` in interactive shells.
- Example: Open a terminal.
- Notes: Both are guarded by interactive checks.

### User aliases

- Function: Sources `~/.config/zsh/user_aliases.zsh` last, so local overrides win.
- Example: Add `alias ll='eza -al'` to that file and open a new shell.
- Notes: The file is optional.

## Navigation and process controls

### `mkcd`

- Function: Creates a directory and enters it.
- Example:

```bash
mkcd ~/Documents/study/projects/new-service
```

### `fkill`

- Function: Uses `fzf` to select a process by CPU usage and sends `SIGTERM`.
- Example:

```bash
fkill
```

- Notes: Requires `fzf`.

### `ports`

- Function: Shows listening TCP/UDP ports with process information.
- Example:

```bash
ports
```

### `killport`

- Function: Finds the process listening on a port and sends `SIGTERM`.
- Example:

```bash
killport 8000
```

- Notes: Useful when a FastAPI reload leaves a stale process behind.

## Logging, backup, and diagnostics

### `log`

- Function: Appends a timestamped entry to the daily work log.
- Example:

```bash
log "Finished the FastAPI CRUD exercise"
```

- Output: `$DEV_LOG` (default `docs/worklog.md`), grouped under `## YYYY-MM-DD`.

### `today`

- Function: Prints today's section of the work log.
- Example:

```bash
today
```

### `backup`

- Function: Archives `~/Documents/study`, `~/.config/zsh`, the Starship config,
  and `~/.zshrc` into `$BACKUP_DIR`.
- Example:

```bash
backup
```

- Output: `~/Backups/study-YYYYMMDD-HHMMSS.tar.zst` (or `.tar.gz` without
  `zstd`).
- Retention: Keeps the 10 newest `study-*` archives.

### `doctor`

- Function: Calls `dev doctor`; falls back to basic tool checks if `dev` is not
  installed.
- Example:

```bash
doctor
```

## Git helpers

### `gclone`

- Function: Clones a repository and enters it. Accepts a URL or `owner/repo`.
- Example:

```bash
gclone dario-perez/backend-devops-pathway
gclone git@github.com:dario-perez/backend-devops-pathway.git
```

### `gscan`

- Function: Scans the current tree for secrets. Uses `gitleaks`, then
  `trufflehog`, then a ripgrep pattern fallback.
- Example:

```bash
gscan
```

- Detects: AWS access key IDs, GitHub tokens, OpenAI-style keys, and private key
  headers.
- Exit code: `1` when a potential secret is found.

## Focus and services

### `study`

- Function: Runs a focus timer, sends a desktop notification, and logs the
  session.
- Example:

```bash
study
study 50
```

- Default: 25 minutes.
- Notes: Uses `notify-send` when available.

### `serve`

- Function: Serves the current directory over HTTP and picks the next free port.
- Example:

```bash
serve
serve 8080
```

### `ssh-load`

- Function: Starts `ssh-agent` if needed and loads `~/.ssh/id_ed25519`.
- Example:

```bash
ssh-load
ssh-load ~/.ssh/work_key
```

- Notes: Does not run automatically, so passphrase prompts stay explicit.

## Docker helpers

### `dps`

- Function: Shows a compact table of running containers.
- Example:

```bash
dps
```

### `dlogs`

- Function: Follows the last 100 log lines of a container.
- Example:

```bash
dlogs payments-api
```

### `dclean`

- Function: Shows Docker disk usage and asks before pruning stopped containers,
  unused networks, dangling images, and build cache.
- Example:

```bash
dclean
```

- Notes: Does not prune volumes.

## Project generators

### `py-project`

- Function: Delegates to `dev new python`.
- Example:

```bash
py-project inventory-cli
```

### `mkapi`

- Function: Delegates to `dev new api`.
- Example:

```bash
mkapi payments-api
```

## Git save and health

### `gsave`

- Function: Adds all changes, commits with a message, and pushes.
- Example:

```bash
gsave "feat: add inventory endpoint"
```

### `health-check`

- Function: Prints RAM, CPU load, and root disk usage with warning thresholds.
- Example:

```bash
health-check
```

### `show-help`

- Function: Prints the shell command reference.
- Example:

```bash
show-help
```

## Short aliases

| Alias | Expands to | Example |
| --- | --- | --- |
| `workspace` | `cd ~/Documents/study` | `workspace` |
| `pathway` | `cd ~/Documents/study/backend-devops-pathway` | `pathway` |
| `study-projects` | `cd ~/Documents/study/projects` | `study-projects` |
| `vsc` | `code .` | `vsc` |
| `d` | `docker` | `d ps` |
| `dc` | `docker compose` | `dc up -d` |
| `gst` | `git status` | `gst` |
| `gcm` | `git commit -m` | `gcm "docs: update setup notes"` |
| `update` | `sudo dnf upgrade --refresh -y` | `update` |
| `update-all` | dnf upgrade, autoremove, and flatpak update | `update-all` |
| `c` | `clear` | `c` |
| `emergency` | `nano ~/.zshrc` | `emergency` |
| `loadzsh` | `source ~/.zshrc` | `loadzsh` |
| `health` | Quick RAM and disk summary | `health` |

Example session:

```bash
workspace
pathway
study-projects
vsc
d ps
dc up -d
gst
gcm "docs: update setup notes"
update
update-all
health
c
emergency
loadzsh
```

---

# `dev` automations

## Project creation

### `dev new python <name>`

- Function: Creates a Python project in `$PROJECTS_DIR/<name>` with `.venv`,
  `app/`, `tests/`, `pyproject.toml`, `requirements-dev.txt`, `.gitignore`,
  README, and an initial git commit.
- Example:

```bash
dev new python inventory-cli
```

- Python selection: `uv` with 3.13, then `python3.13`, then `python3`.
- Skip installs: `DEV_SKIP_INSTALL=1 dev new python inventory-cli`.

### `dev new api <name>`

- Function: Creates a FastAPI project with a working `/`, `/health`, and
  `/items` API, SQLAlchemy, Postgres compose service, Dockerfile, tests, ruff,
  pre-commit, and GitHub Actions.
- Example:

```bash
dev new api payments-api
```

- Generated layout:

```text
payments-api/
├── app/
│   ├── config.py
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── tests/test_health.py
├── .github/workflows/ci.yml
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── Dockerfile
├── Makefile
├── README.md
├── compose.yaml
├── pyproject.toml
├── requirements.txt
└── requirements-dev.txt
```

- Skip installs: `DEV_SKIP_INSTALL=1 dev new api payments-api`.

## Project setup

### `dev init [dir]`

- Function: Adds git, `.gitignore`, README, `.env.example`, and a pre-commit
  config to an existing directory. Installs the pre-commit hook when available
  and creates an initial commit if the repository has no commits.
- Example:

```bash
dev init .
dev init ~/Documents/study/projects/legacy-service
```

## Run and quality

### `dev run [dir]`

- Function: Activates the project venv, creating one if needed, then runs
  `uvicorn app.main:app --reload` for FastAPI projects, `python -m app.main`
  for plain Python apps, or `python main.py`.
- Example:

```bash
dev run
dev run ~/Documents/study/projects/payments-api
PORT=8080 dev run
```

### `dev test [dir]`

- Function: Runs `pytest -q` inside the project venv. Falls back to
  `uv run pytest -q` when needed.
- Example:

```bash
dev test
```

### `dev lint [dir]`

- Function: Runs `ruff check .` inside the project venv.
- Example:

```bash
dev lint
```

### `dev fmt [dir]`

- Function: Runs `ruff format .`, with `black` as a fallback.
- Example:

```bash
dev fmt
```

## Docker

### `dev up [dir]`

- Function: Runs `docker compose up -d --build` and prints service status.
- Example:

```bash
dev up
```

### `dev down [dir]`

- Function: Runs `docker compose down`.
- Example:

```bash
dev down
```

### `dev db [dir]`

- Function: Starts the `db` compose service and waits up to 60 seconds for
  `pg_isready`.
- Example:

```bash
dev db
```

## Git workflow

### `dev ship [message]`

- Function: Runs lint and tests, commits all changes, pushes the branch, and
  creates a PR with `gh` when on a feature branch.
- Example:

```bash
dev ship "feat: add payments endpoint"
SKIP_CHECKS=1 dev ship "chore: update docs"
```

- Notes: Does not create a PR from `main` or `master`.

### `dev status [dir]`

- Function: Shows `git status`, branch, upstream ahead/behind counts, the last
  commit, and PR status when `gh` is available.
- Example:

```bash
dev status
```

### `dev save <message>`

- Function: Adds all changes, commits, and pushes. This is the older, simpler
  save path kept for compatibility.
- Example:

```bash
dev save "fix: correct health check"
```

## Maintenance

### `dev clean [dir]`

- Function: Removes `__pycache__`, `.pytest_cache`, `.ruff_cache`,
  `.mypy_cache`, `.pyc` files, build output, coverage output, and optionally the
  venv or dangling Docker images.
- Example:

```bash
dev clean
dev clean -y
dev clean -y --venv --docker
```

- Flags: `-y/--yes`, `--venv`, `--docker`.

### `dev doctor`

- Function: Checks installed tools and versions, Docker daemon access, GitHub
  authentication, failed systemd units, disk usage, and configured paths.
- Tool checks: `git`, `python3`, `python3.13`, `uv`, `docker`,
  `docker compose`, `gh`, `ruff`, `pytest`, `pre-commit`, `gitleaks`, `jq`,
  `kubectl`, `terraform`, and `ansible`.
- Example:

```bash
dev doctor
```

- Notes: Tool checks print `[OK]` or `[MISS]`; Docker, GitHub, and systemd
  checks are reported separately. A missing optional tool does not stop `dev`.

### `dev secrets [dir]`

- Function: Scans for secrets with `gitleaks`, then `trufflehog`, then a
  ripgrep pattern fallback.
- Example:

```bash
dev secrets
dev secrets ~/Documents/study/projects/payments-api
```

- Exit code: `1` when a potential secret is found.

### `dev backup [dir]`

- Function: Dumps the compose Postgres database when it is running; otherwise
  archives the project excluding `.venv`, `venv`, `__pycache__`, `.git`, and
  `node_modules`.
- Example:

```bash
dev backup
dev backup ~/Documents/study/projects/payments-api
```

- Output: `$BACKUP_DIR/db-YYYYMMDD-HHMMSS.sql` or
  `$BACKUP_DIR/<project>-YYYYMMDD-HHMMSS.tar.zst`.
- Retention: Keeps the 10 newest backups.

## Logging and roadmap

### `dev log <message>`

- Function: Appends a timestamped entry to the shared work log.
- Example:

```bash
dev log "Researched Docker healthchecks"
```

### `dev roadmap`

- Function: Reads `README.md` and prints the learning milestones plus unchecked
  items.
- Example:

```bash
dev roadmap
```

## Health and help

### `dev health`

- Function: Prints RAM, CPU load, and disk usage with warning thresholds.
- Example:

```bash
dev health
```

### `dev help`

- Function: Prints the full command reference.
- Example:

```bash
dev help
```

---

# Common workflows

## New API from zero to running

```bash
dev new api payments-api
cd ~/Documents/study/projects/payments-api
dev run
```

In another terminal:

```bash
dev test
dev lint
```

With Docker:

```bash
dev up
curl http://127.0.0.1:8000/health
dev down
```

## Daily study loop

```bash
log "Started the Linux administration milestone"
study 50
log "Finished the Linux milestone"
today
dev roadmap
```

## Safe commit and push

```bash
dev secrets
dev test
dev lint
dev ship "feat: add inventory endpoint"
```

## Backup before risky work

```bash
backup
dev backup ~/Documents/study/projects/payments-api
```

## Debug a busy port

```bash
ports
killport 8000
dev run
```

## Weekly maintenance

```bash
update-all
doctor
dev clean -y --docker
backup
```

---

# Optional tools and fallbacks

| Tool | Used for | Fallback |
| --- | --- | --- |
| `uv` | Fast venv and dependency installs | `python3 -m venv` + `pip` |
| `python3.13` | Target Python version | `python3` with a warning |
| `direnv` | Per-directory environment loading | Built-in `.venv` hook |
| `gitleaks` | Secret scanning | `trufflehog`, then `rg` |
| `trufflehog` | Secret scanning | `rg` |
| `gh` | PR creation and status | Manual push; `git` output only |
| `terraform` | Infrastructure checks in `dev doctor` | Reported as `[MISS]` |
| `ansible` | Configuration checks in `dev doctor` | Reported as `[MISS]` |
| `starship` | Prompt modules | Basic shell prompt |
| `fastfetch` | Welcome system summary | Banner only |
| `zstd` | Faster backups | `.tar.gz` |
| `fzf` | `fkill` and shell history widgets | `fkill` is disabled |
| `notify-send` | Focus timer notification | No notification; log still written |
| `zoxide` | `z` directory jumps | Normal `cd` |
| `pandoc` + `typst` | Regenerating the personal PDF outside the repo | Markdown remains the source of truth |

# Notes

- `~/.zshrc` is a symlink to this repository. Editing it changes the repository
  working tree.
- Commit shell and `dev` changes after reviewing `git diff`.
- The **API generator creates projects outside the curriculum repository** in
  `~/Documents/study/projects` by default.
- The log file is created on first use; it does not need to exist beforehand.
