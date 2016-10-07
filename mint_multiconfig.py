


#chosen_programs = ['emacs', 'audacity', 'mp3_dec', 'pycharm', 'mp3_dec', 'beets', 'vlc', 'vim', 'gimp', 'pycharm', 'sublime', 'rtorrent', 'pip', 'dropbox', 'google_music']
#chosen_programs = [ 'rtorrent', 'skype']
#chosen_programs = ['beets']
chosen_programs = []
chosen_configs = [ 'caps2ctrl_perm' ] # , 'lock-screensaver-disable', 'add_beet_plugin_libs']
#chosen_configs = [ 'adjust_file_association']


all_programs = {
    'emacs'         : {},
    'vim'           : {},
    'audacity'      : {},
    'mp3_dec'       : {'aka' : 'ffmpeg'},
    'beets'         : {'config' : 'beet_setup'},
    'vlc'           : {},
    'gimp'          : {},
    'pycharm'       : {'aka' : 'pycharm-community', 'repo' : 'ppa:mystic-mirage/pycharm'},
    'sublime'       : {'aka' : 'sublime-text-installer', 'repo' : 'ppa:webupd8team/sublime-text-3'},
    'rtorrent'      : {'config' : 'rtorrent_setup'},
    'google_music'  : {'realname' : 'google-musicmanager-beta',
                       'repo_prequel' : ['wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - '],
                       'repo' : '\'echo "deb [arch=amd64] http://dl.google.com/linux/musicmanager/deb/ stable main" >> /etc/apt/sources.list.d/google.list\'' ,
                       'repo_add_command' : 'sudo sh -c'},
    'pip'           : {'aka' : 'python-dev python-pip', 'config':'pip-upgrade-setup'},
    'dropbox'       : {'repo_prequel' : ['cd ~'],
                       'repo_add_command' : 'wget -O - ',
                       'repo' : '"https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -',
                       'aka' : '',
                       'is_sudo' : '',
                       'install_command' : '',
                       'config': 'dropbox_at_login'  },
    'chrome'        : {'aka' : 'google-chrome-stable',
                       'repo_prequel' : 'wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -', #MIGHT NOT BE REQUIRED!
                       'repo' : 'deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main' },
    'skype'         : {},
    'musescore'     : {}
}


#every config is a list of steps to do,
#every step is a dic with a standard structure, type of action, actual action
config_step_types = {'bashcommand' : 'single command to run in bash',
                     'copy_file' : 'copy a single file from a location to another',
                     'change_add_line' : 'changes or adds a line on a specific file', #{'type':'change_add_line', 'content': 'file':'', 'regex':'', 'newline':''}
                     'make_dir' : 'create a directory in a specified subdir'
}

'''
all_configs = {
    'caps2ctrl_temp' : [ {'type':'bash_command', 'content':'setxkbmap -option ctrl:nocaps'} ],
    'caps2ctrl_perm' : [ {'type':'change_add_line', 'content':{'file':'/home/lollo/.profile',
                                                               'regex':'\s*setxkbmap\s*.*ctrl:nocaps.*',
                                                               'newline':'setxkbmap -option ctrl:nocaps'} ],
    'rtorrent_setup' : [ {'type':make_dir, 'content': ['home', 'rDownloads']},
                         {'type':make_dir, 'content': ['home', 'rDownloads','.rSessions']},
                         {'type':change_add_line, 'content': {'file':'/home/lollo/.rtorrent.rc',
                                                                'regex':r'^\s*directory\s*=\s*(\/|$|\"|\').*',
                                                                'newline':'directory = /home/lollo/rDownloads'}},
                         {'type':change_add_line, 'content': {'file':'/home/lollo/.rtorrent.rc',
                                                                'regex':r'^\s*session\s*=\s*(\/|$|\"|\').*',
                                                                'newline':'session = /home/lollo/rDownloads/.rSessions'}}
                       ],
    'dropbox_at_login' : [ {'type':change_add_line, 'content':{'file':'/etc/rc.local',
                                                                 'regex':'.+dropboxd.+',
                                                                 'newline':'~/.dropbox-dist/dropboxd'} } ],
    #to check these hardcoded parameters: sudo fdisk -l | grep -i ntfs ; ls -al /dev/disk/by-uuid/
    'add_media_partition' : [ {'type':make_dir, 'content':['/mediadisk']},
                              {'type': change_add_line, 'content': {'file':'/etc/fstab',
                                                                      'regex':'.*UUID=AA2E6BAF2E6B72ED.*',
                                                                      'newline':'UUID=AA2E6BAF2E6B72ED            /mediadisk   ntfs  auto            0       0' } }],
    'replace_test' : [{'type':change_add_line, 'content': {'file':'/home/lollo/tmp/io.test',
                                                             'regex':'.+di.+',
                                                             'newline':'oddio'} }],
    'add_beet_plugin_libs' : [{'type':bashcommand, 'content':'sudo pip install pylast request discogs-client'}], #manca beet completion e moving config file
    'adjust_file_association' : [ {'type':change_add_line, 'content': {'file':'/usr/share/applications/defaults.list',
                                                                'regex':r'.*video.*avi\s*=.*',
                                                                'newline':'video/x-avi=xplayer.desktop;vlc.desktop'}},
                                  {'type':change_add_line, 'content': {'file':'/usr/share/applications/defaults.list',
                                                                'regex':r'.*video.*mpeg\s*=.*',
                                                                'newline':'video/mpeg=xplayer.desktop;vlc.desktop'}},
                                  {'type':change_add_line, 'content': {'file':'/usr/share/applications/defaults.list',
                                                                'regex':r'.*video.*ogg\s*=.*',
                                                                'newline':'video/ogg=xplayer.desktop;vlc.desktop'}},
                                  {'type':change_add_line, 'content': {'file':'/usr/share/applications/defaults.list',
                                                                'regex':r'.*video.*ogg\s*=.*',
                                                                'newline':'video/mp4=xplayer.desktop;vlc.desktop'}},
                                  {'type':change_add_line, 'content': {'file':'/usr/share/applications/defaults.list',
                                                                'regex':r'.*video.*m4v\s*=.*',
                                                                'newline':'video/x-m4v=xplayer.desktop;vlc.desktop'}}
                                  ]    
}
'''

defaults = {'install_command' : 'apt-get -q -y install',
            'is_sudo' : 'sudo',
            'realname' : 'self',
            'repo' : 'STNDRD',
            'repo_add_command' : 'sudo add-apt-repository -y',
            'repo_prequel' : '',
            'repo_update_command' : 'sudo apt-get update',
            'config' : 'no'
            }


