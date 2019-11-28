#!/usr/bin/env python
# coding: utf-8

'''
@Author: Senkita
'''

import socket
import re
from multiprocessing import Process

def handle_cli(client):
    request_data = client.recv(1024)
    request_content = request_data
    request_line = request_data.splitlines()
    file_path = re.match(r"\w+ +(/[^ ]*) ", request_line[0].decode("utf-8")).group(1)
    if file_path == '/':
        file_path = '/home/用户名/.Handover Manual/index.html'
    
    try:
        with open(file_path, 'rb') as f:
            response_line = 'HTTP/1.1 200 OK\r\n'
            response_header = 'Server: Handover Manual\r\n'
            response_body = f.read().decode("utf-8")
    except IOError:
        response_line = 'HTTP/1.1 404 Not Found\r\n'
        response_header = 'Server: Handover Manual\r\n'
        response_body = '''
        <!Doctype HTML>
        <html>
            <head>
                <meta charset="utf-8">
                <title>404 Not Found</title>
                <style type="text/css">
                    body {
                        margin: 0 auto;
                        text-align: center;
                        font-size: 72px
                    }
                </style>
            </head>
            <body>
                <p>The Page Is Missing!</p>
                <p>(╯￣^￣)╯︵ ┻━━━┻</p>
                <p>很气！页面自己走丢了！</p>
            </body>
        </html>
        '''
    finally:
        response = response_line + response_header + '\r\n' +response_body
        client.send(bytes(response, 'utf-8'))
        client.close()
        

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        s.bind(('', 8000))
        s.listen()
        while True:
            conn, addr = s.accept()
            Process(target=handle_cli, args=(conn, )).start()
            conn.close()

if __name__ == "__main__":
    main()
