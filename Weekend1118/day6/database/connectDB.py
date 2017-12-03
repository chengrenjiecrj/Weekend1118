import pymysql

def connDb():
    #使用数据库的ip:port,账号,密码,数据库名称
    db=pymysql.Connect(host = "127.0.0.1",user="root",password="root",database="pirate",port=3306,charset="utf8")

    #查询用户表中数据,倒叙排列
    sql = "select * from hd_user order by id desc"
    #执行sql语句,先获取游标
    curs = db.cursor()
    #通过游标来执行sql语句
    curs.execute(sql)
    #想获取数据库中最新的记录,那么就要把数据库所有数据倒序排列,fetchone()
    result = curs.fetchone()
    #如果想获取所有的查询结果,fetchall
    result1 = curs.fetchall()
    #result = curs.desc;
    return result;


if __name__=='__main__':
    print(connDb())