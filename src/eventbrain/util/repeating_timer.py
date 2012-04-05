from threading import Timer

class RepeatingTimer(object):
    """
    USAGE:
    from time import sleep
    def myFunction(inputArgument):
        print(inputArgument)
    
    r = RepeatingTimer(0.5, myFunction, "hello")
    r.start(); sleep(2); r.interval = 0.05; sleep(2); r.stop()
    """

    def __init__(self,interval, function, *args, **kwargs):
        super(RepeatingTimer, self).__init__()
        self.args = args
        self.kwargs = kwargs
        self.function = function
        self.interval = interval
        self.event = threading.Event()

    def start(self):
        while 1:
            self.function(*self.args, **self.kwargs)
            if self.event.wait(self.interval):
                break

    def stop(self):
        self.event.set()