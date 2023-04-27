vim.cmd('noremap <C-b> :noh<cr>:call clearmatches()<cr>') -- clear matches Ctrl+b

function map(mode, shortcut, command)
  vim.api.nvim_set_keymap(mode, shortcut, command, { noremap = true, silent = true })
end

function nmap(shortcut, command)
  map('n', shortcut, command)
end

function imap(shortcut, command)
  map('i', shortcut, command)
end

function vmap(shortcut, command)
  map('v', shortcut, command)
end

function cmap(shortcut, command)
  map('c', shortcut, command)
end

function tmap(shortcut, command)
  map('t', shortcut, command)
end

-- map('``', ':nohlsearch<CR>:call minimap#vim#ClearColorSearch()<CR>')

-- search
-- keep search matches in the middle of the window
nmap('n', 'nzzzv')
nmap('N', 'Nzzzv')

-- Same when jumping around
nmap('g;', 'g;zz')

-- clipboard
vmap('<C-c>', '"+yi')
vmap('<C-x>', '"+c')
vmap('<C-v>', 'c<ESC>"+p')
imap('<C-v', '<ESC>"+pa')

-- use Fuck to save when file is read only
vim.cmd 'command! Fuck w !sudo tee %'
