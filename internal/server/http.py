#!/usr/bin/env-python
# -*- coding: utf-8 -*-
"""
@Time 2025/4/16 12:52:01
@Author ShiqiDing
@File http.py
"""

from flask import Flask

from internal.router import Router


class Http(Flask):
    '''Http服务引擎'''

    def __init__(self, *args, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)
