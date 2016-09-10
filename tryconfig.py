#programs = {'em': {'realname':'emacs'} }

#chosen_programs = ['emacs', 'audacity', 'mp3_dec', 'pycharm']
chosen_programs = ['sublime']
#chosen_programs = ['emacs']

all_programs = {
    'emacs'     : {},
    'audacity'  : {},
    'mp3_dec'   : {'realname' : 'ffmpeg'},
    'beets'     : {},
    'vlc'       : {},
    'gimp'      : {},
    'pycharm'   : {'realname' : 'pycharm-community', 'repo' : 'ppa:mystic-mirage/pycharm'},
    'sublime'   : {'realname' : 'sublime-text-installer', 'repo' : 'ppa:webupd8team/sublime-text-3'}
            }

defaults = {'install_command' : 'apt-get -y install',
            'is_sudo' : 'sudo',
            'realname' : 'self',
            'repo' : 'STNDRD',
            'repo_add_command' : 'sudo add-apt-repository -y',
            'repo_prequel' : '',
            'repo_update_command' : 'sudo apt-get update'
            }
