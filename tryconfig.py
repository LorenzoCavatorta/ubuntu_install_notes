#programs = {'em': {'realname':'emacs'} }

chosen_programs = ['emacs', 'audacity', 'mp3_dec', 'pycharm']

all_programs = {
    'emacs'     : {},
    'audacity'  : {},
    'mp3_dec'   : {'realname' : 'ffmpeg'},
    'beets'     : {},
    'vlc'       : {},
    'gimp'      : {},
    'pycharm'   : {'realname' : 'pycharm-community', 'repo' : 'ppa:mystic-mirage/pycharm'}
            }

defaults = {'install_command' : 'apt-get -y install',
            'is_sudo' : 'sudo',
            'realname' : 'self',
            'repo' : 'STNDRD',
            'repo_add_command' : 'sudo add-apt-repository -y',
            'repo_prequel' : '',
            'repo_update_command' : 'sudo apt-get update'
            }
