import subprocess, os, sys
# print(subprocess.check_output(['git', 'init']))
# print(subprocess.check_output(['ls', '-l']).decode('utf-8'))
def initialize():
    if os.path.exists('.git'):
        print('.git detected')
        print('Remove .git to proceed.')
        print('Exiting....')
        sys.exit(0)
    gitinit = ['git','init']
    subprocess.check_output(gitinit)
    subprocess.run("echo pro.py > .gitignore", shell=True, check=True)
    subprocess.run("git add .",shell=True,check=True)
    subprocess.check_output("git commit -m original",shell=True)

def resetall():
    initial_commit = subprocess.getoutput('git rev-list HEAD | tail -n 1')
    # print(initial_commit)
    subprocess.getoutput('git reset --hard ' + initial_commit)
    # subprocess.check_output(['rm', '-rf', '.git'])
    subprocess.run('rm -rf .git',shell=True)
    subprocess.run('rm .gitignore',shell=True)
    subprocess.run('find . -empty -type d -delete',shell=True)

def start():
    out = '' 
    cmd = input("Enter Command: ")
    cud = os.getcwd()
    while cmd != "exit":
        cmd = cmd.strip().split(' ')        
        try:
            out = subprocess.check_output(cmd).decode('utf-8')
        except:
            print("There was some error. Call Mukesh!")
        if out != '':
            print(out)
        gitcommit()
        cmd = input("Enter Command: ")

def gitcommit():
    from subprocess import getoutput
    getoutput('git add .')
    getoutput('git commit -m "Nahin BACHEGA"')

def main():
    initialize()
    start()
    resetall()

if __name__ == '__main__':
    main()
    print("Exited!")

# if(cmd[0] == "cd"):
#     cud = cud+"/"+cmd[1]
#     print(cud)
#     try:
#         out = subprocess.check_output(cud).decode('utf-8')
#     except:
#         print("can't run this command")
#     # if out != '':
#     print(out)