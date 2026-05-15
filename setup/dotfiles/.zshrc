# =========================================================
# OH MY ZSH
# =========================================================
export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME=""

plugins=(git)

source $ZSH/oh-my-zsh.sh

# =========================================================
# PATHS
# =========================================================
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.opencode/bin:$PATH"

# =========================================================
# ZOXIDE
# =========================================================
if command -v zoxide >/dev/null 2>&1 && [ -x "$(command -v zoxide)" ]; then
    eval "$(zoxide init zsh)"
    alias cd="z"
fi

# =========================================================
# FZF
# =========================================================
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# =========================================================
# STARSHIP
# =========================================================
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
echo "──────────────────────────────────────────────────"
echo "  🚀 Hello, Dario!"
echo "  📅 $(date +'%A, %B %d - %Y')"
echo "  📂 Directory: $(pwd)"
echo "──────────────────────────────────────────────────"

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
alias update='sudo apt update && sudo apt upgrade -y'
alias update-all='sudo apt update && sudo apt upgrade -y'

alias c='clear'

alias health="echo 'Memory:'; free -h | grep Mem; echo 'Disk:'; df -h / | grep /"

# =========================================================
# WORKSPACE
# =========================================================
alias workspace='cd ~/projects'
alias pathway='cd ~/projects/backend-devops-pathway'

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
# LOCAL PROJECT SCRIPTS
# =========================================================

# ---------------------------------------------------------
# Python project generator
# ---------------------------------------------------------
py-project() {
    if [ -z "$1" ]; then
        echo "Usage: py-project <project-name>"
        return 1
    fi

    local folder="$HOME/projects/backend-devops-pathway/$1"

    mkdir -p "$folder/app"

    cd "$folder" || {
        echo "Cannot access directory"
        return 1
    }

    python3 -m venv venv

    source venv/bin/activate

    cd app || return

    echo "print('--> Starting project: $1...')" > main.py
    echo "# Notes about: $1" > README.md

    cd "$folder" || return

    echo -e "venv/\n__pycache__/\n*.pyc\n.env" > .gitignore

    git init &>/dev/null

    echo "✅ Environment ready at: $folder"
}

# ---------------------------------------------------------
# FastAPI project generator
# ---------------------------------------------------------
mkapi() {
    if [ -z "$1" ]; then
        echo "Usage: mkapi <project-name>"
        return 1
    fi

    local folder="$HOME/projects/backend-devops-pathway/$1"

    mkdir -p "$folder/app"

    cd "$folder" || {
        echo "Cannot access directory"
        return 1
    }

    python3 -m venv venv

    source venv/bin/activate

    pip install fastapi uvicorn

    cd app || return

    cat > main.py << 'EOF'
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
EOF

    cat > README.md << 'EOF'
# FastAPI Project

## Run

uvicorn app.main:app --reload
EOF

    cd "$folder" || return

    cat > .gitignore << 'EOF'
venv/
__pycache__/
*.pyc
.env
.vscode/
EOF

    git init &>/dev/null

    echo "✅ FastAPI environment created at $folder"
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

    echo "✅ Successfully pushed to GitHub"
}

# =========================================================
# OBSERVABILITY
# =========================================================
health-check() {
    ram_usage=$(free | awk '/Mem:/ {print int($3/$2 * 100)}')

    cpu_load=$(awk '{print $1}' /proc/loadavg)
    cpu_cores=$(nproc)

    cpu_usage=$(awk -v load="$cpu_load" -v cores="$cpu_cores" 'BEGIN {print int((load/cores)*100)}')

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
    echo "  workspace      -> Go to ~/projects"
    echo "  pathway        -> Go to backend-devops-pathway"
    echo ""

    echo "SYSTEM"
    echo "  update          -> apt update + upgrade"
    echo "  health          -> Quick RAM/Disk info"
    echo "  health-check    -> Advanced system observability"
    echo ""

    echo "GIT"
    echo "  gst             -> git status"
    echo "  gcm             -> git commit -m"
    echo "  gsave           -> add/commit/push automation"
    echo ""

    echo "PROJECT GENERATORS"
    echo "  py-project      -> Create Python project"
    echo "  mkapi           -> Create FastAPI project"
    echo ""

    echo "DEV TOOL"
    echo "  dev             -> Unified DevOps toolkit script"
    echo "  dev health      -> System monitoring"
    echo "  dev new api     -> FastAPI generator"
    echo "  dev new python  -> Python generator"
    echo ""

    echo "UTILITIES"
    echo "  vsc             -> Open VS Code"
    echo "  d               -> docker"
    echo "  dc              -> docker compose"
    echo ""

    echo "══════════════════════════════════════════════════"
    echo ""
}