alias cp="cp -rpv"
alias mkdir="mkdir -p"

if command -q z
    alias cd="z"
end

if command -q batcat
  alias cat="batcat"
end

if command -q dnf
    alias gimme="sudo dnf install"
    alias yeet="sudo dnf remove"
end

if command -q exa
  alias ls="exa --icons"
end

if command -q et
  alias et="et -I --size-left --dirs-first"
end

if command -q fd
  alias find="echo 'This is not the command you are looking for, use fd instead.'; false" 
end

if command -q git
  alias gaa="git add ."
  alias gcm="git commit -m"
  alias gst="git status"
  alias fetch="git fetch"
  alias push="git push"
  alias pull="git pull"
end

if command -q nvim
  alias vim="nvim"
end

if command -q podman
  alias docker="podman"
end

if command -q sgpt
  alias gptcm="git diff | sgpt 'Generate git commit message, for the given changes'"
end

if command -q trash-put
  alias rm="echo 'This is not the command you are looking for, use trash instead.'; false" 
  alias trash="trash-put"
end
