#!/usr/bin/env-python
# -*- coding: utf-8 -*-
"""
@Time 2025/4/18 20:26:45
@Author ShiqiDing
@File http_code.py
"""
from enum import Enum


class HttpCode(str, Enum):
    '''HTTP基础业务状态码'''
    SUCCESS = "success"
    FAIL = "fail"
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"
    VALIDATE_ERROR = "validate_error"
