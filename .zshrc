# Path to your oh-my-zsh installation.
export ZSH=/home/jmoss/.oh-my-zsh

POWERLEVEL9K_MODE='awesome-fontconfig'
POWERLEVEL9K_PROMPT_ON_NEWLINE=true
POWERLEVEL9K_STATUS_VERBOSE=false
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(status context dir vcs virtualenv)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(time background_jobs)
ZSH_THEME="powerlevel9k/powerlevel9k"
#ZSH_THEME="bira"

# Uncomment the following line to change how often to auto-update (in days).
export UPDATE_ZSH_DAYS=1

ENABLE_CORRECTION="true"

plugins=(git python)

source $ZSH/oh-my-zsh.sh

# User configuration

export PATH="$HOME/.local/bin:$PATH"
export WORKON_HOME=~/.virtualenvs
source /usr/bin/virtualenvwrapper_lazy.sh
source /home/jmoss/src/scripts/multiplex
export TERM="xterm-256color"
export DEFAULT_USER=jmoss
export VISUAL="vim"
export BROWSER="qutebrowser"

alias ssh='TERM=xterm-256color ssh'
alias tmux='TERM=xterm-256color tmux'
alias g='git'
alias dots='/usr/bin/git --git-dir=$HOME/.dots/ --work-tree=$HOME'
alias graviton='/home/jmoss/.local/bin/graviton-cli-0.40.1/bin/graviton'
alias cap='bundle exec cap'

# Add RVM to PATH for scripting. Make sure this is the last PATH variable change.
export PATH="$PATH:$HOME/.rvm/bin"
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"
