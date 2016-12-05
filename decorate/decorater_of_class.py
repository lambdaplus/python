# coding=utf-8
class Log():

    def __init__(self, file="info.log"):
        self.file = file

    def __call__(self, func):
        log = func.__name__ + " was called"
        print(log)
        with open(self.file, 'a') as f:
            f.write(log + '\n')


@Log()
def hello():
    print('Hello World!')
