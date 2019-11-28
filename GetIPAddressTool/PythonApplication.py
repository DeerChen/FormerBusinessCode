#!/usr/bin/env python
# coding: utf-8

'''
@Author:Senkita
'''

import socket
import PySimpleGUI as sg

def user_interface(host_name, ip_address):
    sg.Popup('Message', '{}的内网地址为:{}'.format(host_name, ip_address))

def main():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    user_interface(host_name, ip_address)
    
if __name__ == '__main__':
    main()
