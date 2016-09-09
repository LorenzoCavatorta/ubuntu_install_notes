from tryconfig import all_programs
from tryconfig import defaults
from tryconfig import chosen_programs
from subprocess import STDOUT, check_call
import os

class program:

    def __init__(self, s, program_dict):
        self.name = s
        self.config = program_dict

    def get_attr(self,attr):
        if attr in self.config:
            return self.config[attr]
        else:
            try:
                if attr == 'realname':
                    return self.name
                else:
                    return defaults[attr]
            except KeyError:
                print 'ERROR: get_attr raised on a non-defaulted attribute'


    def build_install_command(self):
        l = []
        for i in ['is_sudo','install_command','realname']:
            l.append(self.get_attr(i))
        return ' '.join(l)

    def install(self):
        stdlog = os.popen(self.build_install_command())


i = 1
for p in chosen_programs:
    prog = program( p , all_programs[p])
    print(prog.build_install_command())
    if i == 1:
        prog.install()
    i += 1
