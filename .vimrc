execute pathogen#infect()
filetype plugin indent on
syntax on

colorscheme wal

set backspace=indent,eol,start
set foldmethod=indent
set t_Co=256
set background=dark
set tabstop=2
set shiftwidth=2
set expandtab
set laststatus=2
set updatetime=250
set scrolloff=3
set hlsearch
set incsearch
set hidden
set noshowmode

set backupdir=~/.vim/tmp,.
set directory=~/.vim/tmp,.
set undodir=~/.vim/tmp,.
let mapleader = ';'

" NERDTree Settings
map <C-l> :NERDTreeToggle<CR>

" TabgBar Settings
map <C-m> :TagbarToggle<CR>

" Airline Settings
let g:airline_powerline_fonts = 0
let g:airline_theme='base16_atelierheath'
let g:airline#extensions#tabline#enabled = 1

" Easy Motion Settings
let g:EasyMotion_startofline = 0
let g:EasyMotion_smartcase = 1

" Number Toggle Settings
" Toggle number lines with <F2>
nnoremap <F2> :set nonumber! norelativenumber!<CR>

" Hardmode Toggle
" <leader>h to toggle
nnoremap <leader>h <Esc>:call ToggleHardMode()<CR>

" Clear Search Hilighting
nnoremap <leader>c <Esc>:noh <CR>

" Syntastic Settings
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 0
let g:syntastic_check_on_wq = 1
let g:syntastic_loc_list_height=5
let g:syntastic_python_checkers=['python', 'flake8']
let g:syntastic_python_flake8_args='--ignore=E501,E115'

" SuperTab Settings
let g:SuperTabDefaultCompletionType = "<c-n>"

" Tomato Timer Settings
let g:tomato#remind = " "
let g:tomato#restinfo = " "
let g:tomato#show_clock = 1
let g:tomato#show_count_down = 1
