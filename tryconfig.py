#programs = {'em': {'realname':'emacs'} }

#chosen_programs = ['emacs', 'audacity', 'mp3_dec', 'pycharm']
#chosen_programs = ['emacs']
#chosen_programs = ['emacs', 'pycharm']
chosen_programs = ['dropbox']
#chosen_programs = ['google_music']

chosen_configs = [ 'caps2ctrl' , 'rtorrent_setup']

all_programs = {
    'emacs'         : {},
    'audacity'      : {},
    'mp3_dec'       : {'aka' : 'ffmpeg'},
    'beets'         : {},
    'vlc'           : {},
    'gimp'          : {},
    'pycharm'       : {'aka' : 'pycharm-community', 'repo' : 'ppa:mystic-mirage/pycharm'},
    'sublime'       : {'aka' : 'sublime-text-installer', 'repo' : 'ppa:webupd8team/sublime-text-3'},
    'rtorrent'      : {'config' : 'rtorrent_setup'},
    'google_music'  : {'realname' : 'google-musicmanager-beta',
                       'repo_prequel' : ['wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - '],
                       'repo' : '\'echo "deb [arch=amd64] http://dl.google.com/linux/musicmanager/deb/ stable main" >> /etc/apt/sources.list.d/google.list\'' ,
                       'repo_add_command' : 'sudo sh -c'},
    'pip'           : {'realname' : 'python-pip'},
    'dropbox'       : {'repo_prequel' : ['cd ~']
                       'repo_add_command' : 'wget -O - ',
                       'repo' : '"https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -',
                       'aka' : '',
                       'is_sudo' : '',
                       'install_command' : ''
    }
}


#every config is a list of steps to do,
#every step is a dic with a standard structure, type of action, actual action
config_step_types = {'bash_command' : 'single command to run in bash',
                     'copy_file' : 'copy a single file from a location to another',
                     'change_add_line' : 'changes or adds a line on a specific file',
                     'make_dir' : 'create a directory in a specified subdir'
}

all_configs = {
    'caps2ctrl' : [ {'type':'bash_command', 'content':'setxkbmap -option ctrl:nocaps'} ],
    'rtorrent_setup' : [ {'type':'make_dir', 'content': ['home', 'rDownloads' ]},
                         {'type':'make_dir', 'content': ['home', 'rDownloads','.rSessions' ]}
    ]
    
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


