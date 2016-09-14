#programs = {'em': {'realname':'emacs'} }

#chosen_programs = ['emacs', 'audacity', 'mp3_dec', 'pycharm']
chosen_programs = ['emacs']
#chosen_programs = ['sublime']
#chosen_programs = ['google_music']

chosen_configs = [ 'caps2ctrl' ]

all_programs = {
    'emacs'         : {},
    'audacity'      : {},
    'mp3_dec'       : {'realname' : 'ffmpeg'},
    'beets'         : {},
    'vlc'           : {},
    'gimp'          : {},
    'pycharm'       : {'realname' : 'pycharm-community', 'repo' : 'ppa:mystic-mirage/pycharm'},
    'sublime'       : {'realname' : 'sublime-text-installer', 'repo' : 'ppa:webupd8team/sublime-text-3'},
    #'google_music'  : {'realname' : '', 'repo_prequel' : ['wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - '], 'repo' : 'sudo sh -c \'echo "deb [arch=amd64] http://dl.google.com/linux/musicmanager/deb/ stable main" >> /etc/apt/sources.list.d/google.list\'' , 'repo_add_command' : ''}
    'google_music'  : {'realname' : 'google-musicmanager-beta',
                       'repo_prequel' : ['wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - '],
                       'repo' : '\'echo "deb [arch=amd64] http://dl.google.com/linux/musicmanager/deb/ stable main" >> /etc/apt/sources.list.d/google.list\'' ,
                       'repo_add_command' : 'sudo sh -c'},
    'pip'           : {'realname' : 'python-pip'},
}


#every config is a list of steps to do,
#every step is a dic with a standard structure, type of action, actual action
config_step_types = {'bash_command':'single command to run in bash'}

all_configs = {
    'caps2ctrl' : [ {'type':'bash_command', 'content':'setxkbmap -option ctrl:nocaps'} ],
}


defaults = {'install_command' : 'apt-get -y install',
            'is_sudo' : 'sudo',
            'realname' : 'self',
            'repo' : 'STNDRD',
            'repo_add_command' : 'sudo add-apt-repository -y',
            'repo_prequel' : '',
            'repo_update_command' : 'sudo apt-get update',
            'config' : 'no'
            }


