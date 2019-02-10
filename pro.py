import subprocess, os, sys
from os import chdir, getcwd
from shlex import split
# print(subprocess.check_output(['git', 'init']))
# print(subprocess.check_output(['ls', '-l']).decode('utf-8'))
def initialize():
    HOME = os.environ.get('HOME')
    if os.path.exists(HOME + '/.git'):
        print('.git detected')
        print('Remove .git to proceed.')
        print('Exiting....')
        sys.exit(0)
    gitinit = ['git','init']
    subprocess.check_output(gitinit,cwd=HOME)
    subprocess.run("echo pro.py > .gitignore", shell=True, check=True,cwd=HOME)
    subprocess.run("git add .",shell=True,check=True)
    subprocess.check_output("git commit -m original",shell=True)

def resetall():
    HOME = os.environ.get('HOME')
    
    initial_commit = subprocess.getoutput('git rev-list HEAD | tail -n 1')
    # print(initial_commit)
    subprocess.getoutput('git reset --hard ' + initial_commit)
    # subprocess.check_output(['rm', '-rf', '.git'])
    subprocess.run('rm -rf .git',shell=True,cwd=HOME)
    subprocess.run('rm .gitignore',shell=True,cwd=HOME)
    # subprocess.run('find . -empty -type d -delete',shell=True)

def start():
    out = '' 
    cud = os.getcwd()
    cmd = input(getcwd() + "$ ")
    while cmd != "exit":
        if cmd[:2] == "cd":
            os.chdir(cmd[2:].strip())
        else:
            # cmd = split(cmd)       
            try:
                # out = subprocess.check_output(cmd).decode('utf-8').strip()
                out = subprocess.run(cmd,shell=True)
            except:
                print("There was some error. Call Mukesh!")
            #if out != '':
            #    print(out)
            gitcommit()
        cmd = input(getcwd() + "$ ")

def gitcommit():
    from subprocess import getoutput
    getoutput('git add .')
    getoutput('git commit -m "Nahin BACHEGA"')

def main():
    initialize()
    try:
        start()
    except:
    # except KeyboardInterrupt:
        pass
    resetall()

if __name__ == '__main__':
    main()
    print("Exited!")
