from tryconfig import all_programs, chosen_programs
from tryconfig import defaults
from tryconfig import all_configs, config_step_types, chosen_configs
from subprocess import STDOUT, check_call
from types import *

import pdb
import os

class bashcommand:

    def __init__(self,s=''):
        self.command = s

    def __add__(self, other):
        if type(other) is StringType:
            self.command += ' ' + other
            return
        if type(other) is ListType:
            self.command += ' ' + ' '.join(l)
            return

    def run(self, choseprintlog=False):
        self.stdlog = os.popen(self.command)
        if choseprintlog:
            self.printlog()

    def printlog(self):
        print(self.stdlog)
        for l in self.stdlog:
            print l

class program:

    def __init__(self, s, program_dict):
        self.name = s
        self.setup_instructions = program_dict

    def get_attr(self,attr):
        if attr in self.setup_instructions:
            return self.setup_instructions[attr]
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
        installer.run(True)
        installer.printlog()



    def add_repo(self):
        repo = self.get_attr('repo')
        if repo == defaults['repo']:
            return
        else:
            pre = self.get_attr('repo_prequel')
            #pdb.set_trace()
            for c in pre:
                command = bashcommand(c)
                command.run(True)
            repo_adder = bashcommand(self.get_attr('repo_add_command'))
            repo_adder + repo
            repo_adder.run(True)
            #pdb.set_trace()
            updater = bashcommand(self.get_attr('repo_update_command'))
            updater.run()

    def install(self):
        self.add_repo()
        self.run_install()
        self.prog_config()


    def prog_config(self):
        c = self.get_attr('config')
        if c == defaults['config']:
            return
 #       else:
#        for i in config_steps:
            #move config
            #add config lines
            #

class configuration:

    def __init__(self,name,config_instrucions):
        self.name = name
        self.steps = config_instrucions

    def check_steps(self):
        for s in self.steps:
            assert s['type'] in config_step_types, 'error, command type not allowed'
            if s['type'] not in config_step_types:
                   return 'error, command type not allowed'
        return

    def run_step(self,step):
        if step['type'] == 'bash_command':
            command = bashcommand(step['content'])
            command.run(True)

    def run_all_steps(self):
        self.check_steps()
        for s in self.steps:
            self.run_step(s)

    
        
for p in chosen_programs:
    prog = program( p , all_programs[p])
    print(prog.build_install_command())
    prog.install()

for c in chosen_configs:
    conf = configuration( c, all_configs[c] )
    conf.run_all_steps()
    
