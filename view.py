# 用于提取环境信息
import os
def gainDetails(str):
    listb =str.split(' ')
    if str == "ceph -s":
        mystr = os.popen("ceph -s",shell = true)  # popen与system可以执行指令,popen可以接受返回对象
        mystr = mystr.read()  # 读取输出
        list = mystr.split(' ')
            if ('e17:' in list):  # 提取年、周...转换类型计算
                x = list[list.index('e17:,') - 1]
            if ('osd:' in list):
                y = list[list.index('osd:') - 1]
            if ('up,' in list):
                z = list[list.index('up,') - 1]
        array=[x,y,z]
        return array
    if str == "fdisk –l":
        mystr = os.popen("fdisk –l", shell=true)  # popen与system可以执行指令,popen可以接受返回对象
        mystr = mystr.read()  # 读取输出
        list = mystr.split(' ')
        if ('MiB' in list):  # 提取年、周...转换类型计算
            x = list[list.index('MiB') + 1]
        if ('bytes' in list):
            y = list[list.index('bytes') + 1]
        if ('up,' in list):
            z = list[list.index('sector') - 1]
        array=[x,y,z]
        return array
    if str =="rdb -ls" :
        mystr = os.popen(str, shell=true)  # popen与system可以执行指令,popen可以接受返回对象
        mystr = mystr.read()  # 读取输出
        list = mystr.split(' ')
        return mystr
    if listb[1] == info :
        mystr = os.popen("rbd info",listb[2], shell=true)  # popen与system可以执行指令,popen可以接受返回对象
        mystr = mystr.read()  # 读取输出
        list = mystr.split(' ')
        if ('MiB' in list):  # 提取年、周...转换类型计算
            x = list[list.index('MiB') + 1]
        if ('bytes' in list):
            y = list[list.index('bytes') + 1]
        if ('sectors' in list):
            z = list[list.index('sectors') + 1]
        array = [x, y, z]
        return array
    """if listb[1] == map:
        mystr = os.popen("rbd map", listb[2], shell=true)  # popen与system可以执行指令,popen可以接受返回对象
        mystr = mystr.read()  # 读取输出
        list = mystr.split(' ')
        if ('MiB' in list):  # 提取年、周...转换类型计算
            x = list[list.index('MiB') + 1]
        if ('bytes' in list):
            y = list[list.index('bytes') + 1]
        if ('sectors' in list):
            z = list[list.index('sectors') + 1]
        array = [x, y, z]
        return array"""

