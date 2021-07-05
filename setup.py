import subprocess
import sys
from __dwnldDrivers.versions import *

def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])


def main():
    my_packages = ['requests', 'clint', 'faker', 'selenium', 'colorama']

    installed_pr = []

    for package in my_packages:
        install(package)
        print('\n')

    print('Firefox')
    firefox_ver = get_firefox_version()
    if firefox_ver != None:
        is_firefox_there = 1
        installed_pr.append('Firefox')
        setup_Firefox(firefox_ver)
    else:
        is_firefox_there = 0
        print('Firefox isn\'t installed')


    if is_firefox_there == 0 :
        print(
            'Error - Setup installation failed \nReason - Please install Firefox browser to complete setup process')
        exit()


    inpErr = True

    while inpErr != False:
        userInput = int(1)

        if userInput <= len(installed_pr) and userInput > 0:
            selected = installed_pr[userInput - 1]
            inpErr = False
        else:
            print('Wrong id, Either input 1 or 2')

    print('Setup Completed')


if __name__ == '__main__':
    main()
