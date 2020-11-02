# coding:utf-8
"""
    author:     Haddy Yang (杨仕航)
    descript:   registry edit (注册表操作)
    update:     2020-11-1
    preinstall: pywin32
"""
import os

# 需要安装pywin32
import win32api
import win32con

# 权限设置
REG_FLAGS = (
    win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS
)

# root (根节点)
HKEY_CLASSES_ROOT = win32con.HKEY_CLASSES_ROOT
HKEY_CURRENT_USER = win32con.HKEY_CURRENT_USER
HKEY_LOCAL_MACHINE = win32con.HKEY_LOCAL_MACHINE
HKEY_USERS = win32con.HKEY_USERS
HKEY_CURRENT_CONFIG = win32con.HKEY_CURRENT_CONFIG

# value type (值类型)
REG_SZ = win32con.REG_SZ
REG_BINARY = win32con.REG_BINARY
REG_DWORD = win32con.REG_DWORD
REG_QWORD = win32con.REG_QWORD
REG_MULTI_SZ = win32con.REG_MULTI_SZ
REG_EXPAND_SZ = win32con.REG_EXPAND_SZ


class RegEdit:
    def __init__(self, root, path):
        """init method (key root, key path)"""
        self.root = root
        self.path = path

    # 判断键是否存在
    def check_key(self):
        """check key is exist or not"""
        try:
            key = self.get_key()
            key.close()
            return True
        except Exception as e:
            return False

    # 获取键
    def get_key(self):
        """get key object"""
        key = win32api.RegOpenKeyEx(self.root, self.path, 0, REG_FLAGS)
        return key

    # 获取子键名称
    def get_sub_keys(self):
        """get key's sub keys"""
        key = self.get_key()

        for item in win32api.RegEnumKeyEx(key):
            yield item[0]
        key.close()

    # 获取全部值
    def get_values(self):
        """get key's values"""
        key = self.get_key()

        try:
            i = 0
            while True:
                # 循环枚举值
                yield win32api.RegEnumValue(key, i)
                i += 1
        except Exception as e:
            pass
        finally:
            key.close()

    # 根据名称获取值
    def get_value(self, value_name):
        """get value by name"""
        key = self.get_key()
        value, value_type = win32api.RegQueryValueEx(key, value_name)
        return value, value_type

    # 创建键
    def create_key(self):
        """create and return a key"""
        key, _ = win32api.RegCreateKeyEx(self.root, self.path, REG_FLAGS)
        return key

    # 创建子键
    def create_sub_key(self, sub_key_name):
        """create a sub key"""
        sub_key_path = os.path.join(self.path, sub_key_name)
        sub_key, _ = win32api.RegCreateKeyEx(
            self.root, sub_key_path, REG_FLAGS
        )
        return sub_key

    # 创建值
    def create_value(self, value_name, value_type=REG_SZ, value_value=''):
        """create value"""
        key = self.create_key()
        win32api.RegSetValueEx(key, value_name, 0, value_type, value_value)

        key.close()
        return True

    # 删除当前键
    def delete_current_key(self):
        """delete current key"""
        parent, key_name = os.path.split(self.path)
        key_parent = win32api.RegOpenKeyEx(self.root, parent, 0, REG_FLAGS)
        win32api.RegDeleteKeyEx(key_parent, key_name)

        key_parent.close()
        return True

    # 删除子键
    def delete_sub_key(self, sub_key_name):
        """delete sub key"""
        key = self.get_key()
        win32api.RegDeleteKeyEx(key, sub_key_name)

        key.close()
        return True

    # 删除值
    def delete_value(self, value_name):
        """delete a value item"""
        key = self.get_key()
        win32api.RegDeleteValue(key, value_name)

        key.close()
        return True
