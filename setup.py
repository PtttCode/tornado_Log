#!/usr/bin/env python
from setuptools import setup

setup(
    name='ptttloggg',    # 包名称，之后如果上传到了pypi，则需要通过该名称下载
    version='0.0.3',  # version只能是数字，还有其他字符则会报错
    keywords=['log', 'easy'],
    description='web_log',
    license='MIT',   # 遵循的协议
    author='pangtong',
    author_email='tongpang@webot.com',
    platforms='any',
    url="https://github.com/desion/tidy_page",     # 项目链接,
    include_package_data=True,
    entry_points={},
    packages=['ptttloggg']
)
