# @Time    : 2021/9/16 17:57
# @Author  : wanglinxian
# @Email   : wanglinxian@uino.com
# @File    : db_operate.py
# @Software: PyCharm
# @Description: 数据库相关操作

import psycopg2
import pymysql


def postgresql_operate(host, port, username, password, database, sql, sql_type='select'):
    conn = psycopg2.connect(host=host, port=port, user=username, password=password, database=database)  # 建立连接
    cursor = conn.cursor()  # 建立游标
    cursor.execute(sql)  # 执行SQL命令
    '''如果是select语句，就返回查询结果'''
    if sql_type == 'select':
        rows = cursor.fetchall()  # 获取查询结果
        if len(rows) > 0:
            cursor.close() # 关闭游标
            conn.close() # 关闭连接
            return rows
        else:
            cursor.close() # 关闭游标
            conn.close() # 关闭连接
            return False
    '''其他语句需要提交SQL，返回执行行数'''
    else:
        conn.commit()  # 提交SQL命令
        rows = cursor.rowcount
        cursor.close() # 关闭游标
        conn.close() # 关闭连接
        return rows

def mysql_operate(host, port, username, password, database, sql, sql_type='select'):
    conn = pymysql.connect(host=host, port=port, user=username, password=password, db=database)
    cursor = conn.cursor()
    cursor.execute(sql)
    if sql_type == 'select':
        result = cursor.fetchall()
        if len(result) > 0:
            cursor.close()
            conn.close()
            return result
        else:
            cursor.close()
            conn.close()
            return False
    else:
        conn.commit()
        rows = cursor.rowcount
        cursor.close()
        conn.close()
        return rows
