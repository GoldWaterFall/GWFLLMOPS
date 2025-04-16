#!/usr/bin/env-python
# -*- coding: utf-8 -*-
"""
@Time 2025/4/16 13:01:56
@Author ShiqiDing
@File app.py
"""

from injector import Injector

from internal.router import Router
from internal.server.http import Http

injector = Injector()

app = Http(__name__, router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)
