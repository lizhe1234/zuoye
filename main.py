import create_bbs
import zc
import dl

def xx():
    print("注册用户请按1","登录系统请按2")
    a = input("请输入")
    if int(a) == 1:
        ab = zc.my_sql()
        ab.sql()
    if int(a) == 2:
        abc = dl.my_sql()
        abc.sql()


if __name__ == '__main__':
    xx()
