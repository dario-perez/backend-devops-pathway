# =========================================================
# OPTIONAL STARTUP PROFILING
# =========================================================
if [[ -n "${ZSH_PROFILE:-}" ]]; then
    zmodload zsh/zprof
fi

# =========================================================
# OH MY ZSH
# =========================================================
export ZSH="$HOME/.oh-my-zsh"
ZSH_CUSTOM="$ZSH/custom"
ZSH_THEME="robbyrussell"

# Install Oh My Zsh and plugins if missing
if [ ! -d "$ZSH" ]; then
  echo "Installing Oh-My-Zsh..."
  git clone https://github.com/ohmyzsh/ohmyzsh.git "$ZSH" >/dev/null 2>&1
fi

if [ ! -d "$ZSH_CUSTOM/plugins/zsh-autosuggestions" ]; then
  echo "Installing zsh-autosuggestions..."
  git clone https://github.com/zsh-users/zsh-autosuggestions "$ZSH_CUSTOM/plugins/zsh-autosuggestions" >/dev/null 2>&1
fi

if [ ! -d "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting" ]; then
  echo "Installing zsh-syntax-highlighting..."
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting" >/dev/null 2>&1
fi

plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

# History
HISTFILE="$HOME/.zsh_history"
HISTSIZE=10000
SAVEHIST=10000
setopt HIST_IGNORE_ALL_DUPS
setopt APPEND_HISTORY
setopt INC_APPEND_HISTORY
setopt SHARE_HISTORY

# =========================================================
# PATHS
# =========================================================
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.opencode/bin:$PATH"

export DEV_REPO="${DEV_REPO:-$HOME/Documents/study/backend-devops-pathway}"
export PROJECTS_DIR="${PROJECTS_DIR:-$HOME/Documents/study/projects}"
export DEV_LOG="${DEV_LOG:-$DEV_REPO/docs/worklog.md}"
export BACKUP_DIR="${BACKUP_DIR:-$HOME/Backups}"

# =========================================================
# ZOXIDE
# =========================================================
if command -v zoxide >/dev/null 2>&1 && [ -x "$(command -v zoxide)" ]; then
    eval "$(zoxide init zsh)"
fi

# cd also lists directory contents
cd() {
    builtin cd "$@" && ls
}

# Auto-activate the nearest .venv or venv when entering a project
_auto_venv() {
    local dir="$PWD"
    local venv=""

    while [[ -n "$dir" ]]; do
        if [[ -f "$dir/.venv/bin/activate" ]]; then
            venv="$dir/.venv"
            break
        fi
        if [[ -f "$dir/venv/bin/activate" ]]; then
            venv="$dir/venv"
            break
        fi
        [[ "$dir" == "/" ]] && break
        dir="${dir:h}"
    done

    if [[ -n "$venv" ]]; then
        if [[ "${VIRTUAL_ENV:-}" != "$venv" ]]; then
            if (( $+functions[deactivate] )); then
                deactivate
            elif [[ -n "${VIRTUAL_ENV:-}" ]]; then
                unset VIRTUAL_ENV
            fi
            source "$venv/bin/activate"
            echo "[venv] activated: ${venv:h:t}"
        fi
    elif [[ -n "${VIRTUAL_ENV:-}" ]]; then
        if (( $+functions[deactivate] )); then
            deactivate
        else
            unset VIRTUAL_ENV
        fi
        echo "[venv] deactivated"
    fi
}

autoload -Uz add-zsh-hook
add-zsh-hook chpwd _auto_venv
_auto_venv

# =========================================================
# FZF
# =========================================================
if command -v fzf >/dev/null 2>&1; then
    source <(fzf --zsh)
fi

# =========================================================
# DIRENV
# =========================================================
if command -v direnv >/dev/null 2>&1; then
    eval "$(direnv hook zsh)"
fi

# =========================================================
# STARSHIP
# =========================================================
if [[ -f "$DEV_REPO/setup/dotfiles/starship.toml" ]]; then
    export STARSHIP_CONFIG="$DEV_REPO/setup/dotfiles/starship.toml"
fi

if command -v starship >/dev/null 2>&1 && [ -x "$(command -v starship)" ]; then
    eval "$(starship init zsh)"
fi

# =========================================================
# NVM
# =========================================================
export NVM_DIR="$HOME/.nvm"

[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# =========================================================
# WELCOME MESSAGE
# =========================================================
if [[ -o interactive ]]; then
    echo "──────────────────────────────────────────────────"
    echo "  🚀 Hello, Dario!"
    echo "  📅 $(date +'%A, %B %d - %Y')"
    echo "  📂 Directory: $(pwd)"
    echo "──────────────────────────────────────────────────"
fi

# =========================================================
# FASTFETCH
# =========================================================
if [[ -o interactive ]] && command -v fastfetch >/dev/null 2>&1; then
    fastfetch
fi

# =========================================================
# EMERGENCY / RELOAD
# =========================================================
alias emergency='nano ~/.zshrc'
alias loadzsh='source ~/.zshrc'

# =========================================================
# SYSTEM
# =========================================================
alias update='sudo dnf upgrade --refresh -y'
alias update-all='sudo dnf upgrade --refresh -y && sudo dnf autoremove -y && flatpak update -y'

alias c='clear'

alias health="echo 'Memory:'; free -h | grep Mem; echo 'Disk:'; df -h / | grep /"

# =========================================================
# WORKSPACE
# =========================================================
alias workspace='cd ~/Documents/study'
alias pathway='cd ~/Documents/study/backend-devops-pathway'
alias study-projects='cd ~/Documents/study/projects'

# =========================================================
# DEVELOPMENT
# =========================================================
alias vsc='code .'

# Docker
alias d='docker'
alias dc='docker compose'

# Git
alias gst='git status'
alias gcm='git commit -m'

# =========================================================
# NAVIGATION HELPERS
# =========================================================
mkcd() {
    if [[ $# -eq 0 ]]; then
        echo "Usage: mkcd <directory>"
        return 1
    fi
    mkdir -p "$1" && cd "$1"
}

fkill() {
    if ! command -v fzf >/dev/null 2>&1; then
        echo "fzf is required for fkill"
        return 1
    fi

    local pid
    pid=$(ps -eo pid,comm,args --sort=-%cpu |
        fzf --header='Select a process to terminate' \
            --preview 'ps -p {1} -o pid,comm,args' |
        awk '{print $1}')

    if [[ -z "$pid" ]]; then
        echo "No process selected"
        return 1
    fi

    kill -TERM "$pid" && echo "Sent TERM to PID $pid"
}

ports() {
    if command -v ss >/dev/null 2>&1; then
        ss -tulpn
    else
        netstat -tulpn
    fi
}

killport() {
    local port="${1:-}"
    if [[ -z "$port" ]]; then
        echo "Usage: killport <port>"
        return 1
    fi

    local pid
    pid=$(ss -tulpn "sport = :$port" 2>/dev/null |
        sed -n 's/.*pid=\([0-9]*\).*/\1/p' |
        head -n 1)

    if [[ -z "$pid" ]]; then
        echo "No process found on port $port"
        return 1
    fi

    kill -TERM "$pid" && echo "Sent TERM to PID $pid on port $port"
}

# =========================================================
# LOGGING / BACKUP / DOCTOR
# =========================================================
log() {
    if [[ $# -eq 0 ]]; then
        echo "Usage: log <message>"
        return 1
    fi

    local file="${DEV_LOG:-$DEV_REPO/docs/worklog.md}"
    mkdir -p "${file:h}"

    local day
    day=$(date +%F)
    grep -q "^## ${day}$" "$file" 2>/dev/null ||
        printf '\n## %s\n\n' "$day" >> "$file"

    printf -- '- **%s** - %s\n' "$(date +%H:%M)" "$*" >> "$file"
    echo "Logged to $file"
}

today() {
    local file="${DEV_LOG:-$DEV_REPO/docs/worklog.md}"
    if [[ ! -f "$file" ]]; then
        echo "No log yet: $file"
        return 0
    fi

    local day
    day="## $(date +%F)"
    awk -v day="$day" '$0 == day { show=1; print; next } /^## / { show=0 } show' "$file"
}

backup() {
    local dest="${BACKUP_DIR:-$HOME/Backups}"
    local stamp
    stamp=$(date +%Y%m%d-%H%M%S)

    local ext="tar.zst"
    local -a tar_opts=(--zstd -cf)
    if ! command -v zstd >/dev/null 2>&1; then
        ext="tar.gz"
        tar_opts=(-czf)
    fi

    local archive="$dest/study-$stamp.$ext"
    mkdir -p "$dest"

    local -a paths=(Documents/study)
    [[ -d "$HOME/.config/zsh" ]] && paths+=(.config/zsh)
    [[ -f "$HOME/.config/starship.toml" ]] && paths+=(.config/starship.toml)
    [[ -e "$HOME/.zshrc" ]] && paths+=(.zshrc)

    tar "${tar_opts[@]}" "$archive" -C "$HOME" "${paths[@]}" 2>/dev/null

    if [[ -f "$archive" ]]; then
        echo "Backup created: $archive"
        ls -1t "$dest"/study-*.$ext 2>/dev/null |
            tail -n +11 |
            xargs -r rm --
    else
        echo "Backup failed"
        return 1
    fi
}

doctor() {
    if command -v dev >/dev/null 2>&1; then
        dev doctor
        return
    fi

    echo "dev is not installed; basic checks:"
    local cmd
    for cmd in git python3 docker zsh starship fzf; do
        if command -v "$cmd" >/dev/null 2>&1; then
            printf '  [OK]   %s\n' "$cmd"
        else
            printf '  [MISS] %s\n' "$cmd"
        fi
    done
}

# =========================================================
# GIT HELPERS
# =========================================================
gclone() {
    if [[ $# -eq 0 ]]; then
        echo "Usage: gclone <url|owner/repo> [directory]"
        return 1
    fi

    local url="$1"
    local dir="${2:-}"

    if [[ "$url" =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]]; then
        url="https://github.com/$url.git"
    fi

    [[ -z "$dir" ]] && dir="${${url##*/}%.git}"
    git clone "$url" "$dir" && cd "$dir"
}

gscan() {
    if command -v gitleaks >/dev/null 2>&1; then
        gitleaks detect --source . --no-git --redact -v
    elif command -v trufflehog >/dev/null 2>&1; then
        trufflehog filesystem . --no-update
    elif command -v rg >/dev/null 2>&1; then
        if rg -n --hidden \
            -g '!.git/**' -g '!node_modules/**' -g '!.venv/**' \
            -e 'AKIA[0-9A-Z]{16}' \
            -e 'ghp_[A-Za-z0-9]{36}' \
            -e 'sk-[A-Za-z0-9]{20,}' \
            -e '-----BEGIN (RSA|OPENSSH|EC) PRIVATE KEY-----' .; then
            echo "Potential secrets found"
            return 1
        fi
        echo "No obvious secrets found"
    else
        echo "Install gitleaks or ripgrep to scan for secrets"
        return 1
    fi
}

# =========================================================
# FOCUS / SERVE / DOCKER / SSH
# =========================================================
study() {
    local minutes="${1:-25}"
    if ! [[ "$minutes" =~ ^[0-9]+$ ]]; then
        echo "Usage: study [minutes]"
        return 1
    fi

    echo "Focus session started: ${minutes} min (Ctrl-C to stop)"
    sleep $((minutes * 60))

    if command -v notify-send >/dev/null 2>&1; then
        notify-send "Study session complete" "${minutes} minutes finished" 2>/dev/null
    fi

    log "Focus session: ${minutes} min"
    echo "Focus session complete."
}

serve() {
    local port="${1:-8000}"
    if ! [[ "$port" =~ ^[0-9]+$ ]]; then
        echo "Usage: serve [port]"
        return 1
    fi

    if command -v ss >/dev/null 2>&1; then
        while ss -ltn "sport = :$port" 2>/dev/null | grep -q LISTEN; do
            port=$((port + 1))
        done
    fi

    echo "Serving $PWD at http://127.0.0.1:$port"
    python3 -m http.server "$port" --bind 127.0.0.1
}

dps() {
    docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
}

dlogs() {
    if [[ -z "${1:-}" ]]; then
        echo "Usage: dlogs <container>"
        return 1
    fi
    docker logs --tail 100 -f "$1"
}

dclean() {
    if ! command -v docker >/dev/null 2>&1; then
        echo "docker is not installed"
        return 1
    fi

    docker system df

    local reply
    read -q "reply?Prune stopped containers, unused networks, dangling images, and build cache? [y/N] "
    echo

    if [[ "$reply" == [yY] ]]; then
        docker system prune -f
    else
        echo "Cancelled"
    fi
}

ssh-load() {
    local key="${1:-$HOME/.ssh/id_ed25519}"

    if [[ -z "${SSH_AUTH_SOCK:-}" ]]; then
        eval "$(ssh-agent -s)" >/dev/null
    else
        ssh-add -l >/dev/null 2>&1
        if (( $? == 2 )); then
            eval "$(ssh-agent -s)" >/dev/null
        fi
    fi

    if ssh-add -l >/dev/null 2>&1; then
        echo "ssh-agent already has identities"
        ssh-add -l
        return 0
    fi

    if [[ ! -f "$key" ]]; then
        echo "SSH key not found: $key"
        return 1
    fi

    ssh-add "$key"
}

zprof-start() {
    ZSH_PROFILE=1 zsh -i -c 'exit'
}

# =========================================================
# LOCAL PROJECT SCRIPTS
# =========================================================

# ---------------------------------------------------------
# Python project generator
# ---------------------------------------------------------
py-project() {
    if command -v dev >/dev/null 2>&1; then
        dev new python "$@"
    else
        echo "dev is not installed. Run the setup install step first."
        return 1
    fi
}

# ---------------------------------------------------------
# FastAPI project generator
# ---------------------------------------------------------
mkapi() {
    if command -v dev >/dev/null 2>&1; then
        dev new api "$@"
    else
        echo "dev is not installed. Run the setup install step first."
        return 1
    fi
}

# =========================================================
# GITHUB SAVE
# =========================================================
gsave() {
    if [ -z "$1" ]; then
        echo "Usage: gsave 'commit message'"
        return 1
    fi

    if git diff --quiet && git diff --cached --quiet; then
        echo "No changes to commit"
        return 0
    fi

    git add .

    if ! git commit -m "$1"; then
        echo "Commit failed"
        return 1
    fi

    local branch
    branch=$(git branch --show-current)

    if ! git push 2>/dev/null; then
        git push -u origin "$branch"
    fi

    echo "Changes pushed"
}

# =========================================================
# OBSERVABILITY
# =========================================================
health-check() {
    ram_usage=$(free | awk '/Mem:/ {print int($3/$2 * 100)}')

    cpu_load=$(awk '{print $1}' /proc/loadavg)
    cpu_cores=$(nproc)

    cpu_usage=$(awk -v sys_load="$cpu_load" -v cores="$cpu_cores" 'BEGIN {print int((sys_load/cores)*100)}')

    disk_usage=$(df / | awk 'END {print int($5)}')

    echo "──────────────────────────────────────────────────"
    echo "SYSTEM HEALTH REPORT | $(date +'%B %d - %Y | %H:%M:%S')"
    echo "──────────────────────────────────────────────────"

    print_status() {
        local label=$1
        local value=$2

        if [ "$value" -ge 80 ]; then
            echo -e "$label: \e[31m$value%\e[0m (CRITICAL)"
        elif [ "$value" -ge 70 ]; then
            echo -e "$label: \e[33m$value%\e[0m (WARNING)"
        else
            echo -e "$label: \e[32m$value%\e[0m (OK)"
        fi
    }

    print_status "RAM" "$ram_usage"
    print_status "CPU" "$cpu_usage"
    print_status "Disk" "$disk_usage"

    echo "──────────────────────────────────────────────────"
}

# =========================================================
# HELP
# =========================================================
show-help() {
    echo ""
    echo "══════════════════════════════════════════════════"
    echo "                DARIO DEV TOOLKIT"
    echo "══════════════════════════════════════════════════"
    echo ""

    echo "WORKSPACE"
    echo "  workspace       -> Go to ~/Documents/study"
    echo "  pathway         -> Go to backend-devops-pathway"
    echo "  study-projects  -> Go to generated projects"
    echo "  mkcd <dir>      -> Create and enter a directory"
    echo ""

    echo "NAVIGATION / PROCESSES"
    echo "  z <dir>         -> zoxide jump"
    echo "  fkill           -> Fuzzy select a process to terminate"
    echo "  ports           -> Show listening ports"
    echo "  killport <port> -> Kill the process on a port"
    echo ""

    echo "LOGGING / BACKUP"
    echo "  log <message>   -> Append a timestamped work log entry"
    echo "  today           -> Show today's work log"
    echo "  backup          -> Archive study files and dotfiles"
    echo "  doctor          -> Run dev doctor"
    echo ""

    echo "GIT"
    echo "  gst             -> git status"
    echo "  gcm             -> git commit -m"
    echo "  gsave           -> add/commit/push automation"
    echo "  gclone <repo>   -> Clone and enter a repository"
    echo "  gscan           -> Scan the tree for secrets"
    echo ""

    echo "FOCUS / SERVICES"
    echo "  study [min]     -> Focus timer (default 25)"
    echo "  serve [port]    -> Serve current directory over HTTP"
    echo "  ssh-load [key]  -> Start ssh-agent and load a key"
    echo ""

    echo "DOCKER"
    echo "  d               -> docker"
    echo "  dc              -> docker compose"
    echo "  dps             -> docker ps table"
    echo "  dlogs <name>    -> Follow container logs"
    echo "  dclean          -> Prune Docker safely"
    echo ""

    echo "PROJECT GENERATORS"
    echo "  py-project      -> Delegates to dev new python"
    echo "  mkapi           -> Delegates to dev new api"
    echo ""

    echo "SYSTEM"
    echo "  update          -> dnf upgrade (refresh)"
    echo "  update-all      -> dnf upgrade, autoremove, flatpak"
    echo "  health          -> Quick RAM/Disk info"
    echo "  health-check    -> Advanced system observability"
    echo "  zprof-start     -> Profile shell startup"
    echo ""

    echo "DEV TOOL"
    echo "  dev help        -> Full dev toolkit commands"
    echo "  dev new api     -> Rich FastAPI project"
    echo "  dev new python  -> Python project"
    echo ""

    echo "══════════════════════════════════════════════════"
    echo ""
}

# =========================================================
# USER ALIASES (last so local overrides win)
# =========================================================
[ -f "$HOME/.config/zsh/user_aliases.zsh" ] && source "$HOME/.config/zsh/user_aliases.zsh"

# =========================================================
# PROFILE OUTPUT
# =========================================================
if [[ -n "${ZSH_PROFILE:-}" ]]; then
    zprof
fi
