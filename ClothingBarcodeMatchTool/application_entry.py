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

def timer(start_time, barcode_count, tag_count):
    layout = [
        [sg.T(barcode_count)],
        [sg.T(tag_count)],
        [sg.T('总用时：{}秒'.format(time.process_time() - start_time))],
        [sg.OK('完成')]
        ]
    window = sg.Window('Timer', layout)
    event, value = window.Read()
    if event in (None, '完成'):
        window.Close()

def main():
    try:
        file_path, match_file_path, barcode_choice, tag_choice = user_interface()
        start_time = time.process_time()
        bp = background_processing.BackgroundProcessing(file_path, match_file_path, barcode_choice, tag_choice)
        barcode_count, tag_count = bp.match_barcode()
        timer(start_time, barcode_count, tag_count)
    except:
        sys.exit(0)

if __name__ == '__main__':
    main()
