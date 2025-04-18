#!/usr/bin/env-python
# -*- coding: utf-8 -*-
"""
@Time 2025/4/18 19:47:33
@Author ShiqiDing
@File config.py
"""


class Config:
    def __init__(self):
        # 关闭wtf的csrf保护
        self.WTF_CSRF_ENABLED = False
