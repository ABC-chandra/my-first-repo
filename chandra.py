import psycopg2
import xlsxwriter

hostname ="54.242.197.47"
database ="edb"
username ="imeidbtrn"
pwd="IMEIDBTRN$VG1228$"
port_id =5444
conn=None
cur =None

conn =psycopg2.connect(
        dbname=database,
        host=hostname,
        user=username,
        password=pwd,
        port=port_id)
cur = conn.cursor()
cur.execute("select empno,ename,job,mgr,hiredate,sal,comm,e.deptno,dname,loc from emp e,dept d where e.deptno=d.deptno")
'''two = conn.cursor()
two.execute("select * from dept")'''
'''empno,ename,job,mgr,hiredate,sal,comm,deptno'''
row=1
col=0

workbook = xlsxwriter.Workbook('Downloads\\join1.xlsx')
worksheet = workbook.add_worksheet('EMP')
for i in cur.fetchall():
    worksheet.write(row, col,  i[0])
    worksheet.write(row, col+1,  i[1])
    worksheet.write(row, col+2,  i[2])
    worksheet.write(row, col+3,  i[3])
    worksheet.write(row, col+4,  i[4])
    worksheet.write(row, col+5,  i[5])
    worksheet.write(row, col+6,  i[6])
    worksheet.write(row, col+7,  i[7])
    worksheet.write(row, col+8,  i[8])
    worksheet.write(row, col+9,  i[9])
    row += 1


worksheet.write(0, 0,  'empno')
worksheet.write(0, 1,  'ename')
worksheet.write(0, 2,  'job')
worksheet.write(0, 3,  'mgr')
worksheet.write(0, 4,  'hiredate')
worksheet.write(0, 5,  'sal')
worksheet.write(0, 6,  'comm')
worksheet.write(0, 7,  'deptno')
worksheet.write(0, 8,  'dname')
worksheet.write(0, 9,  'loc')


'''row=1
worksheet1 = workbook.add_worksheet('Dept')
for i in two.fetchall():
    worksheet1.write(row, col,  i[0])
    worksheet1.write(row, col+1,  i[1])
    worksheet1.write(row, col+2,  i[2])
    row += 1

worksheet1.write(0, 0,  'dpnumber')
worksheet1.write(0, 1,  'dname')
worksheet1.write(0, 2,  'loc')'''
    
    
workbook.close()


========================================


DB connection script



import psycopg2
import pandas as pd
import os
import openpyxl
import sys

hostname ="54.242.197.47"
database ="IMEIDBTRN"
username ="imeidbtrn"
pwd="IMEIDBTRN$VG1228$"
port_id =5444
conn=None
cur =None

conn =psycopg2.connect(
        dbname=database,
        host=hostname,
        user=username,
        password=pwd,
        port=port_id)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS vishnu(id varchar2 PRIMARY KEY,name varchar2(40),salary int,dept_id varchar(30));")
cur.execute("INSERT INTO vishnu (id,name,salary,dept_id) values(4, 'madhu', 19000, 'D4')")

'''cur.execute("select * from vishnu")
print(cur.fetchall())'''

df=pd.read_sql_query("select * from emp",conn)
ls=df['name'].unique()
base_dir="C:\\Users\\chandrasekhar\\OneDrive - Venusgeo Solution Inc\\DBA_GSMA\\Chandra reports"
for x in ls:
    folders=base_dir + x
    if not os.path.exists(folders):
        os.mkdir(folders)
        df[df['name']==x].to_excel("{}\{}.xlsx".format(folders,x),sheet_name=x,index=False)

conn.commit()
cur.close()
conn.close()
