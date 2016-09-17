from tryconfig import all_programs, chosen_programs
from tryconfig import defaults
from tryconfig import all_configs, config_step_types, chosen_configs
from dir_config import default_folders
from subprocess import STDOUT, check_call
#from types import *

import pdb
import os

class bashcommand:

    def __init__(self,s=''):
        self.command = s

    def __add__(self, other):
        if type(other) is str:
            self.command += ' ' + other
            return
        if type(other) is list:
            self.command += ' ' + ' '.join(l)
            return

    def run(self, choseprintlog=False):
        self.stdlog = os.popen(self.command)
        if choseprintlog:
            self.printlog()

    def printlog(self):
        print(self.stdlog)
        for l in self.stdlog:
            print(l)


class stuff_to_do:

    def __init__(self,kind,config_dic,default_dic):
        self.kind = kind
        self.config_dic = config_dic
        self.default_dic = default_dic
    
    def get_attr(self, attr, dictionary=False, defaults=False):
#        pdb.set_trace()
        if dictionary == False:
            dictionary = self.config_dic
        if defaults == False:
            defaults = self.default_dic
        if attr in dictionary:
            return dictionary[attr]
        else:
            try:
                return defaults[attr]
            except KeyError:
                print('warning: get_attr raised on a non-defaulted attribute %s',attr)
                return False

            
class program(stuff_to_do):

    def __init__(self,name):
        self.name = name
        super().__init__('program', all_programs[name] ,defaults)

    def build_install_command(self):
        l = []
        realname=self.name
        if 'aka' in self.config_dic:
            realname = self.get_attr('aka')
        for i in ['is_sudo','install_command']:
            l.append(self.get_attr(i))
        l.append(realname)
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
        else:
            conf = configuration( c, all_configs[c] )
            conf.run_all_steps()
    

class configuration(stuff_to_do):

    def __init__(self,name):
        self.name = name
        super().__init__('config', all_configs[name] ,defaults)


    def check_steps(self):
        for s in self.config_dic:
            assert s['type'] in config_step_types, 'error, command type not allowed'
            if s['type'] not in config_step_types:
                   return 'error, command type not allowed'
        return

    def run_step(self,step):
        if step['type'] == 'bash_command':
            command = bashcommand(step['content'])
            command.run(True)
        if step['type'] == 'make_dir':
            content = step['content']
            directory = '/'
            for c in content:
#                pdb.set_trace()
                path_steps = self.get_attr(c,default_folders)
                if path_steps:
                    for s in path_steps:
                        directory = os.path.join(directory,s)
                else:
                    directory = os.path.join(directory,c)
            print(directory)
            print(os.path.exists(directory))
            if not os.path.exists(directory):
                os.makedirs(directory)
                
       
            
    def run_all_steps(self):
        self.check_steps()
        for s in self.config_dic:
            self.run_step(s)

    
        
for p in chosen_programs:
    prog = program(p)
    print(prog.build_install_command())
    prog.install()

for c in chosen_configs:
    conf = configuration( c )
    conf.run_all_steps()
    
