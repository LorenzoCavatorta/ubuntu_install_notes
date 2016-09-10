from tryconfig import all_programs
from tryconfig import defaults
from tryconfig import chosen_programs
from subprocess import STDOUT, check_call
import os

class bashcommand:

    def __init__(self,s=''):
        self.command = s

    def add_list(self,l):
        self.command + ' '.join(l)

    def run(self):
        stdlog = os.popen(self.command)

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

    def run_install(self):
        installer = bashcommand(self.build_install_command())
        installer.run()



    def add_repo(self):
        repo = self.get_attr('repo')
        if repo == defaults['repo']:
            return
        else:
            pre = self.get_attr('repo_prequel')
            for c in pre:
                command = bashcommand(c)
                command.run()
            repo_adder = bashcommand(self.get_attr('repo_add_command'))
            repo_adder.add_list(repo)
            updater = bashcommand(self.get_attr('repo_update_command'))
            updater.run()

    def install(self):
        self.run_install()

i = 1
for p in chosen_programs:
    prog = program( p , all_programs[p])
    print(prog.build_install_command())
    if i == 4:
        prog.install()
    i += 1
