
# postgreSQL 修改某一字段的值~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# update 你的表名 set 字段名=你想要设为的值 where 表名.字段='原先那个值'

# 修改数据库中某字段，特定位置数值；
sql = '''update info161 set student_name='罗鹏青' where info161.student_name=' 罗鹏青';'''

# 添加新列；
sql = '''ALTER TABLE public."A_C040" ADD price int;'''