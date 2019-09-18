import pymssql

server = "127.0.0.1"    # 连接服务器地址
user = "sa" # 连接帐号
password = "w1121382295"# 连接密码

conn = pymssql.connect(server, user, password, "test")  #获取连接

cursor = conn.cursor() # 获取光标

# 创建表
cursor.execute("""
IF OBJECT_ID('persons', 'U') IS NOT NULL
    DROP TABLE persons
    CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
)
""")

# 插入多行数据
cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.')])
# 你必须调用 commit() 来保持你数据的提交如果你没有将自动提交设置为true
conn.commit()

# 查询数据
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')

# 遍历数据（存放到元组中） 方式1
row = cursor.fetchone()
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()

# 遍历数据（存放到元组中） 方式2
for row in cursor:
    print('row = %r' % (row,))


# 遍历数据（存放到字典中）
# cursor = conn.cursor(as_dict=True)
#
# cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
# for row in cursor:
#     print("ID=%d, Name=%s" % (row['id'], row['name']))
#
# conn.close()
# 关闭连接
conn.close()

# 注：在任何时候，在一个连接下，一次正在执行的数据库操作只会出现一个cursor对象

