from threading import *
import copy
import time

from gi.repository import GObject

class Future:
    def __init__(self, func, *param):
        self.done = False
        self.result = None
        self.condition = Condition()
        self.thread = Thread(target=self.wrapper, args=(func, param))
        self.thread.setName("FutureThread")
        self.thread.start()

    def get_result(self):
        self.condition.acquire()
        while not self.done:
            self.condition.wait()
        self.condition.release()
        result = copy.deepcopy(self.result)
        return result

    def wrapper(self, func, param):
        self.condition.acquire()
        self.result = func(*param)
        self.done = True
        self.condition.notify()
        self.condition.release()