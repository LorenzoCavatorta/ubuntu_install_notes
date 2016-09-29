#small trick on how I got this:
#history | cut -c 8- | tail -n30 > ~/projects/ubuntu_install_notes/emacs_setup_notes.sh 


#ll /usr/bin/python*
virtualenv -p /usr/bin/python3.4 mymess

cat <<EOF > ~/.bashrc
mymess() {
    # Set working directory.
    cd /home/lorenzocavatorta/projects/ubuntu_install_notes/
    # Set virtualenv.
    virtualenv_path="/home/lorenzocavatorta/.envs/mymess/bin/activate"
    source "$virtualenv_path"
}
EOF
. ~/.bashrc
mymess
#python #just to check it went fine

#these are from
#https://www.youtube.com/watch?v=0kuCeS-mfyc
#and 
#https://github.com/jorgenschaefer/elpy

pip install elpy
pip install rope
pip install jedi

# flake8 for code checks
pip install flake8
# importmagic for automatic imports
pip install importmagic
# and autopep8 for automatic PEP8 formatting
pip install autopep8
# and yapf for code formatting
pip install yapf

#evaluate this in emacs
#(require 'package)
#(add-to-list 'package-archives
#             '("elpy" . "https://jorgenschaefer.github.io/packages/"))
#select and M-x eval-region

#M-x package-refresh-contents
#install
#M-x package-install RET elpy RET
#or M-x package-list-packages, navigate to elpy, hit I to select it (pointer on the name), x to install it

cat <<EOF > ~/.emacs
(package-initialize)
(elpy-enable)
EOF

#video is rebinding two bugs (define-key global-map (kbd "WHATEVER") 'iedit-mode)
# M-x elpy-config to check what's going on, 
#in my case the virtual env was not active
# M-x pyvenv-activate RET ~/.envs/mymess/
