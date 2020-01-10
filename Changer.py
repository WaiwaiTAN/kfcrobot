import os
import sys
import re
import random
import string

class Changer(object):
    def __init__(self, path):
        self.path = path
        self.allfiles = []
        self.chiallfiles = []
        self.newnames = []
        for i,j,k in os.walk(path):
            self.allfiles += k

        for k in self.allfiles:
            for i in k:
                if (not (i >= 'A' and i <= 'z')) and (not (i >= '0' and i <= '9')) and (not (i=='.' or i=='_' or i=='-')):
                    self.chiallfiles.append(k)
                    break

        print('These are all the filenames which are not support by xletax :')
        print(self.chiallfiles)
        print('Are you sure to rename them to random names and check and replace all the refferences of them in the files in this folder into their new names? (yes/not)')
        f=open(os.path.join(path+'/rename.sh'), 'w+')
        for s in self.chiallfiles:
            f.write('sed -i \"s/' + s + '/size/g" `grep ' + s +' -rl ./`\n')

        f.close()
        ans = input()
        if not (ans == 'yes' or ans == 'y' or ans == 'Y' or ans == 'Yes'):
            exit(0)

    def make_new_name(self):
        s = string.ascii_lowercase
        self.newnames = []
        for k in self.chiallfiles:
            newname = []
            for i in range(0, 6):
                newname.append(random.choice(s))

            name, suffix = str.split(k, '.')
            newname += '.' + suffix
            self.newnames.append(''.join(newname))

    def check(self, filename):
        flag = True
        fo = open(os.path.join(filename), mode='r')
        fn = open(os.path.join(filename), mode='r+')
        print('trying to replace original name in ' + filename)
        try:
            raw_line = fo.readline()
        except:
            fo.close()
            fn.close()
            fo = open(os.path.join(filename), mode = 'rb')
            fn = open(os.path.join(filename), mode = 'rb+')
            try:
                raw_line = fo.readline()
                flag = False
            except:
                print("Could not read " + filename)
        if flag:
            line = raw_line
        else:
            try:
                line = str(raw_line, 'utf-8')
            except:
                fo.close()
                fn.close()
                print(filename + ' is not a text file, skipped.')
                return
        
        while line != '':
            for index in range(len(self.chiallfiles)):
                if re.search(self.chiallfiles[index],line):
                    print(self.chiallfiles[index] + ' is found in ' + filename)
                    new_line = line.replace(self.chiallfiles[index], self.newnames[index])
                    seek_point = fo.tell()
                    fn.seek(seek_point, 0)
                    fn.write(new_line.encode('utf-8'))
        
            raw_line = fo.readline()
            if flag:
                line = raw_line
            else:
                line = str(raw_line, 'utf-8')

        fo.close()

if __name__ == '__main__':
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0])) 
    chg = Changer(dirname)
    chg.make_new_name()

    for i,j,k in os.walk(dirname):     
        for filename in k:
            filename = i+'\\' + filename
            if filename == sys.argv[0]:
                break    
            chg.check(filename)

    print(chg.chiallfiles)
    print(chg.newnames)