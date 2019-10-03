
# Oracle数据库的安装
> 参考链接：<br>
https://blog.csdn.net/qq_37768482/article/details/77963109

# Oracle数据库的JAVA环境配置
> 参考链接：<br>
https://www.cnblogs.com/yif1991/p/5202385.html

# 创建本地数据库
> 参考链接：<br>
https://www.cnblogs.com/zx-n/p/6150071.html

# Oracle 11g数据库详细安装步骤图解

1.Oracle官网上下载11g<br>
适用于 Microsoft Windows (x64) 的 Oracle Database 11g 第 2 版 (11.2.0.1.0)<br>
下载地址：<br>
> https://www.oracle.com/technetwork/database/enterprise-edition/downloads/index.html<br>
下载时注意：1. 注册并登陆， 2. 接受许可协议（网页最上面），3. 下载对应版本的文件1和文件2<br>
第一步：将两个文件一起解压到同一目录下的同一文件夹内， 路径名称中不要出现中文，也不要出现空格等不规则字符。<br>
https://img-blog.csdn.net/20170913105027660?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzc3Njg0ODI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center<br>
解压完成后，到相应路径下，找到【setup.exe】，双击运行，安装Oracle 11g。<br>
第二步：配置安全更新：本步可将自己的电子邮件地址填写进去（也可以不填写，只是收到一些没什么用的邮件）。取消下面的“我希望通过My Oracle Support接受安全更新(W)”。<br>
https://img-blog.csdn.net/20170913105156017?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzc3Njg0ODI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center<br>
第三步：安全选项：直接选择默认创建和配置一个数据库(安装完数据库管理软件后，系统会自动创建一个数据库实例)。 如图：<br>
https://img-blog.csdn.net/20170913105211810?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzc3Njg0ODI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center<br>
第四步：系统类：直接选择默认的桌面类就可以了。 如图：<br>
https://img-blog.csdn.net/20170913105227107?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzc3Njg0ODI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center<br>
第五步：典型安装：此步骤为重要步骤。<br>
建议只需要将Oracle基目录更新下，目录路径不要含有中文或其它的特殊字符。<br>
全局数据库名可以默认，口令密码必须要牢记。Oracel建议的密码规则必须是大写字母加小写字母加数字，而且必须是8位以上。如图：<br>
https://img-blog.csdn.net/20170913105252390?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzc3Njg0ODI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center<br>
第六步：先决条件检查：本步骤安装程序会检查计算机的软硬件系统是否满足安装此Oracle版本的最低要求。直接下一步即可：<br>
https://img-blog.csdn.net/20170913105321046?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzc3Njg0ODI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center<br>
第七步：<br>
https://img-blog.csdn.net/20170913105341547?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzc3Njg0ODI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center<br>
第八步：
https://img-blog.csdn.net/20170913105407376?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzc3Njg0ODI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center<br>
口令设置<br>

## 配置方法1（不好用）：<br>
1.找到jdk1.6版本，复制bin、jre、lib 三个文件夹<br>
https://img-blog.csdn.net/20170913105505947?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzc3Njg0ODI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center<br>
2.找到Oracle的安装路径：D:\app\Administrator\product\11.2.0\dbhome_1\sqldeveloper<br>
在此路径下新建文件夹：jdk，在jdk文件夹下将在jdk下复制的三个文件夹粘贴<br>
返回到D:\app\Administrator\product\11.2.0\dbhome_1\sqldeveloper路径下，双击sqldeveloper.exe打开数据库<br>
https://img-blog.csdn.net/20170913105534234?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzc3Njg0ODI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center<br>
3.点击数据库左上角的加号新建<br>
https://img-blog.csdn.net/20170913105550898?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzc3Njg0ODI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center<br>
输入以下内容，点击“测试”，若状态为成功，点击链接即可，若失败，返回安装时的口令设置重新设置用户名或口令<br>
https://img-blog.csdn.net/20170913105603679?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzc3Njg0ODI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center<br>

## 配置方法2（推荐）：<br>
安装了64位的Oracle数据库以及32位的Oracle客户端，在开始菜单中第一次打开客户端的SQL Developer时提示输入java.exe的路径，我选择了Oracle数据库自带的jdk路径，确定之后报错：<br>
https://images2015.cnblogs.com/blog/686215/201602/686215-20160219220447066-946333197.png<br>
百度查找解决办法，原因是64位的Oracle数据库中自带的jdk也是64位的，但安装的Oracle客户端是32位的，所以不兼容。<br>

SQL Developer报错：Unable to find a Java Virtual Machine解决办法<br>
> https://www.cnblogs.com/yif1991/p/5202385.html<br>
解决办法一般有两种做法：<br>
1）从网上下载Oracle SQL Developer x64（http://www.oracle.com/technetwork/developer-tools/sql-developer/downloads/index.html），然后替换原目录：D:\app\oracle\product\11.1.0\db_1\sqldeveloper下的32位的Oracle SQL Developer。这样重新启动Oracle SQL Developer 并制定java.exe的路径就可以了。<br>
2）安装JDK6 x86，也就是32位的JDK，虽然我们的系统是64位的，但是也兼容32位的JDK。<br>
> https://www.oracle.com/technetwork/java/javasebusiness/downloads/java-archive-downloads-javase6-419409.html#jdk-6u25-oth-JPR<br>
由于其他需要，我必须使用32位的客户端，所以我选择了第二种办法，在Oracle官网下载了32位jdk安装完成。之后要修改SQL Developer的java.exe启动路径。此时不能在开始菜单中点击SQL Developer定义java.exe路径了，因为该路径已经初始化，一点击SQL Developer就会报上面的错误。此时要想修改java.exe路径需要修改配置文件。<br>
1.在下面的路径中找到sqldeveloper.conf文件<br>
D:\app\mattran\product\11.2.0\client_1\sqldeveloper\sqldeveloper\bin<br>
2.打开该文件<br>
https://images2015.cnblogs.com/blog/686215/201602/686215-20160219221740909-1045359365.png<br>
3.将红线处的路径更改为刚才安装的32位jdk的路径如下：<br>
https://images2015.cnblogs.com/blog/686215/201602/686215-20160219221916753-1003939540.png<br>
4.保存并退出。<br>
之后在开始菜单中点击Oracle - OraClient11g_home1下的SQL Developer就可成功启动。<br>


# 创建数据库<br>
https://www.cnblogs.com/zx-n/p/6150071.html







