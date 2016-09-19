git config --global user.email "lorenzo.cavatorta.pr@gmail.com"
ssh-keygen -t rsa -b 4096 -C "lorenzo.cavatorta.pr@gmail.com"
#copying it to the clipboard
sudo apt-get install -y xclip
xclip -sel clip < ~/.ssh/id_rsa.pub

#on github, profile settings => ssh => add new => paste

#bits hardcoded in the script that we need to check

#ntfs partition parameters
sudo fdisk -l | grep -i ntfs 
ls -al /dev/disk/by-uuid/
