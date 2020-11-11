# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop

import tornado.httpserver

class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write("hello tornado")

# class mainHandler(tornado.web.RequestHandler):
#     def get(self,*args,**kwargs):
#         self.write("hello world")

if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/',IndexHandler),
        # (r'/',mainHandler),
    ])
    # 实例化一个HTTP服务器对象， 匹配app中的路由
    HttpServer = tornado.httpserver.HTTPServer(app)
    # 绑定端口
    HttpServer.bind(8888)
    # 启动的进程数，默认开启一个进程
    HttpServer.start(num_processes=5)
    # app.listen(8888)
    # 开始监听， 坚挺epoll中的请求
    tornado.ioloop.IOLoop.current().start()