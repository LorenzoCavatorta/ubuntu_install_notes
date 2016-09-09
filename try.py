from tryconfig import programs
from tryconfig import defaults

class pr:

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


p1 = pr('emacs',programs['emacs'])
print(p1.name)
print(p1.config)
#print(p1.get_attr('realname'))
#print(p1.get_real_name())
#print(p1.get_install_command())
#print(p1.is_sudo())
print(p1.build_install_command())

s = p1.name + 'test'
print(s)

print('hellp')
