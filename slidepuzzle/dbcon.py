import pymssql

server = "127.0.0.1"    # 连接服务器地址
user = "sa" # 连接帐号
password = "w1121382295"# 连接密码

def add(time,data):
    conn = pymssql.connect(server, user, password, "test")  # 获取连接
    cursor = conn.cursor()  # 获取光标
    cursor.executemany("INSERT INTO score VALUES ( %s, %s)",[( str(time), str(data))])
    conn.commit()
    conn.close()

def select():
    conn = pymssql.connect(server, user, password, "test")  # 获取连接
    cursor = conn.cursor()  # 获取光标
    # 查询数据
    cursor.execute('SELECT * FROM score')
    #cursor.execute('SELECT * FROM score WHERE salesrep=%s', 'John Doe')
    # 遍历数据（存放到元组中） 方式1
    row = cursor.fetchone()
    list1=[]
    while row:
        #print("time=%s, score=%s" % (row[0], row[1]))

        list1.append(row)
        #print(list1)
        row = cursor.fetchone()
    conn.close()
    return list1

def delete(id):
    conn = pymssql.connect(server, user, password, "test")  # 获取连接
    cursor = conn.cursor()  # 获取光标
    cursor.executemany("delete from score where id="+(str(id)))
    conn.commit()
    conn.close()

def update(id):
    pass
# list1=select()
# for i in list1:
#     print(i)
