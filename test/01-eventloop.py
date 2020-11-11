# -*- coding:utf-8 -*-

from queue import Queue
from functools import partial

enventloop = None

class EventLoop(Queue):
    def start(self):
        while True:
            function = self.get()
            function()


def do_hello():
    global enventloop
    print('hello')
    enventloop.put(do_hello)

def do_world():
    global enventloop
    print('world')
    enventloop.put(do_hello)

if __name__ == '__main__':

    enventloop = EventLoop()
    enventloop.put(do_hello)
    enventloop.put(do_world)
