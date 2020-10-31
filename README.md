pyregedit
==============

 - 该项目用于操作注册表，读写注册表的键和值
 - 兼容windows 64位和32位
 - 代码在python2.7开发和测试，应该兼容python3。欢迎下载并测试
 - 博客地址：http://yshblog.com/blog/132

使用方法：
-----
 1. 需要安装pywin32： pip install pywin32
 2. 把pyregedit加入你的项目中
 3. 代码示例
    ```python
    #coding:utf-8
    import pyregedit

    root = pyregedit.HKEY_LOCAL_MACHINE
    path = r"SOFTWARE\Microsoft\test"
    reg = pyregedit.RegEdit(root, path)

    #判断键是否存在
    if reg.check_key():
        #获取键(可用于其他操作)
        key = reg.get_key()
    else:
        #创建键
        key = reg.create_key()

    #创建值
    reg.create_value('test_name', pyregedit.REG_SZ, 'this is a test code')

    #创建子键
    reg.create_sub_key('sub_test')

    #获取子键名称列表
    print(list(reg.get_sub_keys()))

    #获取全部值
    print(list(reg.get_values()))

    #根据具体名称获取某个值的数据
    print(reg.get_value('test_name'))

    #删除值
    reg.delete_value('test_name')

    #删除子键
    reg.delete_sub_key('sub_test')

    #删除当前键
    reg.delete_current_key()
    ```
