#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


import BaseHTTPServer
import requests

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('192.168.56.102',12340)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


class ProxyHaddler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''
    代理服务器
    '''
    def do_GET(self):
        headers = {"Host":self.path,
                   "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
                   "Accept-Encoding":"gzip,deflate,sdch,br",
                   "Accept-Language":"zh-CN,zh;q=0.8",
                   "Connection":"keep-alive" }
        request = requests.get(self.path,headers)
        self.send_response(request.status_code)
        self.end_headers()
        self.wfile.write(request.content)

if __name__ == "__main__":
    run(handler_class=ProxyHaddler)
