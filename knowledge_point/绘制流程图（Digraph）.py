# -*- coding: utf-8 -*-
"""
时间：2019-10-13
作者: zuoshao（佐少）
代码说明：python绘制流程图
"""

# 导入所需要的模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from graphviz import Digraph

# ######################################################################################################################
# python绘制流程图
# ######################################################################################################################

# 产品购课退课数量&金额计算流程图~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gz=Digraph("产品购课退课数量&金额计算流程图",'comment',None,None,'png',None,"UTF-8",
           {'rankdir':'TB'},
           {'color':'black','fontcolor':'black','fontname':'SimSun','fontsize':'12','style':'rounded','shape':'box'},
           {'color':'#999999','fontcolor':'#888888','fontsize':'10','fontname':'SimSun'},None,False)

gz.node('a','course',{'color':'blue','fontcolor':'blue'})
gz.node('b','Courseedu_subject',{'color':'blue','fontcolor':'blue'})
gz.node('c','course_subject',{'color':'blue','fontcolor':'blue'})
gz.node('d','product_info_vip_db')

gz.node('e','product_info_vip_ry20190614',{'color':'green','fontcolor':'green'})
gz.node('f','product_info_relation')

gz.node('g','pcenter_payment',{'color':'blue','fontcolor':'blue'})
gz.node('h','pcenter_payment_buy')
gz.node('i','pcenter_payment_buy_main')
gz.node('j','product_vip_buy_ymd')
gz.node('k','pcenter_payment_ref')
gz.node('l','pcenter_payment_ref_main')
gz.node('m','product_vip_ref_ymd')
gz.node('n','product_vip',{'color':'red','fontcolor':'red'})

a1 = set(['ad'])
a2 = set(['bd'])
a3 = set(['cd'])
b1 = set(['ef'])

gz.edges(a1|a2|a3|b1)
# gz.edge('d','f','根据产品ProductID关联')
gz.edge('d','g','根据产品ProductID关联')

gz.edge('g','h','合并两种支付方式，计算购课金额')
gz.edge('d','h','添加班级ID')
gz.edge('f','h','添加主课程代码')

gz.edge('h','i','计算每个用户每个订单主课程数量和金额')
gz.edge('i','j','分别计算每日主课程和其他交费购课数量和金额')

gz.edge('g','k','合并两种支付方式，计算退课金额')
gz.edge('d','k','添加班级ID')
gz.edge('f','k','添加主课程代码')
gz.edge('k','l','计算每个用户每个订单主课程数量和金额')
gz.edge('l','m','分别计算每日主课程和其他交费退课数量和金额')

gz.edge('j','n','合并')
gz.edge('m','n','合并')

# print(gz.source)
gz.view()

# 产品退课原因数量&金额计算流程图~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gz=Digraph("产品退课原因数量&金额计算流程图",'comment',None,None,'png',None,"UTF-8",
           {'rankdir':'TB'},
           {'color':'black','fontcolor':'black','fontname':'SimSun','fontsize':'12','style':'rounded','shape':'box'},
           {'color':'#999999','fontcolor':'#888888','fontsize':'10','fontname':'SimSun'},None,False)

gz.node('a','course',{'color':'blue','fontcolor':'blue'})
gz.node('b','Courseedu_subject',{'color':'blue','fontcolor':'blue'})
gz.node('c','course_subject',{'color':'blue','fontcolor':'blue'})
gz.node('d','product_info_vip_db')

gz.node('e','product_info_vip_ry20190614',{'color':'green','fontcolor':'green'})
gz.node('f','product_info_relation')

gz.node('g','Pay_CourseFavourableCause',{'color':'blue','fontcolor':'blue'})
gz.node('h','refund_reason_list')

gz.node('i','pcenter_payment',{'color':'blue','fontcolor':'blue'})
gz.node('j','product_refund')

gz.node('k','Pay_Payment',{'color':'blue','fontcolor':'blue'})
gz.node('l','Pay_PaymentRefundment',{'color':'blue','fontcolor':'blue'})
gz.node('m','Pay_CourseFavourableCause',{'color':'blue','fontcolor':'blue'})

gz.node('n','product_refund_caiwu')
gz.node('o','product_refund_yewu')

gz.node('p','Sale_OrderRefund',{'color':'blue','fontcolor':'blue'})
gz.node('q','Sale_OrderRefundDetail',{'color':'blue','fontcolor':'blue'})
gz.node('r','product_refund_list')

gz.node('s','product_refund_total')

gz.node('t','product_refund_t',{'color':'red','fontcolor':'red'})

gz.edges(set(['ad'])|set(['bd'])|set(['cd'])|set(['ef'])|set(['gh'])|set(['ij'])|
         set(['kn'])|set(['lk'])|set(['ml'])|set(['pr'])|set(['qp'])|
         set(['ro'])|set(['js'])|set(['st']))

gz.edge('n','j','合并')
gz.edge('o','j','合并')
gz.edge('h','s','添加原因名称')
gz.edge('d','s','添加班级ID')
gz.edge('f','s','添加主课程代码')
gz.edge('d','k','提供产品ID')
gz.edge('d','i','提供产品ID')
gz.edge('n','p','提供财务表没有找到原因的产品ID')

# print(gz.source)
gz.view()

# 会计网所有产品购课退课数量&金额计算流程图~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gz=Digraph("会计网所有产品购课退课数量&金额计算流程图",'comment',None,None,'png',None,"UTF-8",
           {'rankdir':'TB'},
           {'color':'black','fontcolor':'black','fontname':'SimSun','fontsize':'12','style':'rounded','shape':'box'},
           {'color':'#999999','fontcolor':'#888888','fontsize':'10','fontname':'SimSun'},None,False)

gz.node('a','pcenter_payment',{'color':'blue','fontcolor':'blue'})
gz.node('b','pcenter_account',{'color':'blue','fontcolor':'blue'})
gz.node('c','product_buy')
gz.node('d','product_refund')
gz.node('e','product_rechage')
gz.node('f','product_rebate')
gz.node('g','product_total',{'color':'red','fontcolor':'red'})

gz.edges(set(['ac'])|set(['ad'])|set(['be'])|set(['bf'])|set(['cg'])|set(['dg'])|
         set(['eg'])|set(['fg']))

# gz.edge('d','g','根据产品ProductID关联')

gz.view()


