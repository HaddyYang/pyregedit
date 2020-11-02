# coding: utf-8

import os
from setuptools import find_packages, setup
from pyregedit import AUTHOR, NAME, VERSION, WEBSITE

description = "registry edit (注册表操作)"

try:
    with open('README.md', encoding='utf-8') as md:
        long_description = md.read()
except Exception:
    long_description = description

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    url=WEBSITE,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License',
    packages=find_packages(),
    platforms=['win32', 'win_amd64'],
    install_requires=['pywin32>=228'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ],
    keywords=['registry edit'],
)
