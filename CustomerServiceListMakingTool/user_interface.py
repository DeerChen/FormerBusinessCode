#!/usr/bin/env python
# coding: utf-8

'''
@Author: Senkita
'''

import PySimpleGUI as sg
from datetime import datetime

def user_interface():
    date = datetime.strftime(datetime.now(), '%Y%m%d')
    year = date[:4]
    month = date[4:6]
    defult_order_num = date + '001'

    layout = [
        [sg.T('配货单号(0-9000)：2K{}'.format(date[2:])), sg.I(size=(4, None), default_text='1111'), sg.T('NY')],
        [sg.T('总运单号：'), sg.I(size=(12, None), default_text=defult_order_num)],
        [sg.T('航班日期：{}年'.format(year)), sg.I(size=(2, None), default_text=month), sg.T('月'), sg.I(size=(2, None)), sg.T('日')],
        [sg.T('物流公司：'), sg.Combo(['圆通速递', '韵达速递'], size=(10, None))],
        [sg.T('发货商品详情导出CSV文件路径：')],
        [sg.I(size=(40, None), disabled=True), sg.FileBrowse(button_text='打开', file_types=(('发货商品详情', '*.csv'),))],
        [sg.Submit('确认'), sg.Cancel('取消')]
        ]
    window = sg.Window('模板必填项', layout)

    event, value = window.Read()
    if event == '确认':
        window.Close()
        if '' in value.values():
            warnning_window = sg.Popup('警告！', '存在漏填项！')
            if warnning_window in (None, 'OK'):
                return user_interface()
        else:
            try:
                splicing_date = '{}{:0>2d}{:0>2d}'.format(year, int(value[2]), int(value[3]))
                flight_date = datetime.strptime(splicing_date, '%Y%m%d')
                if 0 <= int(value[0]) <= 9000:
                    return date, value[0], value[1], flight_date, value[4], value[5]
            except:
                warnning_window = sg.Popup('警告！', '配货单号限填0~9000的数字！', '日期填写是否规范？')
                if warnning_window in (None, 'OK'):
                    return user_interface()
    elif event in (None, '取消'):
        window.Close()