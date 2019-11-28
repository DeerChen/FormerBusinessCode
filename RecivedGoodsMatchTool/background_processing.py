#!/usr/bin/env python
# coding: utf-8

'''
@Author: Senkita
'''

import pandas as pd
import re

pd.set_option('mode.chained_assignment', None)

class BackgroundProcessing:
    @classmethod
    def __init__(cls, file_path):
        cls.file = pd.read_excel(file_path, sheet_name='京东下载资料')
        cls.match_file = pd.read_excel(file_path, sheet_name='备件库退货信息')
        cls.style_pattern = re.compile(r'([A-Z]{3}[0-9]{6})')
          
    @classmethod
    def match_received(cls):
        for i in range(cls.file.shape[0]):
            cls.file['商品代码'][i] = re.findall(cls.style_pattern, cls.file['商品名称'][i])[0]
            cls.file['类目'][i] = '配饰'
            if cls.file['商品名称'][i][0] == 'G':
                cls.file['品牌'][i] = 'GLO-STORY'
            elif cls.file['商品名称'][i][0] == 'M':
                cls.file['品牌'][i] = 'MAXVIVI'
                
        for num in cls.match_file['出库单号']:
            index = cls.file[cls.file['出库单号']==num].index
            if index.size == 0:
                pass
            cls.file['收货正品'][index] = 1
            
        for barcode in cls.match_file['备件条码']:
            index = cls.file[cls.file['备件条码']==barcode].index
            if index.size == 0:
                pass
            cls.file['收货正品'][index] = 1
            
        cls.file.to_excel('备件库退货匹配.xlsx', index=False)
