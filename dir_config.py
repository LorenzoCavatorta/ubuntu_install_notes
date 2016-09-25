#configuration of the main folders used by the bootstrap script
import datetime

default_folders = {'usr_home':['home','lollo'], 'bootstrap_folder':['home','lollo','projects','ubuntu_install_notes']}
logfolder = '/'+ '/'.join(default_folders['usr_home']) +'/Desktop/'
logfile = 'bootstrap_log-' + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M") + '.log'
