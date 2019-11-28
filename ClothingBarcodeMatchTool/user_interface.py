#!/usr/bin/env python
# coding: utf-8

'''
@Author: Senkita
'''

import PySimpleGUI as sg

def user_interface():
    layout = [
        [sg.T('男装总表XLSX文件路径：')],
        [sg.I(size=(40, None), disabled=True), sg.FileBrowse(button_text='打开', file_types=(('男装总表', '男装总表.xlsx'),))],
        [sg.T('条码匹配模板XLSM文件路径：')],
        [sg.I(size=(40, None), disabled=True), sg.FileBrowse(button_text='打开', file_types=(('条码匹配模板', '条码匹配模板.xlsm'),))],
        [sg.T('勾选匹配种类：'), sg.Checkbox('条码', default=True), sg.Checkbox('吊牌')],
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
            if value[2] == False and value[3] == False:
                warnning_window = sg.Popup('警告！', '匹配种类至少要选择一项！')
                if warnning_window in (None, 'OK'):
                    return user_interface()
            else:
                return value[0], value[1], value[2], value[3]
    elif event in (None, '取消'):
        window.Close()
