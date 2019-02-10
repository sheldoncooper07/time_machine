from os import getcwd, environ, chdir, listdir, path
from subprocess import run, call, PIPE, getoutput
from functools import partial
from sys import exit

HOME = environ.get('HOME')
PWD = environ.get('PWD')
basedir = PWD

def validSandBoxInitial():
    PWD = environ.get('PWD')
    if not (PWD.startswith(HOME) and PWD!=HOME):
        return False
    return True

def validPWD():
    # print(os.getcwd(),basedir)
    if getcwd().startswith(basedir):
        return True
    return False
        
def initialize():
    chdir(basedir)
    chdir('..')
    if path.exists('.git'):
        #print('.git detected')
        #print('Remove .git to proceed.')
        #print('Exiting....')
        print("Mysterious Error!")
        print("\033[1;37m",end='')
        exit(0)
    nrun = partial(call,shell=True,stdout=PIPE)
    rfolder = basedir[len(getcwd()) + 1:]
    nrun('touch .gitignore')
    for f in listdir():
        if f!=rfolder and f!='.gitignore':
            nrun('echo ' + f + ' >> .gitignore' )
    nrun('git init')
    nrun('git add .')
    nrun('git commit -m "original"')
    chdir(rfolder)


def start():
    print("\033[1;33m",end='')
    print("Use exit or Ctrl-C to exit the pverse")
    prompt = "(pverse)%s$ "
    print("\033[1;32m",end='')
    print(prompt % getcwd(),end='')
    print("\033[1;37m",end='')
    cmd = input()    
    while cmd != "exit":
        if cmd.startswith("cd "):
            beforecd = getcwd()
            try:
                chdir(cmd[2:].strip())
                if not validPWD():
                    print("\033[1;31m",end='')
                    print("You can't go outside the sandbox!")
                    chdir(beforecd)
            except:
                print("\033[1;31m",end='')
                print("Call Gaurav")
        else:       
            try:
                run(cmd,shell=True)
            except:
                print("\033[1;31m",end='')
                print("There was some error. Call Mukesh!")
        print("\033[1;32m",end='')
        print(prompt % getcwd(),end='')
        print("\033[1;37m",end='')
        cmd = input()

def resetall():
    while True:
        print("\033[1;33m",end='')
        print("Do you want to keep these changes [y/n]: ",end='')
        print("\033[1;37m",end='')
        saveornot = input()
        if saveornot in {'y','n'}:
            break
    gitcommit()
    if saveornot == 'n': 
        initial_commit = getoutput('git rev-list HEAD | tail -n 1')
        # print(initial_commit)
        getoutput('git reset --hard ' + initial_commit)
        # subprocess.check_output(['rm', '-rf', '.git'])
    chdir(basedir)
    chdir('..')
    run('rm -rf .git',shell=True,cwd=getcwd())
    run('rm .gitignore',shell=True,cwd=getcwd())
    if saveornot == 'n':
        run('find . -empty -type d -delete',shell=True,cwd=basedir)

def gitcommit():
    getoutput('git add .')
    getoutput('git commit -m "Nahin BACHEGA"')

def main():
    if not validSandBoxInitial():
        print("\033[1;31m",end='')
        print('pverse may exist only inside a subdirectory of HOME')
        print("\033[1;37m",end='')
        exit(0)
    initialize()
    try:
        start()
    except:
        print()
    # except KeyboardInterrupt:
        pass
    resetall()

if __name__ == '__main__':
    print("\033[1;32m",end='')
    main()
    print("\033[1;33m",end='')
    print("Exited Successfully!")
    print("\033[1;37m",end='')
