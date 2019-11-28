#!/usr/bin/env python
# coding: utf-8

'''
@Author: Senkita
'''

import pandas as pd
import PySimpleGUI as sg

pd.set_option('display.float_format',lambda x : '%.0f' % x)
pd.set_option('mode.chained_assignment', None)

class BackgroundProcessing:
    @classmethod
    def __init__(cls, raw_domestic_file_path, raw_imported_file_path):
        cls.raw_domestic_file = pd.read_excel(raw_domestic_file_path)
        cls.raw_imported_file = pd.read_excel(raw_imported_file_path)
        cls.window, cls.progress_bar = cls.progress_bar()

    @classmethod
    def progress_bar(cls):
        layout = [
            [sg.T('请耐心等待…')],
            [sg.ProgressBar(cls.raw_domestic_file.shape[0] + cls.raw_imported_file.shape[0], orientation='h', size=(40, 20), key ='progressbar')]
            ]
        window = sg.Window('Processing…', layout)
        progress_bar = window.FindElement('progressbar')
        return window, progress_bar

    @staticmethod
    def generate_template():
        template = pd.DataFrame(columns=[
            '商品代码（必填）',
            '规格代码',
            '规格名称',
            '商品名称',
            '商品简称',
            '商品条码',
            '重量',
            '体积',
            '打包积分',
            '销售积分',
            '标准进价',
            '标准售价',
            '代理售价',
            '成本价',
            '类别',
            '供应商（名称）',
            '单位（名称）',
            '库存状态',
            '商品备注',
            '商品税号',
            '税率',
            '原产地',
            '供应商货号',
            '保质期',
            '预警天数',
            '生产日期（yy-mm-dd）',
            '图片地址',
            '品牌',
            '税收分类编码',
            '长(CM)',
            '宽(CM)',
            '高(CM)'
            ])
        return template

    @classmethod
    def generate_domestic_file(cls, domestic_file, event):
        for i in range(cls.raw_domestic_file.shape[0]):
            if event == None:
                break
            cls.progress_bar.UpdateBar(i + 1)
            
            domestic_file.loc[i, '商品代码（必填）'] = cls.raw_domestic_file.loc[i, '事业部编码']
            domestic_file.loc[i, '规格代码'] = cls.raw_domestic_file.loc[i, '条码']
            domestic_file.loc[i, '规格名称'] = cls.raw_domestic_file.loc[i, '类目']
            domestic_file.loc[i, '商品名称'] = cls.raw_domestic_file.loc[i, '商品名称']
            domestic_file.loc[i, '商品简称'] = cls.raw_domestic_file.loc[i, '店铺商品名称']
            domestic_file.loc[i, '重量'] = cls.raw_domestic_file.loc[i, '重量（kg）']
            domestic_file.loc[i, '标准进价'] = domestic_file.loc[i, '成本价'] = cls.raw_domestic_file.loc[i, '成本价']
            domestic_file.loc[i, '标准售价'] = cls.raw_domestic_file.loc[i, '市场价']
            domestic_file.loc[i, '类别'], domestic_file.loc[i, '单位（名称）'], domestic_file.loc[i, '库存状态'] = '国产玩具', '个', '正常'
            domestic_file.loc[i, '品牌'] = cls.raw_domestic_file.loc[i, '品牌']

        domestic_file.to_excel('国产玩具.xlsx', index=False)

    @classmethod
    def generate_imported_file(cls, imported_file, event):
        for i in range(cls.raw_imported_file.shape[0]):
            if event == None:
                break
            cls.progress_bar.UpdateBar(i + 1 + cls.raw_domestic_file.shape[0])
            
            imported_file.loc[i, '商品代码（必填）'] = cls.raw_imported_file.loc[i, '事业部编码']
            imported_file.loc[i, '规格代码'] = cls.raw_imported_file.loc[i, '条码（现用）']
            imported_file.loc[i, '规格名称'] = cls.raw_imported_file.loc[i, '类目']
            imported_file.loc[i, '商品名称'] = cls.raw_imported_file.loc[i, '商品名称']
            imported_file.loc[i, '商品简称'] = cls.raw_imported_file.loc[i, '店铺商品名称']
            imported_file.loc[i, '重量'] = cls.raw_imported_file.loc[i, '重量（kg）']
            imported_file.loc[i, '标准进价'] = imported_file.loc[i, '成本价'] = cls.raw_imported_file.loc[i, '成本价']
            imported_file.loc[i, '标准售价'] = cls.raw_imported_file.loc[i, '市场价（京东价）']
            imported_file.loc[i, '类别'], imported_file.loc[i, '单位（名称）'], imported_file.loc[i, '库存状态'] = '进口玩具', '个', '正常'
            imported_file.loc[i, '品牌'] = cls.raw_imported_file.loc[i, '品牌']
            
        imported_file.to_excel('进口玩具.xlsx', index=False)
        
    @classmethod
    def generate_file(cls):
        event, value = cls.window.Read(timeout=0)
        
        domestic_file = cls.generate_template()
        imported_file = cls.generate_template()
        
        cls.generate_domestic_file(domestic_file, event)
        cls.generate_imported_file(imported_file, event)

        cls.window.Close()
