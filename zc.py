import pymysql
import time
import hashlib

class my_sql():
    def __init__(self):
        self.conn = pymysql.Connect(host='127.0.0.1',user='root',password='123456',db='bbs',port=3306,charset='utf8')
# conn = pymysql.Connect(host='127.0.0.1',user='root',
#                        password='123456',db='bbs',port=3306,charset='utf8')
# 2 创建游标

        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    def sql(self):
        while 1:
            username = input("请输入用户名：").split()[0]
            if len(username)<2:
                print("对不起输入有误，请重新输入")
            else:
                sqll = "select username from user where username='%s'" % username
                ress = self.cursor.execute(sqll)
                if ress>0:
                    print("对不起，用户名已存在请重新输入")
                    continue
                # self.cursor.close()
                # self.conn.close()
                #
                break

        while 1:
            password1 = input("请输入密码：")
            password2 = input("请再次输入密码：")
            if password2 == password1:
                password = hashlib.sha1(password1.encode('utf8')).hexdigest()
                break
            else:
                print("对不起密码不一致，请重新输入。")
        emall = input("请输入邮箱：")
        timea = time.strftime("%Y年%m月%d日")
        # 如果字段是字符串，请在字符串两边添加单引号
        # insert into user(username,password,regtime,email) values('li',sha1('aa'),'2019-03-10','245@qq.com')

        sql = """
        insert into user(username,password,regtime,email) values ('%s','%s','%s','%s')
        """ % (username,password,timea,emall)
        # print(sql)



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



