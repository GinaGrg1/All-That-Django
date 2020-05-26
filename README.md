# All-That-Django

## To clone a specific directory
$ mkdir password_generator

$ cd password_generator

$ git init

$ git remote add origin -f https://github.com/GinaGrg1/All-That-Django.git

$ git config core.sparsecheckout true

$ echo "password_generator/*" >> .git/info/sparse-checkout

$ git pull --depth=2 origin master
