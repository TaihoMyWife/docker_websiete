#!/usr/bin/python
# coding=utf-8

import re
import datetime
import simplejson
import time
import os
import sys
import pymysql
import filedata
import sys
from shutil import copyfile #copy
#from PIL import Image
from flask import Flask, render_template, jsonify, request, redirect, url_for,flash,current_app
'''
from cpuidle import timess,values
from cpuwait import timess1,values1
from cpunice import timess2,values2
from cpusoftirq import timess3,values3

from membuffer import timessmem,valuesmem
from memcache import valuesmem1
from memfree import valuesmem2
from memused import valuesmem3
from ioerrosrx import timessio,valuesio
from ioerrostx import valuesio1
from iooctetsrx import valuesio2
from iooctetstx import valuesio3

from diskblock import timessdisk,valuesdisk
from diskrunning import valuesdisk1
from disksleeping import valuesdisk2
from diskstopped import valuesdisk3
'''



import  paramiko


app = Flask(__name__)
app.config.from_object('config')
global root
root = '/'
global name
global password
#fn = getattr(sys.modules['__main__'], '__file__')
#basedir = os.path.dirname('__file__')
#print(basedir)
db = pymysql.connect("202.117.10.235", "root", "root", "cloud") #"root", "wykl0920", "cloud"
aimlocation = r'C:\Users\19371\Desktop\Dockerfile'
commandsA= 'dir /a'
commandsb= ''#docker 执行
#Dockerfile 执行文件夹
@app.route('/jiedian', methods=['POST','GET']) #这里不能post和get同时写
def jiedian():
    print('denglu')
    cursor = db.cursor()

    #如果是刚登录的话是收不到节点页面传来的nodeid信息，所以直接跳到最初的页面

    nameuser=request.args.get('username')
    print(nameuser)

    password=request.args.get('password')
    print(password)
    #要删除的节点id
    nodeid = request.args.get('nodeID')
    #登录模块
    if nameuser==None:  #不是从登录界面转过来的，就是删除操作
        if password==None and nodeid==None:
            return render_template('./login.html')
        else:
            cursor.execute("delete from node where nodeid=%s",nodeid)
            db.commit()
            return render_template('./jiedian.html')
    else:
        cursor.execute("select * from user1 where iden='"+nameuser+"'and password='"+password+"' and index1='1'")             ####
        result=cursor.fetchall()
        print(result)
        #该用户不存在
        res="1"
        if not result:
            return render_template('./login.html', res= '用户名密码不正确')
        else:
            cursor.execute("select authority from user1 where iden=%s", nameuser)
            auth = cursor.fetchone()

            print(1)
            print(auth)
            if auth==None:
                return render_template('./jiedian.html')

            else:
                rootuer=[]
                # 返回
                if auth[0]=='1':
                    rootuer.append(nameuser)
                    rootuer.append(password)
                    return render_template('./jiedian.html',rootuer=rootuer)
                else:
                    if auth[0]=='0':
                        return render_template('./shili2.html')
                    else:
                        return render_template('./blank.html')


@app.route('/shili', methods=['POST','GET'])
def shili():
    print("haha")
    shilicursor=db.cursor()
    #print(request.stream.read())
    nodeid=request.args.get('jiedianID')
    nodename=request.args.get('jiedianName')
    address=request.args.get('address')
    port=request.args.get('port')
    state=request.args.get('state')
    createtime=request.args.get('createtime')
    caseid=request.args.get('caseID')
    print(nodeid,nodename,address,port,state,createtime,caseid)
    if nodeid==None:
        if caseid==None:
            #shilicursor.execute()
            return render_template('./shili.html')
        else:
            shilicursor.execute("delete from case1 where caseid=%s",caseid)
            db.commit()
            return render_template('./shili.html')
    else:

        shilicursor.execute("update case1 set casename = '"+nodename+"',ip='"+address+"',port='"+str(port)+"',createtime='"+createtime+"' where caseid='"+nodeid+"'")

        db.commit()
        return render_template('./shili.html')

@app.route('/shili2')
def shili2():
    return render_template('./shili2.html')

@app.route('/sketch/')
def hello():
    return render_template('sketch.html')

@app.route('/sketch/monitor', methods=['POST', 'GET']) #show docker
def monitor():
    a=os.popen(commandsA)
    monitor = a.read()
    return render_template(monitor)

@app.route('/sketch/delete', methods=['POST', 'GET']) #paste the dockerfile
def delete():
    path = request.args.get('path')
    path_ = request.args.get('path_')
    #print("123"+path)
    #print(path)
    if os.path.isfile(path):
        copyfile(path, aimlocation )
        #os.system(commandsB)
        os.remove(path)
        return render_template('demo.html')

@app.route('/demo')
def gotoDemo():
    return render_template('demo.html')
@app.route('/sketch/upload', methods=['POST', 'GET']) #upload page
def upload():
    if request.method == 'POST':
        f = request.files['files[]']

        print(f)
        filename = f.filename  # 获取接收到的文件名
        print(filename)
        minetype = f.content_type  # 文件类型
        print(minetype)

        now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')  # 获取本地时间，进行图片重命名
        dir = '/static/temp-img/rough/' + now_time
        # ‘static/temp-img/rough/’是我们预设置的路径，用来暂时存储原图片

        os.makedirs(dir)
        filepath = dir + "/" + now_time + "." + filename.split(".")[1]  # 但别忘记我们还需要获得图片格式（扩展名，可能是.jpg，.png等）

        f.save(filepath)  # 将文件存储下来

        filepath_ = dir + "/" + now_time + "." + filename.split(".")[1]
        # ‘static/temp-img/simplified/’也是我们预设置的路径，用来暂时存储结果图片
        #img_.save(filepath_)

        # 最后我们就可以返回对应的路径啦
        return simplejson.dumps({
            "files":
                [{
                    "name": filename,
                    "mintype": minetype,
                    "filepath": filepath,
                    "filepath_": filepath_
                }]
        })
    else:
        return render_template('demo.html')

@app.route('/info')
def info():
    return render_template('./info.html')

@app.route('/shiliinfo')
def shiliinfo():
    return render_template('./shiliinfo.html')

@app.route('/editnode')
def editnode():
    return render_template('./editnode.html')

@app.route('/addnode')
def addnode():
    return render_template('./addnode.html')


@app.route('/editshili')
def editshili():
    return render_template('./editshili.html')

#用户管理
@app.route('/user-manage')
def usermanage():
    return render_template('./user-manage.html')

#用户展示模块
@app.route('/show_user')
def show_user():
    print("123")
    cursoregister=db.cursor()
    cursoregister.execute("select * from user1 where index1 = '1'")
    userregister1=[]
    statue="0"
    try:
        userregister1=list(cursoregister.fetchall())
        print(userregister1)
        statue="1"
    except e:
        print(e)
    finally:
        return jsonify({'userregister1':userregister1,"statue":statue})

@app.route('/show_node')
def show_node():
    print("123")
    cursornode=db.cursor()
    cursornode.execute("select * from node order by createtime")
    shownode=[]
    statue="0"
    try:
        shownode=list(cursornode.fetchall())
        print(cursornode)
        statue="1"
    except e:
        print(e)
    finally:
        return jsonify({'shownode':shownode,"statue":statue})

@app.route('/show_case')
def show_case():
    print("123")
    cursorcase=db.cursor()
    cursorcase.execute("select * from case1 order by createtime")
    showcase=[]
    statue="0"
    try:
        showcase=list(cursorcase.fetchall())
        print(cursorcase)
        statue="1"
    except e:
        print(e)
    finally:
        return jsonify({'showcase':showcase,"statue":statue})


#用户管理
@app.route('/user-register')
def userregister():
    print("123")
    cursoregister=db.cursor()
    cursoregister.execute("select * from user1 order by createtime desc limit 1 ")
    userregister1=list(cursoregister.fetchone())
    #shell
    print(userregister1)
    return render_template('./user-register.html',userregister1=userregister1)

@app.route('/show_register')
def show_register():
    print("123")
    cursoregister=db.cursor()
    cursoregister.execute("select * from user1 where index1 = '0' order by createtime")
    userregister1=[]
    statue="0"
    try:
        userregister1=list(cursoregister.fetchall())
        print(userregister1)
        statue="1"
    except e:
        print(e)
    finally:
        return jsonify({'userregister1':userregister1,"statue":statue})


@app.route('/show_blocked_register')
def show_blocked_register():
    print("123")
    cursoregister=db.cursor()
    cursoregister.execute("select * from user1 where index1 = '2' order by createtime")
    userregister1=[]
    statue="0"
    try:
        userregister1=list(cursoregister.fetchall())
        print(userregister1)
        statue="1"
    except e:
        print(e)
    finally:
        return jsonify({'userregister1':userregister1,"statue":statue})

@app.route('/add_register')
def add_register():
    print("123")
    rootname = request.args.get('name')
    print(rootname)
    cursoregister=db.cursor()
    print("update user1 set index = '1' where username ='"+rootname+"'")
    cursoregister.execute("update user1 set index1 = '1' where username ='"+rootname+"'")
    db.commit()
    cursor=db.cursor
    cursor.execute("select password from user1 where username='"+rootname+"'")
    password=cursor.fetchone()
    cmd='expect ./static/shell/test.sh '+rootname+' '+password[0]
    data=os.system(cmd)                                                  #点点
    print(data)
    return render_template('./user-register.html')


#文件管理
@app.route('/file-manage')
def filemanage():
    return render_template('./file-manage.html')

@app.route('/file-manage2')
def filemanage2():
    return render_template('./file-manage2.html')
#监控
#@app.route('/001-cpu')
#def CPU1():
#    return render_template('./001-cpu.html')

#容错
@app.route('/fault-tolerant')
def faulttolerant():
    return render_template('./fault-tolerant.html')

@app.route('/index2')
def index2():
    return render_template('./index2.html')

@app.route('/chartjs')
def chartjs():
    legend = 'Monthly Data'
    gettime = timess
    getvalue = values
    num=0
    for i in getvalue:
        if i=='None':
            getvalue[num]=0
        num=num+1
    getvalue1 = values1
    gettime1 = timess1
    num1 = 0
    for i1 in getvalue1:
        if i1 == 'None':
            getvalue1[num1] = 0
        num1 = num1 + 1
    getvalue2 = values2
    num2 = 0
    for i2 in getvalue2:
        if i2 == 'None':
            getvalue2[num2] = 0
        num2 = num2 + 1

    getvalue3 = values3
    num3 = 0
    for i3 in getvalue3:
        if i3 == 'None':
            getvalue3[num3] = 0
        num3 = num3 + 1

    return render_template('./pages/charts/chartjs.html', getvalue=getvalue,gettime=gettime, legend=legend, getvalue1=getvalue1,gettime1=gettime1,getvalue2=getvalue2,getvalue3=getvalue3)

@app.route('/chartjs-mem')
def chartjsmem():
    legend = 'Monthly Data'
    gettime = timessmem
    getvalue = valuesmem
    num=0
    for i in getvalue:
        if i=='None':
            getvalue[num]=0
        num=num+1
    getvalue1 = valuesmem1
    num1 = 0
    for i1 in getvalue1:
        if i1 == 'None':
            getvalue1[num1] = 0
        num1 = num1 + 1
    getvalue2 = valuesmem2
    num2 = 0
    for i2 in getvalue2:
        if i2 == 'None':
            getvalue2[num2] = 0
        num2 = num2 + 1

    getvalue3 = valuesmem3
    num3 = 0
    for i3 in getvalue3:
        if i3 == 'None':
            getvalue3[num3] = 0
        num3 = num3 + 1

    return render_template('./pages/charts/chartjs-mem.html', getvalue=getvalue,gettime=gettime, legend=legend, getvalue1=getvalue1,getvalue2=getvalue2,getvalue3=getvalue3)

@app.route('/chartjs-io')
def chartjsio():
    legend = 'Monthly Data'
    gettime = timessio
    getvalue = valuesio
    num=0
    for i in getvalue:
        if i=='None':
            getvalue[num]=0
        num=num+1
    getvalue1 = valuesio1
    num1 = 0
    for i1 in getvalue1:
        if i1 == 'None':
            getvalue1[num1] = 0
        num1 = num1 + 1
    getvalue2 = valuesio2
    num2 = 0
    for i2 in getvalue2:
        if i2 == 'None':
            getvalue2[num2] = 0
        num2 = num2 + 1

    getvalue3 = valuesio3
    num3 = 0
    for i3 in getvalue3:
        if i3 == 'None':
            getvalue3[num3] = 0
        num3 = num3 + 1

    return render_template('./pages/charts/chartjs-io.html', getvalue=getvalue,gettime=gettime, legend=legend, getvalue1=getvalue1,getvalue2=getvalue2,getvalue3=getvalue3)

@app.route('/chartjs-disk')
def chartjsdisk():
    legend = 'Monthly Data'
    gettime = timessdisk
    getvalue = valuesdisk
    num=0
    for i in getvalue:
        if i=='None':
            getvalue[num]=0
        num=num+1
    getvalue1 = valuesdisk1
    num1 = 0
    for i1 in getvalue1:
        if i1 == 'None':
            getvalue1[num1] = 0
        num1 = num1 + 1
    getvalue2 = valuesdisk2
    num2 = 0
    for i2 in getvalue2:
        if i2 == 'None':
            getvalue2[num2] = 0
        num2 = num2 + 1

    getvalue3 = valuesdisk3
    num3 = 0
    for i3 in getvalue3:
        if i3 == 'None':
            getvalue3[num3] = 0
        num3 = num3 + 1

    return render_template('./pages/charts/chartjs-io.html', getvalue=getvalue,gettime=gettime, legend=legend, getvalue1=getvalue1,getvalue2=getvalue2,getvalue3=getvalue3)


@app.route('/chartjs2')
def chartjs2():
    legend = 'Monthly Data'
    gettime = timess
    getvalue = values
    num=0
    for i in getvalue:
        if i=='None':
            getvalue[num]=0
        num=num+1
    getvalue1 = values1
    gettime1 = timess1
    num1 = 0
    for i1 in getvalue1:
        if i1 == 'None':
            getvalue1[num1] = 0
        num1 = num1 + 1
    getvalue2 = values2
    num2 = 0
    for i2 in getvalue2:
        if i2 == 'None':
            getvalue2[num2] = 0
        num2 = num2 + 1

    getvalue3 = values3
    num3 = 0
    for i3 in getvalue3:
        if i3 == 'None':
            getvalue3[num3] = 0
        num3 = num3 + 1

    return render_template('./pages/charts/chartjs2.html', getvalue=getvalue,gettime=gettime, legend=legend, getvalue1=getvalue1,gettime1=gettime1,getvalue2=getvalue2,getvalue3=getvalue3)

@app.route('/get_file', methods=['POST', 'GET'])
def get_file():
    id_iterm=['1','2','3']
    rootname = request.args.get('name')
    print(rootname)
    global root
    if root != '/' and rootname!="":
        root = root + '/' + rootname
    else:
        root = root + rootname
    print(root)
    dirname=[]
    filename=[]
    size=[]
    resultfile=[]
    resultdir=[]
    dirname,filename=filedata.file(root)
    print(dirname)
    print(filename)
    t= 'a'
    for file in  filename:
        if t in file:
            resultfile.append("1")
        else:
            resultfile.append("0")
    for file in dirname:
        if t in file:
            resultdir.append("1")
        else:
            resultdir.append("0")
    try:
        for file in filename:
            mid=os.path.getsize(root+file)
            if mid>1024:
                mid=mid/1024
                size.append(str(mid)+'   MB')
            else:
                size.append(str(mid)+'   B')
    except e:
        print (e)
    finally:
        return jsonify({'dirname':dirname,'filename':filename,'size':size,'resultfile':resultfile,'resultdir':resultdir})


@app.route('/get_file_parent', methods=['POST', 'GET'])
def get_file_parent():
    id_iterm=['1','2','3']
    rootname = request.args.get('name')
    print(rootname)
    global root
    count = root.rfind('/')
    if count != 0:
        root = root[0:count]
    else:
        root = '/'
    print(root)
    dirname=[]
    filename=[]
    size=[]
    resultfile=[]
    resultdir=[]
    dirname,filename=filedata.file(root)
    print(dirname)
    print(filename)
    t= 'a'
    for file in  filename:
        if t in file:
            resultfile.append("1")
        else:
            resultfile.append("0")
    for file in dirname:
        if t in file:
            resultdir.append("1")
        else:
            resultdir.append("0")
    try:
        for file in filename:
            mid=os.path.getsize(root+file)
            if mid>1024:
                mid=mid/1024
                size.append(str(mid)+'   MB')
            else:
                size.append(str(mid)+'   B')
    except e:
        print (e)
    finally:
        return jsonify({'dirname':dirname,'filename':filename,'size':size,'resultfile':resultfile,'resultdir':resultdir})


@app.route('/search_file', methods=['POST', 'GET'])
def search_file():
        id_iterm = ['1', '2', '3']
        namematch = request.args.get('name')
        print(namematch)
        global root
        print(root)
        dirname = []
        filename = []
        size = []
        resultfile = []
        resultdir = []
        dirname, filename = filedata.search_file(root,namematch)
        print(dirname)
        print(filename)
        t = 'a'
        for file in filename:
            if t in file:
                resultfile.append("1")
            else:
                resultfile.append("0")
        for file in dirname:
            if t in file:
                resultdir.append("1")
            else:
                resultdir.append("0")
        try:
            for file in filename:
                mid = os.path.getsize(root + file)
                if mid > 1024:
                    mid = mid / 1024
                    size.append(str(mid) + '   MB')
                else:
                    size.append(str(mid) + '   B')
        except e:
            print (e)
        finally:
            return jsonify({'dirname': dirname, 'filename': filename, 'size': size, 'resultfile': resultfile,
                            'resultdir': resultdir})


@app.route('/get_ssh', methods=['POST', 'GET'])
def get_ssh():
    # 创建SSH对象
    # 创建SSH对象
    ssh = paramiko.SSHClient()

    # 把要连接的机器添加到known_hosts文件中
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    ssh.connect(hostname='202.117.10.235', port=22, username="root", password="root")
    cmd = request.args.get('name')
    print(cmd)
    #cmd = 'ls -l;ifconfig'       #多个命令用;隔开
    stdin, stdout, stderr = ssh.exec_command(cmd)

    result = stdout.read()
    if not result:
        result = stderr.read()
    ssh.close()

    print(result.decode())

    #print(result)

    return jsonify({"stdout": result.decode()})

@app.route('/docker_del', methods=['POST', 'GET'])
def docker_del():
    # 创建SSH对象
    ssh = paramiko.SSHClient()

    # 把要连接的机器添加到known_hosts文件中
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    ssh.connect(hostname='202.117.10.235', port=22, username="root", password="root")

    cmd = request.args.get('name')
    print(cmd)
    # cmd = 'ls -l;ifconfig'       #多个命令用;隔开
    stdin, stdout, stderr = ssh.exec_command(cmd)

    result = stdout.read()

    if not result:
        result = stderr.read()
    ssh.close()

    print(result.decode())

    #print(result)

    return jsonify({"stdout": result.decode()})

#登录
@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('./login.html')

#注册
@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('./register.html')

@app.route('/blank', methods=['POST', 'GET'])
def blank():
    return render_template('./blank.html')

@app.route('/authentication', methods=['POST', 'GET'])
def authetication():
    usertime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    iden=request.args.get('iden')
    username=request.args.get('username')
    role=request.args.get('role')
    imageid=request.args.get('imageid')
    password=request.args.get('password')

    idenpassword=request.args.get('idenpassword')
    print(type(iden),username,role,imageid,password,idenpassword)
    cursor_auth=db.cursor()
    cursor_auth.execute("insert into user1 values ('"+iden+"','"+username+"','"+role+"','"+imageid+"','"+password+"','"+idenpassword+"','"+usertime+"','0','0')")
    db.commit()
    cursor_auth.close()
    print("insert into user1 values ('"+iden+"','"+username+"','"+role+"','"+imageid+"','"+password+"','"+idenpassword+"','"+usertime+"','0','0')")
    return render_template('./authentication.html')

@app.route('/ssh_managment', methods=['POST', 'GET'])
def ssh_managment():
    return render_template('./ssh-managment.html')

@app.route('/user_block', methods=['POST', 'GET'])         #用户拉黑
def user_block():
    return render_template('./user-block.html')

@app.route('/block_user', methods=['POST', 'GET'])
def block_user():
    print("123123")

    rootname = request.args.get('name')
    print(rootname)
    cursoregister=db.cursor()
    print("update user1 set index = '2' where username ='"+rootname+"'")
    cursoregister.execute("update user1 set index1 = '2' where username ='"+rootname+"'")
    db.commit()
    f1 = open('/home/chen/Documents/wsgi/static/text/delete_from.txt', 'w')
    f1.writelines(["'CN="+rootname+"\n'"])
    return render_template('./user-manage.html')

@app.route('/revoke_block', methods=['POST', 'GET'])
def revoke_block():
    print("123123")
    rootname = request.args.get('name')
    print(rootname)
    cursoregister=db.cursor()
    print("update user1 set index = '2' where username ='"+rootname+"'")
    cursoregister.execute("update user1 set index1 = '1' where username ='"+rootname+"'")
    db.commit()

    with open('static/text/test.txt', 'w') as g:
        for line in f.readlines():
            if rootname in line:
                return render_template('./user-manage.html')
    return render_template('./user-manage.html')

@app.route('/cert_managment')
def cert_managment():
    return render_template('./cert-manage.html')

@app.route('/delcase')
def delcase():
    return render_template('./delcase.html')

@app.route('/delnode')
def delnode():
    return render_template('./delnode.html')

@app.route('/register_schedule', methods=['POST', 'GET'])
def register_schedule():
    return render_template('./register-schedule.html')

@app.route('/register_result', methods=['POST', 'GET'])
def register_result():
    iden=request.args.get('iden')
    username=request.args.get('username')
    password=request.args.get('password')
    cursoregister=db.cursor()
    print("select * from user1 where iden= '"+iden+"' and username='"+username+"'and password='"+password+"'order by createtime")
    #res_has=cursoregister.execute("select * from user1 where iden= '"+iden+"' and username='"+username+"' and password='"+password+"'order by createtime")
    res_registered=cursoregister.execute("select * from user1 where iden= '"+iden+"' and username='"+username+"' and index1='1"+"' and password='"+password+"'order by createtime")
    res_registering = cursoregister.execute("select * from user1 where iden= '" + iden + "' and username='" + username + "' and index1='0" + "' and password='" + password + "'order by createtime")
    if res_registered==1:
        name=username+".p12"
        if filedata.search(root_path+"/static/text/auth",name)==-1:
            return render_template('./cert-download.html',iden=iden,username=username,name=name)
        else:
            return render_template('./cert-download.html')
    elif res_registering==1:
        return render_template('./register-schedule.html')
    else:
        return render_template('./register-schedule.html')

@app.route('/cert_download', methods=['POST', 'GET'])
def cert_download():
    iden = request.args.get('iden')
    username = request.args.get('username')
    filename = request.args.get('name')
    if filedata.search(root_path+"/static/text/auth", name) == -1:
        return send_from_directory(root_path+'/static/text/auth', filename, as_attachment=True)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
