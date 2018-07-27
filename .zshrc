export ZSH=/home/hubcaps/.oh-my-zsh

ZSH_THEME="theunraveler"

export UPDATE_ZSH_DAYS=1
ENABLE_CORRECTION="true"

plugins=(git python history-substring-search zsh-autosuggestions zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

# User configuration

export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"

export WORKON_HOME=~/.virtualenvs
source $HOME/.local/bin/virtualenvwrapper_lazy.sh
source /home/hubcaps/src/scripts/multiplex

export TERM="xterm-256color"

export DEFAULT_USER=hubcaps
export VISUAL="vim"
export BROWSER="qutebrowser"

alias ssh='TERM=xterm-256color ssh'
alias tmux='TERM=xterm-256color tmux'
alias g='git'
alias dots='/usr/bin/git --git-dir=$HOME/.doots/ --work-tree=$HOME'
alias ansible-playbook='ANSIBLE_COW_SELECTION=bong ansible-playbook'
alias wtf='man'

(cat ~/.cache/wal/sequences &)
