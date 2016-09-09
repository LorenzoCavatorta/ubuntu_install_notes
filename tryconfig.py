#programs = {'em': {'realname':'emacs'} }

chosen_programs = ['emacs', 'audacity', 'mp3_dec']

all_programs = {
    'emacs'     : {},
    'audacity'  : {},
    'mp3_dec'   : {'realname' : 'ffmpeg'},
    'beets'     : {},
    'vlc'       : {},
    'gimp'      : {}
            }

defaults = {'install_command' : 'apt-get -y install',
            'is_sudo' : 'sudo',
            'realname' : 'self'
            }
