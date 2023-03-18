import os

# pid (process ID) and cwd
print(os.getpid(), os.getcwd())
# uid (user ID) and gid (group ID)
print(os.getuid(), os.getgid())

# subprocess module is used to create and manage processes
import subprocess

# in case you need just output of a command
ret = subprocess.getoutput("date")
print(ret)

# check_output() - receives list of strings as input, returns output in bytes
ret = subprocess.check_output(["date"])
print(ret)

# getstatusoutput() - returns tuple of status code and string output
ret = subprocess.getstatusoutput("date")
print(ret)

# call() - only returns status code
ret = subprocess.call("date")
print(ret)

# two ways to run with arguments:
# 1. pass the whole command as one string and use shell=True arg
# 2. pass the while command as list of command and args
ret = subprocess.call("date -u", shell=True)
ret = subprocess.call(["date", "-u"])

