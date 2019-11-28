#!/usr/bin/env python
# coding: utf-8

'''
@Author: Senkita
'''

import PySimpleGUI as sg

def user_interface():
    layout = [
        [sg.T('备件库退货模板XLSM文件路径：')],
        [sg.I(size=(40, None), disabled=True), sg.FileBrowse(button_text='打开', file_types=(('备件库退货模板', '备件库退货模板.xlsm'),))],
        [sg.Submit('确认'), sg.Cancel('取消')]
        ]
    window = sg.Window('Source File Selector', layout)

    event, value = window.Read()
    if event == '确认':
        window.Close()
        if '' in value.values():
            warnning_window = sg.Popup('警告！', '存在漏填项！')
            if warnning_window in (None, 'OK'):
                return user_interface()
        else:
                return value[0]
    elif event in (None, '取消'):
        window.Close()
