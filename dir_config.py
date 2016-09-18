#configuration of the main folders used by the bootstrap script
import datetime

default_folders = {'home':['home','lollo']}
logfolder = '/'+ '/'.join(default_folders['home']) +'/Desktop/'
logfile = 'bootstrap_log-' + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M") + '.log'
