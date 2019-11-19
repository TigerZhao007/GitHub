

# ######################################################################################################################
# Sql 四大排名函数（ROW_NUMBER、RANK、DENSE_RANK、NTILE）实例
# ######################################################################################################################

# 1、ROW_NUMBER（推荐）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 查询出来的每一行记录生成一个序号，依次排序且不会重复
sql = '''select * from (
select column_name1, column_name2, column_name3, column_name4,
ROW_NUMBER() over(partition by column_name1, column_name2 order by column_name3 desc, column_name4 desc) as t
from public.table_name) as tt
where tt.t <= 3'''

# 2、RANK~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 分区内每行的排名， 行的排名是相关行之前的排名数加一。
sql = '''select * from (
select column_name1, column_name2, column_name3, column_name4,
RANK() over(partition by column_name1, column_name2 order by column_name3 desc, column_name4 desc) as t
from public.table_name) as tt
where tt.t <= 3'''

# 3、DENSE_RANK~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 生成序号时是连续的，而rank函数生成的序号有可能不连续。
sql = '''select * from (
select column_name1, column_name2, column_name3, column_name4,
DENSE_RANK() over(partition by column_name1, column_name2 order by column_name3 desc, column_name4 desc) as t
from public.table_name) as tt
where tt.t <= 3'''

# 4、NTILE(?)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 对序号进行分组处理，将有序分区中的行分发到指定数目的组中。 各个组有编号，编号从一开始。
sql = '''select * from (
select column_name1, column_name2, column_name3, column_name4,
NTILE() over(partition by column_name1, column_name2 order by column_name3 desc, column_name4 desc) as t
from public.table_name) as tt
where tt.t <= 3'''

# ######################################################################################################################
# Sql 四大排名函数（ROW_NUMBER、RANK、DENSE_RANK、NTILE）说明
# ######################################################################################################################

# 1、ROW_NUMBER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''row_number的用途的非常广泛，排序最好用他，一般可以用来实现web程序的分页，他会为查询出来的每一行记录生成一个序号，
依次排序且不会重复，注意使用row_number函数时必须要用over子句选择对某一列进行排序才能生成序号。row_number用法实例:
'''
sql = '''select ROW_NUMBER() OVER(order by [SubTime] desc) as row_num, *
         from [Order]'''

'''图中的row_num列就是row_number函数生成的序号列，其基本原理是先使用over子句中的排序语句对记录进行排序，
然后按照这个顺序生成序号。over子句中的order by子句与SQL语句中的order by子句没有任何关系，
这两处的order by 可以完全不同，如以下sql，over子句中根据SubTime降序排列，Sql语句中则按TotalPrice降序排列。
'''
sql = '''select ROW_NUMBER() OVER(order by [SubTime] desc) as row_num,*
         from [Order] order by [TotalPrice] desc'''

'''利用row_number可以实现web程序的分页，我们来查询指定范围的表数据。例：根据订单提交时间倒序排列获取第三至第五条数据。
'''
sql = '''with orderSection as (select ROW_NUMBER() OVER(order by [SubTime] desc) rownum,* from [Order])
         select * from [orderSection] where rownum between 3 and 5 order by [SubTime] desc'''

'''注意：在使用row_number实现分页时需要特别注意一点，over子句中的order by 要与Sql排序记录中的order by 保持一致，
否则得到的序号可能不是连续的。下面我们写一个例子来证实这一点，将上面Sql语句中的排序字段由SubTime改为TotalPrice。
另外提一下，对于带有子查询和CTE的查询，子查询和CTE查询有序并不代表整个查询有序，除非显示指定了order by。
'''
sql = '''with orderSection as (select ROW_NUMBER() OVER(order by [SubTime] desc) rownum,* from [Order])
         select * from [orderSection] where rownum between 3 and 5 order by [TotalPrice] desc'''

# 2、RANK~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''rank函数用于返回结果集的分区内每行的排名， 行的排名是相关行之前的排名数加一。
简单来说rank函数就是对查询出来的记录进行排名，与row_number函数不同的是，
rank函数考虑到了over子句中排序字段值相同的情况，如果使用rank函数来生成序号，
over子句中排序字段值相同的序号是一样的，后面字段值不相同的序号将跳过相同的排名号排下一个，
也就是相关行之前的排名数加一，可以理解为根据当前的记录数生成序号，后面的记录依此类推。
可能我描述的比较苍白，理解起来也比较吃力，我们直接上代码，rank函数的使用方法与row_number函数完全相同。
'''
sql = '''select RANK() OVER(order by [UserId]) as rank,* from [Order] '''

'''rank函数在进行排名时，同一组的序号是一样的，而后面的则是根据当前的记录数依次类推，
图中第一、二条记录的用户Id相同，所以他们的序号是一样的，第三条记录的序号则是3。　　'''

# 3、DENSE_RANK~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''dense_rank函数的功能与rank函数类似，dense_rank函数在生成序号时是连续的，而rank函数生成的序号有可能不连续。
dense_rank函数出现相同排名时，将不跳过相同排名号，rank值紧接上一次的rank值。在各个分组内，rank()是跳跃排序，
有两个第一名时接下来就是第四名，dense_rank()是连续排序，有两个第一名时仍然跟着第二名。
将上面的Sql语句改由dense_rank函数来实现。
'''
sql = '''select DENSE_RANK() OVER(order by [UserId]) as den_rank,* from [Order]'''

'''图中第一、二条记录的用户Id相同，所以他们的序号是一样的，第三条记录的序号紧接上一个的序号，
所以为2不为3，后面的依此类推。'''

# 4、DENSE_RANK~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''ntile函数可以对序号进行分组处理，将有序分区中的行分发到指定数目的组中。 各个组有编号，编号从一开始。 
对于每一个行，ntile 将返回此行所属的组的编号。这就相当于将查询出来的记录集放到指定长度的数组中，
每一个数组元素存放一定数量的记录。ntile函数为每条记录生成的序号就是这条记录所有的数组元素的索引（从1开始）。
也可以将每一个分配记录的数组元素称为“桶”。ntile函数有一个参数，用来指定桶数。
下面的SQL语句使用ntile函数对Order表进行了装桶处理：
'''
sql = '''select NTILE(4) OVER(order by [SubTime] desc) as ntile,* from [Order]'''

'''Order表的总记录数是6条，而上面的Sql语句ntile函数指定的组数是4，
那么Sql Server2005是怎么来决定每一组应该分多少条记录呢？这里我们就需要了解ntile函数的分组依据（约定）。

ntile函数的分组依据（约定）：
1、每组的记录数不能大于它上一组的记录数，即编号小的桶放的记录数不能小于编号大的桶。
也就是说，第1组中的记录数只能大于等于第2组及以后各组中的记录数。
2、所有组中的记录数要么都相同，要么从某一个记录较少的组（命名为X）开始后面所有组的记录数都与该组（X组）的记录数相同。
也就是说，如果有个组，前三组的记录数都是9，而第四组的记录数是8，那么第五组和第六组的记录数也必须是8。
'''


