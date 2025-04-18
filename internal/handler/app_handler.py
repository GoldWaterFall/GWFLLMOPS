#!/usr/bin/env-python
# -*- coding: utf-8 -*-
"""
@Time 2025/4/16 12:37:02
@Author ShiqiDing
@File app_handler.py
"""
import os

from flask import request
from openai import OpenAI


class AppHandler:
    '''应用控制器'''

    def completion(self):
        '''聊天接口'''
        # 1.提取从接口中获取的输入
        query = request.json.get('query')
        # 2.构建OpenAI客户端，并发起请求
        client = OpenAI(
            # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
            api_key=os.getenv("OPENAI_API_KEY"),
            # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
            base_url=os.getenv("BASE_URL")
        )
        # 3.得到请求响应，然后将OpenAI的响应传递给前端
        completion = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=[
                {"role": "system", "content": "你是OpenAI开发的聊天机器人，请根据用户输入回复对应消息"},
                {"role": "user", "content": query},
            ]
        )

        content = completion.choices[0].message.content
        return content

    def ping(self):
        return {'ping': 'pong'}
