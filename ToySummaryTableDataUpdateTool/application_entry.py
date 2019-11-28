#!/usr/bin/env python
# coding: utf-8

'''
@Author: Senkita
'''

from user_interface import user_interface
import background_processing
import time
import PySimpleGUI as sg
import sys

def timer(start_time):
    layout = [
        [sg.T('总用时：{}秒'.format(time.process_time() - start_time))],
        [sg.OK('完成')]
        ]
    window = sg.Window('Timer', layout)
    event, value = window.Read()
    if event in (None, '完成'):
        window.Close()

def main():
    try:
        raw_domestic_file_path, raw_imported_file_path = user_interface()
        start_time = time.process_time()
        bp = background_processing.BackgroundProcessing(raw_domestic_file_path, raw_imported_file_path)
        bp.generate_file()
        timer(start_time)
    except:
        sys.exit(0)

if __name__ == '__main__':
    main()
