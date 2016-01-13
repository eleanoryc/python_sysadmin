#!/usr/bin/python

import sys
import subprocess_2_7
import getpass
import os
import time
import pwd

#input_user = raw_input('Username:')
input_passwd = getpass.getpass('Password:')

USERID = pwd.getpwuid( os.getuid() ).pw_name

SVN_CO_CMD = "svn --username " + USERID + " --password " + input_passwd + " co https://vc-commit.ops.sfdc.net/subversion/tools/imtncc"
SVN_UP_CMD = "svn --username " + USERID + " --password " + input_passwd + " up imtncc/"

#print SVN_CO_CMD 

def main():

    while True:

        try:
            svnco_output = subprocess_2_7.check_output(SVN_CO_CMD,shell=True)
            print(os.getcwd())
            svnup_output = subprocess_2_7.check_output(SVN_UP_CMD,shell=True)
            print svnup_output
            time.sleep(10)
        except:
            sys.exit(1)


if __name__ == '__main__':
    main()

