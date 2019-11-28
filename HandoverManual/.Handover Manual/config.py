#!/usr/bin/sh python
# coding: utf-8

'''
@Author: Senkita
'''

from datetime import timedelta

DEBUG = True
SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
PERMANENT_SESSION_LIFETIME = timedelta(seconds=1)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123321@127.0.0.1:3306/unfinished_business?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False