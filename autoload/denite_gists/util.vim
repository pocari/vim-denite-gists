function! denite_gists#util#github_user() abort
  return substitute(system('git config --get github.user'), "\n", '', '')
endfunction
