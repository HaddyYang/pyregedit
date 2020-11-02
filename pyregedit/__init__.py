# coding: utf-8

from .pyregedit import (
    RegEdit,
    # 权限设置
    REG_FLAGS,
    # root (根节点)
    HKEY_CLASSES_ROOT,
    HKEY_CURRENT_USER,
    HKEY_LOCAL_MACHINE,
    HKEY_USERS,
    HKEY_CURRENT_CONFIG,
    # value type (值类型)
    REG_SZ,
    REG_BINARY,
    REG_DWORD,
    REG_QWORD,
    REG_MULTI_SZ,
    REG_EXPAND_SZ,
)

__all__ = [
    "RegEdit",
    # 权限设置
    "REG_FLAGS",
    # root (根节点)
    "HKEY_CLASSES_ROOT",
    "HKEY_CURRENT_USER",
    "HKEY_LOCAL_MACHINE",
    "HKEY_USERS",
    "HKEY_CURRENT_CONFIG",
    # value type (值类型)
    "REG_SZ",
    "REG_BINARY",
    "REG_DWORD",
    "REG_QWORD",
    "REG_MULTI_SZ",
    "REG_EXPAND_SZ",
]

NAME = "pyregedit"
VERSION = "1.0.0"
AUTHOR = "Haddy Yang (杨仕航)"
WEBSITE = "https://github.com/HaddyYang/pyregedit"
