import os

print('Prossess (%s) start...' % os.getpid())

pid = os.fork()
if pid == 0:
    print("I am child process (%s) and my partent is %s." %(os.getpid()), os.getpgid())
else:
    print('I (%s) just creat a child process (%s).' %(os.getpid(), pid))