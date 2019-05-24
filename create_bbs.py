import pymysql
import settings

# 连接数据库
conn = pymysql.Connect(**settings.paramters)

# 创建游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# print(cursor)

# # 执行sql语句


sql1 = "create database bbs default charset=utf8;"

sql2 = "use bbs;"

sql3 = "create table user(uid int(10) auto_increment, username varchar(8) not null unique , usertype enum('普通用户','管理员') default '普通用户', password varchar(40), regtime varchar(11), email varchar(20), primary key(uid));"

# sql = """
# create database bbs default charset=utf8;
#  use bbs;
#  create table user(uid int(10) auto_increment, username varchar(8) not null unique , usertype enum('普通用户','管理员') default '普通用户', password varchar(40), regtime datetime, email varchar(20), primary key(uid));
#
#
# """

try:


    res = cursor.execute(sql1)
    res = cursor.execute(sql2)
    res = cursor.execute(sql3)
except Exception as e:
    print(e)
finally:
    # 5 关闭连接和游标
    cursor.close()
    conn.close()

