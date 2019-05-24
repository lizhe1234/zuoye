import pymysql
import time
import hashlib


class my_sql():
    def __init__(self):
        self.conn = pymysql.Connect(host='127.0.0.1', user='root', password='123456', db='bbs', port=3306,
                                    charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def sql(self):
        while 1:
            username = input("请输入用户名：").split()[0]
            if len(username) < 2:
                print("对不起输入有误，请重新输入")
            else:
                sql = "select password from user where username='%s'" % username
                res = self.cursor.execute(sql)
                records = self.cursor.fetchall()[0]
                # print(records["password"])
                password1 = input("请输入密码：")
                password = hashlib.sha1(password1.encode('utf8')).hexdigest()
                # print(password)
                if password == records["password"]:
                    print("登录成功")
                    sql = "select * from user where username='%s'" % username
                    res = self.cursor.execute(sql)
                    a = self.cursor.fetchall()[0]
                    # {'uid': 1, 'username': '12', 'usertype': '普通用户',
                     # 'password': '7b52009b64fd0a2a49e6d8a939753077792b0554', 'regtime': '2019年05月24日', 'email': '12'}
                    ps = a["password"][0:20]
                    print("用户名".ljust(5), "用户类型".ljust(8), "密码".ljust(20), "注册时间".ljust(15), "email".ljust(20),"\r\n","{:<5}".format(a["username"]),"{:<5}".format(a["usertype"]),"{}{}".format(ps,"..."),"{:<5}".format(a["regtime"]),"{:<5}".format(a["email"]))

                    break
                else:
                    print("对不起输入有误，请重新输入")







        try:
            # pymysql默认开启事物
            # 插入成功返回1,否则返回0
            res = self.cursor.execute(sql)
            if res:
                self.conn.commit()
                # 获取新增加记录的自增主键值
                # print(self.cursor.lastrowid)

                # 查看sql语句
                # print(self.cursor._executed)
            else:
                self.conn.rollback()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            # 5 关闭连接和游标
            self.cursor.close()
            self.conn.close()


