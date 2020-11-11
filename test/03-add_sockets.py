# -*- coding:utf-8 -*-
import os
import time
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.process
import tornado.netutil

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(str(os.getpid()))
        time.sleep(10)

if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/',IndexHandler),
    ])
    sockets = tornado.netutil.bind_sockets(8090)
    tornado.process.fork_processes(2)
    server = tornado.httpserver.HTTPServer(app)
    server.add_socket(sockets)
    tornado.ioloop.IOLoop.instance().start()
