
# 数据库类型简介
原文链接：https://www.cnblogs.com/quyong/p/6688113.html

# 1.1  数据库介绍
## 1.1.1什么是数据库
简单的说，数据库（database）就是一个存放数据的仓库，这个仓库是按照一定的数据结构
（数据结构是指数据的组织形式或数据之间的联系）来组织、存储的，
我们可以通过数据提供的多种方法来管理数据库里的数据。

当人们收集了大量的数据后，应该把它们保存起来进入近一步的处理，进一步的抽取有用的信息。当
年人们把数据存放在文件柜中，可现在随着社会的发展，数据量急剧增长，现在人们就借助计算机和数据库技术科学的保存大量的数据，
以便能更好的利用这些数据资源。

# 1.2数据库的种类
数据库通常分为`层次式数据库`、`网络式数据库`和`关系式数据库`三种。
而不同的数据库是按不同的数据结构来联系和组织的。而在当今的互联网中，最常见的数据库模型主要是两种，
即关系型数据库和非关系型数据库。

## 1.2.1关系型数据库介绍
####  （1）、关系型数据库的由来
虽然网状数据库和层次数据库已经很好的解决了数据的集中和共享问题，但是在数据库独立性和抽象级别上扔有很大欠缺。
用户在对这两种数据库进行存取时，仍然需要明确数据的存储结构，指出存取路径。而关系型数据库就可以较好的解决这些问题。

#### （2）、关系型数据库介绍
关系型数据库模型是把复杂的数据结构归结为简单的二元关系（即二维表格形式）。在关系型数据库中，对数据的操作几乎
全部建立在一个或多个关系表格上，通过对这些关联的表格分类、合并、连接或选取等运算来实现数据库的管理。

关系型数据库诞生40多年了，从理论产生发展到现实产品，例如：Oracle和MySQL，Oracle在数据库领域上升到霸主地位，
形成每年高达数百亿美元的庞大产业市场。

#### （3）、关系型数据库表格之间的关系举例


## 1.2.2非关系型数据库介绍
### 1.2.2.1 非关系型数据库诞生背景
NoSQL，泛指非关系型的数据库。随着互联网web2.0网站的兴起，传统的关系数据库在应付web2.0网站，
特别是超大规模和高并发的SNS类型的web2.0纯动态网站已经显得力不从心，暴露了很多难以克服的问题，
而非关系型的数据库则由于其本身的特点得到了非常迅速的发展。
NoSql数据库在特定的场景下可以发挥出难以想象的高效率和高性能，它是作为对传统关系型数据库的一个有效的补充。

NoSQL(NoSQL = Not Only SQL )，意即“不仅仅是SQL”，是一项全新的数据库革命性运动，早期就有人提出，
发展至2009年趋势越发高涨。NoSQL的拥护者们提倡运用非关系型的数据存储，相对于铺天盖地的关系型数据库运用，
这一概念无疑是一种全新的思维的注入。

### 1.2.2.2 非关系型数据库种类
#### （1）、键值存储数据库（key-value）
键值数据库就类似传统语言中使用的哈希表。可以通过key来添加、查询或者删除数据库，因为使用key主键访问，
所以会获得很高的性能及扩展性。

键值数据库主要使用一个哈希表，这个表中有一个特定的键和一个指针指向特定的数据。
Key/value模型对于IT系统来说的优势在于简单、易部署、高并发。

典型产品：Memcached、Redis、MemcacheDB

#### （2）、列存储（Column-oriented）数据库
列存储数据库将数据存储在列族中，一个列族存储经常被一起查询的相关数据，比如人类，我们经常会查询某个人的姓名和年龄，
而不是薪资。这种情况下姓名和年龄会被放到一个列族中，薪资会被放到另一个列族中。

这种数据库通常用来应对分布式存储海量数据。

典型产品：Cassandra、HBase

#### （3）、面向文档（Document-Oriented）数据库
文档型数据库的灵感是来自于Lotus Notes办公软件，而且它同第一种键值数据库类似。
该类型的数据模型是版本化的文档，半结构化的文档以特定的格式存储，比如JSON。
文档型数据库可以看作是键值数据库的升级版，允许之间嵌套键值。而且文档型数据库比键值数据库的查询效率更高。

面向文档数据库会将数据以文档形式存储。每个文档都是自包含的数据单元，是一系列数据项的集合。
每个数据项都有一个名词与对应值，值既可以是简单的数据类型，如字符串、数字和日期等；
也可以是复杂的类型，如有序列表和关联对象。数据存储的最小单位是文档，同一个表中存储的文档属性可以是不同的，
数据可以使用XML、JSON或JSONB等多种形式存储。

典型产品：MongoDB、CouchDB

#### （4）、图形数据库
图形数据库允许我们将数据以图的方式存储。实体会被作为顶点，而实体之间的关系则会被作为边。
比如我们有三个实体，Steve Jobs、Apple和Next，则会有两个“Founded by”的边将Apple和Next连接到Steve Jobs。

典型产品：Neo4J、InforGrid

## 1.3 常用关系型数据库产品介绍
### 1.3.1 Oracle数据库
ORACLE数据库系统是美国ORACLE公司（甲骨文）提供的以分布式数据库为核心的一组软件产品，是目前最流行的客户/服务器
(CLIENT/SERVER)或B/S体系结构的数据库之一。比如SilverStream就是基于数据库的一种中间件。
ORACLE数据库是目前世界上使用最为广泛的数据库管理系统，作为一个通用的数据库系统，它具有完整的数据管理功能；
作为一个关系数据库，它是一个完备关系的产品；作为分布式数据库它实现了分布式处理功能。
但它的所有知识，只要在一种机型上学习了ORACLE知识，便能在各种类型的机器上使用它。

Oracle数据库最新版本为Oracle Database 12c。Oracle数据库12c 引入了一个新的多承租方架构，使用该架构可轻松部署和管理数据库云。
此外，一些创新特性可最大限度地提高资源使用率和灵活性，如Oracle Multitenant可快速整合多个数据库，
而Automatic Data Optimization和Heat Map能以更高的密度压缩数据和对数据分层。
这些独一无二的技术进步再加上在可用性、安全性和大数据支持方面的主要增强，
使得Oracle数据库12c 成为私有云和公有云部署的理想平台。 

### 1.3.2 MySQL数据库
MySQL（发音为"my ess cue el"，不是"my sequel"）是一种开放源代码的关系型数据库管理系统（RDBMS），
MySQL数据库系统使用最常用的数据库管理语言--结构化查询语言（SQL）进行数据库管理。

由于MySQL是开放源代码的，因此任何人都可以在General Public License的许可下下载并根据个性化的需要对其进行修改。
MySQL因为其速度、可靠性和适应性而备受关注。大多数人都认为在不需要事务化处理的情况下，MySQL是管理内容最好的选择。

MySQL这个名字，起源不是很明确。一个比较有影响的说法是，基本指南和大量的库和工具带有前缀“my”已经有10年以上，
而且不管怎样，MySQL AB创始人之一的Monty Widenius的女儿也叫My。这两个到底是哪一个给出了MySQL这个名字至今依然是个迷，
包括开发者在内也不知道。 

### 1.3.3 MariaDB数据库
MariaDB数据库管理系统是MySQL的一个分支，主要由开源社区在维护，采用GPL授权许可。开发这个分支的原因之一是：
甲骨文公司收购了MySQL后，有将MySQL闭源的潜在风险，因此社区采用分支的方式来避开这个风险。 
MariaDB的目的是完全兼容MySQL，包括API和命令行，使之能轻松成为MySQL的代替品。
在存储引擎方面，使用XtraDB（英语：XtraDB）来代替MySQL的InnoDB。 
MariaDB由MySQL的创始人Michael Widenius（英语：Michael Widenius）主导开发，
他早前曾以10亿美元的价格，将自己创建的公司MySQL AB卖给了SUN，此后，随着SUN被甲骨文收购，
MySQL的所有权也落入Oracle的手中。MariaDB名称来自Michael Widenius的女儿Maria的名字。

### 1.3.4 SqlServer数据库
SQL Server是由Microsoft开发和推广的关系数据库管理系统（DBMS），它最初是由Microsoft、Sybase和Ashton-Tate三家公司共同开发的，
并于1988年推出了第一个OS/2版本。Microsoft SQL Server近年来不断更新版本，1996年，Microsoft 推出了SQL Server 6.5版本；
1998年，SQL Server 7.0版本和用户见面；SQL Server 2000是Microsoft公司于2000年推出，
目前最新版本是2012年3月份推出的SQL SERVER 2012。

### 1.3.5 Access数据库
Microsoft Office Access是微软把数据库引擎的图形用户界面和软件开发工具结合在一起的一个数据库管理系统。
它是微软OFFICE的一个成员, 在包括专业版和更高版本的office版本里面被单独出售。
2012年12月4日,最新的微软Office Access 2013在微软Office 2013里发布,微软Office Access 2010 是前一个版本。

MS ACCESS以它自己的格式将数据存储在基于Access Jet的数据库引擎里。它还可以直接导入或者链接数据
(这些数据存储在其他应用程序和数据库)。

软件开发人员和数据架构师可以使用Microsoft Access开发应用软件,“高级用户”可以使用它来构建软件应用程序。
和其他办公应用程序一样，ACCESS支持Visual Basic宏语言,它是一个面向对象的编程语言,可以引用各种对象，包括DAO(数据访问对象),
ActiveX数据对象,以及许多其他的ActiveX组件。可视对象用于显示表和报表，他们的方法和属性是在VBA编程环境下，
VBA代码模块可以声明和调用Windows操作系统函数。

### 1.3.6 其他不常用数据库
DB2，PostgreSQL，Informix，Syase等。

## 1.4 常用非关系型数据库产品介绍
#### 1.4.1 Memcached（key-value）
memcached是一套分布式的快取系统，当初是Danga Interactive为了LiveJournal所发展的，但被许多软件（如MediaWiki）所使用。
这是一套开放源代码软件，以BSD license授权协议发布。[1] 

memcached缺乏认证以及安全管制，这代表应该将memcached服务器放置在防火墙后。[1] 

memcached的API使用32位元的循环冗余校验（CRC-32）计算键值后，将资料分散在不同的机器上。当表格满了以后，
接下来新增的资料会以LRU机制替换掉。由于memcached通常只是当作快取系统使用，所以使用memcached的应用程式在写回较慢的系统时
（像是后端的数据库）需要额外的程式码更新memcached内的资料[1] 

memcached 是以LiveJournal 旗下Danga Interactive 公司的Brad Fitzpatric 为首开发的一款软件。
已成为mixi、hatena、Facebook、Vox、LiveJournal等众多服务中提高Web应用扩展性的重要因素。
许多Web应用都将数据保存到RDBMS中，应用服务器从中读取数据并在浏览器中显示。
但随着数据量的增大、访问的集中，就会出现RDBMS的负担加重、数据库响应恶化、网站显示延迟等重大影响。

这时就该memcached大显身手了。memcached是高性能的分布式内存缓存服务器。一般的使用目的是，通过缓存数据库查询结果，
减少数据库访问次数，以提高动态Web应用的速度、提高可扩展性。

Memcached 的守护进程（daemon ）是用C写的，但是客户端可以用任何语言来编写，并通过memcached协议与守护进程通信。
但是它并不提供冗余（例如，复制其hashmap条目）；当某个服务器S停止运行或崩溃了，所有存放在S上的键/值对都将丢失。

Memcached由Danga Interactive开发，其最新版本发布于2010年，作者为Anatoly Vorobey和Brad Fitzpatrick。
用于提升LiveJournal.com访问速度的。LJ每秒动态页面访问量几千次，用户700万。Memcached将数据库负载大幅度降低，
更好的分配资源，更快速访问。

### 1.4.2 Redis（key-value）
redis是一个key-value存储系统。和Memcached类似，它支持存储的value类型相对更多，
包括string(字符串)、list(链表)、set(集合)、zset(sorted set --有序集合)和hash（哈希类型）。
这些数据类型都支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。
在此基础上，redis支持各种不同方式的排序。与memcached一样，为了保证效率，数据都是缓存在内存中。
区别的是redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，并且在此基础上实现了master-slave(主从)同步。

Redis 是一个高性能的key-value数据库。 redis的出现，很大程度补偿了memcached这类key/value存储的不足，
在部分场合可以对关系数据库起到很好的补充作用。
它提供了Java，C/C++，C#，PHP，JavaScript，Perl，Object-C，Python，Ruby，Erlang等客户端，使用很方便。[1] 

Redis支持主从同步。数据可以从主服务器向任意数量的从服务器上同步，从服务器可以是关联其他从服务器的主服务器。
这使得Redis可执行单层树复制。从盘可以有意无意的对数据进行写操作。由于完全实现了发布/订阅机制，
使得从数据库在任何地方同步树时，可订阅一个频道并接收主服务器完整的消息发布记录。
同步对读取操作的可扩展性和数据冗余很有帮助。 

### 1.4.3 MongoDB（Document-oriented）
MongoDB是一个基于分布式文件存储的数据库。由C++语言编写。旨在为WEB应用提供可扩展的高性能数据存储解决方案。

MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。
他支持的数据结构非常松散，是类似json的bson格式，因此可以存储比较复杂的数据类型。
Mongo最大的特点是他支持的查询语言非常强大，其语法有点类似于面向对象的查询语言，
几乎可以实现类似关系数据库单表查询的绝大部分功能，而且还支持对数据建立索引。 

### 1.4.4 Cassandra（Column-oriented）
Cassandra是一个混合型的非关系的数据库，类似于Google的BigTable。其主要功能比Dynamo （分布式的Key-Value存储系统）更丰富，
但支持度却不如文档存储MongoDB（介于关系数据库和非关系数据库之间的开源产品，是非关系数据库当中功能最丰富，最像关系数据库的。
支持的数据结构非常松散，是类似json的bjson格式，因此可以存储比较复杂的数据类型）。
Cassandra最初由Facebook开发，后转变成了开源项目。它是一个网络社交云计算方面理想的数据库。
以Amazon专有的完全分布式的Dynamo为基础，结合了Google BigTable基于列族（Column Family）的数据模型。
P2P去中心化的存储。很多方面都可以称之为Dynamo 2.0。

### 1.4.5 其他不常用非关系型数据库
HBase、MemacheDB、BerkeleyDB、Tokyo Cabinet

## 1.5 数据库相关知识
### 1.5.1数据库软件企业应用排名参考



