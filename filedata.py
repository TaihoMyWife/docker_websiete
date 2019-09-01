#!/usr/bin/env python
#coding=utf-8


import os

def file(str):
    print('this ')
    # dirname,subdirList,fileList=os.walk("/", topdown=False)
    # print(dirname)
    dir=[]
    f=[]
    size=[]
    rootDir = str
    for dirName, subdirList, fileList in os.walk(rootDir):
     print('Found directory: %s' % dirName)
     for dirname in subdirList:
         print('\t%s' % dirname)
         #size.append("文件夹")
         dir.append(dirname)
     print("filename")
     for fname in fileList:
         print('\t%s' % fname)
         f.append(fname)
     break

    return dir,f


def search_file(str,match):
    print('this ')
    # dirname,subdirList,fileList=os.walk("/", topdown=False)
    # print(dirname)
    dir=str
    searchdir=[]
    searchfile=[]
    rootDir = str
    for dirName, subdirList, fileList in os.walk(rootDir):
     print('Found directory: %s' % dirName)
     for dirname in subdirList:
         print('\t%s' % dirname)
         if match==dirname:
            searchdir.append(dirName+'/'+dirname)
     print("filename")
     for fname in fileList:
         print('\t%s' % fname)
         if match==fname:
            searchfile.append(dirName+'/'+fname)

    return searchdir,searchfile

def search(path,name):

    for root, dirs, files in os.walk(path):  # path 为根目录
        if name in files:
            flag = 1      #判断是否找到文件
            root = str(root)
            dirs = str(dirs)
            return os.path.join(root, dirs)
    return -1




